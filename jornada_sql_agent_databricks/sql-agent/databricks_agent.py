import json
import os

# Rodando LLM model do Databricks
from databricks_langchain import ChatDatabricks
from db import engine
from dotenv import load_dotenv
from langchain_community.agent_toolkits import SQLDatabaseToolkit, create_sql_agent
from langchain_community.utilities import SQLDatabase

load_dotenv()

CATALOG = os.getenv("DATABRICKS_CATALOG", "erp_farma")
SCHEMA = os.getenv("DATABRICKS_SCHEMA", "gold")

# Descrição das views da camada Gold, baseada nos COMMENTs do Unity Catalog.
# Substitui o DDL gerado automaticamente pelo sql_db_schema, então lista também as colunas.
# Dados de vendas cobrem de 2023-10-07 a 2026-10-06.
TABLE_INFO = {
    "agg_vendas_cupons_diarios": """
View: agg_vendas_cupons_diarios
Número de vendas (cupons) e faturamento por dia, filial e canal.
Grão: data_venda x nome_filial x canal.
Use para: quantidade de vendas, faturamento total e ticket médio = SUM(faturamento) / SUM(quantidade_vendas).
Colunas:
- data_venda DATE: dia da venda
- nome_filial STRING: filial que realizou a venda
- canal STRING: Loja Física, E-commerce, Delivery ou Convênio
- quantidade_vendas BIGINT: número de vendas (cupons) concluídas
- quantidade_clientes_identificados BIGINT: número de vendas com cliente identificado
- faturamento DECIMAL(18,2): faturamento líquido, em reais
""",
    "agg_vendas_diarias": """
View: agg_vendas_diarias
Vendas concluídas por dia, filial, canal, categoria e tipo de produto.
Grão: data_venda x nome_filial x canal x categoria x tipo_produto.
Use para: faturamento, unidades, desconto, custo e margem por categoria/tipo de produto.
NÃO use para contar vendas (cupons): uma venda pode ter itens em várias categorias. Use agg_vendas_cupons_diarios.
Colunas:
- data_venda DATE: dia da venda
- nome_filial STRING: filial que realizou a venda
- canal STRING: Loja Física, E-commerce, Delivery ou Convênio
- categoria STRING: categoria comercial do produto
- tipo_produto STRING: Referência, Genérico, Similar ou Não medicamento
- quantidade_itens BIGINT: total de unidades vendidas
- faturamento DECIMAL(18,2): faturamento líquido, em reais
- valor_desconto DECIMAL(18,2): descontos concedidos, em reais
- custo_total DECIMAL(18,2): custo das unidades vendidas, em reais
- margem_bruta DECIMAL(18,2): faturamento menos custo, em reais
""",
    "agg_pagamentos_diarios": """
View: agg_pagamentos_diarios
Pagamentos recebidos por dia, filial, canal e forma de pagamento.
Grão: data_venda x nome_filial x canal x forma_pagamento.
Use para: totais por forma de pagamento. Para bandeira ou parcelas use fato_pagamentos.
Colunas:
- data_venda DATE: dia da venda
- nome_filial STRING: filial que realizou a venda
- canal STRING: Loja Física, E-commerce, Delivery ou Convênio
- forma_pagamento STRING: PIX, Cartão de Crédito, Cartão de Débito, Dinheiro ou Convênio
- quantidade_pagamentos BIGINT: número de pagamentos recebidos
- valor_pago DECIMAL(18,2): valor recebido, em reais
""",
    "fato_vendas": """
View: fato_vendas
Fato de vendas no grão de item de venda. Contém apenas vendas concluídas (canceladas ficam de fora).
Grão: id_venda x numero_item.
Use para: análises por produto, cliente, vendedor ou hora. Para totais diários prefira as views agg_*.
Contar vendas: COUNT(DISTINCT id_venda). Faturamento: SUM(faturamento).
Joins: id_filial -> dim_filial, id_produto -> dim_produto, id_cliente -> dim_cliente,
id_vendedor -> dim_vendedor, data_venda -> dim_data.data.
Colunas:
- id_venda BIGINT: identificador da venda (cupom); uma venda tem um ou mais itens
- numero_item INT: sequência do item dentro da venda
- data_venda DATE: dia da venda
- data_hora_venda TIMESTAMP: data e hora da venda
- id_filial BIGINT: filial que realizou a venda
- id_cliente BIGINT: cliente identificado; nulo em vendas de balcão sem identificação
- id_vendedor BIGINT: vendedor que atendeu; nulo no e-commerce
- id_produto BIGINT: produto vendido
- canal STRING: Loja Física, E-commerce, Delivery ou Convênio
- quantidade INT: unidades vendidas do produto neste item
- preco_unitario DECIMAL(12,2): preço de tabela por unidade no momento da venda, em reais
- valor_bruto DECIMAL(14,2): quantidade x preço unitário, antes do desconto, em reais
- valor_desconto DECIMAL(14,2): desconto concedido no item, em reais
- faturamento DECIMAL(14,2): valor líquido do item (bruto - desconto); é a medida de faturamento/receita
- custo_total DECIMAL(14,2): custo de aquisição das unidades vendidas, em reais
- margem_bruta DECIMAL(14,2): faturamento - custo_total, em reais
""",
    "fato_pagamentos": """
View: fato_pagamentos
Fato de pagamentos recebidos das vendas concluídas. Grão: um pagamento.
Uma venda pode ter mais de um pagamento: não some valor_pago junto com fato_vendas sem agregar antes.
Joins: id_venda -> fato_vendas.id_venda, id_filial -> dim_filial, data_venda -> dim_data.data.
Colunas:
- id_pagamento BIGINT: identificador do pagamento
- id_venda BIGINT: venda a que o pagamento se refere
- data_venda DATE: dia da venda
- id_filial BIGINT: filial que realizou a venda
- canal STRING: Loja Física, E-commerce, Delivery ou Convênio
- forma_pagamento STRING: PIX, Cartão de Crédito, Cartão de Débito, Dinheiro ou Convênio
- bandeira STRING: bandeira do cartão; nulo quando não é cartão
- parcelas INT: número de parcelas; só é maior que 1 no cartão de crédito
- valor_pago DECIMAL(14,2): valor recebido neste pagamento, em reais
""",
    "fato_estoque": """
View: fato_estoque
Posição diária de estoque por filial, produto e lote, com situação de validade.
Grão: data_posicao x id_filial x id_produto x lote. Hoje só existe a posição de 2026-10-06.
NÃO some quantidades de dias diferentes: filtre WHERE posicao_atual = true (ou uma data_posicao).
Joins: id_filial -> dim_filial, id_produto -> dim_produto.
Colunas:
- data_posicao DATE: dia a que a posição se refere
- posicao_atual BOOLEAN: verdadeiro para a posição mais recente
- id_filial BIGINT: filial onde o estoque está
- id_produto BIGINT: produto em estoque
- lote STRING: código do lote do fabricante
- data_validade DATE: data de validade do lote
- dias_para_vencer INT: dias entre a posição e a validade; negativo = lote vencido
- situacao_validade STRING: Vencido, Vence em até 60 dias, Vence em 61 a 180 dias ou Acima de 180 dias
- quantidade_disponivel INT: unidades disponíveis do lote na filial
- valor_estoque DECIMAL(14,2): quantidade disponível x custo unitário, em reais
""",
    "dim_produto": """
View: dim_produto
Produtos da farmácia: medicamentos e não medicamentos. 703 produtos. Chave: id_produto.
Para o preço praticado em cada venda use fato_vendas.preco_unitario, não preco_venda_atual.
Colunas:
- id_produto BIGINT: chave da dimensão
- ean STRING: código de barras EAN-13
- nome_produto STRING: nome comercial com dosagem e apresentação
- principio_ativo STRING: princípio ativo; nulo para não medicamentos
- laboratorio STRING: laboratório ou marca fabricante
- categoria STRING: categoria comercial, ex.: Analgésicos e Antitérmicos, Dermocosméticos, Higiene Pessoal
- tipo_produto STRING: Referência, Genérico, Similar ou Não medicamento
- eh_medicamento BOOLEAN: verdadeiro para Referência, Genérico ou Similar
- eh_generico BOOLEAN: verdadeiro para medicamento genérico
- tarja STRING: Sem tarja, Vermelha, Preta ou Não se aplica
- controlado BOOLEAN: venda exige retenção de receita (antibióticos e psicotrópicos)
- exige_receita BOOLEAN: só pode ser vendido com prescrição
- fornecedor STRING: razão social do fornecedor
- tipo_fornecedor STRING: Laboratório, Indústria de Consumo ou Distribuidora
- preco_venda_atual DECIMAL(12,2): preço de venda vigente no cadastro, em reais
- preco_custo_atual DECIMAL(12,2): custo de aquisição vigente no cadastro, em reais
- data_cadastro DATE: data de entrada no cadastro
""",
    "dim_filial": """
View: dim_filial
Filiais (lojas) da rede de farmácias. 8 filiais. Chave: id_filial.
Filiais: Barão Geraldo, Cambuí, Hospital Paulínia, Matriz Centro, Shopping Dom Pedro, Sumaré, Valinhos Centro, Vinhedo.
A Matriz Centro também fatura os pedidos do e-commerce.
Colunas:
- id_filial BIGINT: chave da dimensão
- nome_filial STRING: nome da loja (mesmo valor usado em nome_filial nas views agg_*)
- cidade STRING: cidade da filial
- uf STRING: sigla do estado
- bairro STRING: bairro da filial
- tipo_loja STRING: Rua, Shopping ou Hospitalar
- data_abertura DATE: data de inauguração
""",
    "dim_cliente": """
View: dim_cliente
Clientes identificados, sem dados pessoais. Chave: id_cliente.
Vendas de balcão sem identificação não têm cliente (fato_vendas.id_cliente nulo).
Colunas:
- id_cliente BIGINT: chave da dimensão
- sexo STRING: F ou M
- faixa_etaria STRING: Até 24, 25 a 39, 40 a 59 ou 60 ou mais
- cidade STRING: cidade de residência
- uf STRING: sigla do estado de residência
- programa_fidelidade BOOLEAN: participa do programa de fidelidade
- data_cadastro DATE: data de cadastro do cliente
""",
    "dim_vendedor": """
View: dim_vendedor
Vendedores. 51 vendedores. Chave: id_vendedor. Vendas do e-commerce não têm vendedor.
Colunas:
- id_vendedor BIGINT: chave da dimensão
- nome_vendedor STRING: nome do vendedor
- cargo STRING: Atendente, Farmacêutico ou Gerente
- id_filial BIGINT: filial em que está lotado
- nome_filial STRING: nome da filial em que está lotado
- data_admissao DATE: data de admissão
- ativo BOOLEAN: vendedor ativo
""",
    "dim_data": """
View: dim_data
Calendário de 2023-10-07 a 2026-10-06 (do primeiro ao último dia com vendas). Chave: data.
Use para agrupar por mês, trimestre, dia da semana ou fim de semana.
Colunas:
- data DATE: chave da dimensão
- ano INT: ex.: 2025
- trimestre INT: 1 a 4
- mes INT: 1 a 12
- nome_mes STRING: nome do mês em português
- ano_mes STRING: formato AAAA-MM
- dia INT: dia do mês
- dia_semana STRING: nome do dia da semana em português
- fim_de_semana BOOLEAN: verdadeiro para sábado e domingo
""",
}

# 1) Conecta ao Warehouse
db = SQLDatabase(
    engine,
    include_tables=list(TABLE_INFO),
    view_support=True,
    custom_table_info=TABLE_INFO,
)

# 2) LLM (troque por seu provedor preferido)
# llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0) # Rodando LLM model da Open AI
llm = ChatDatabricks(
    endpoint="databricks-gpt-oss-120b"
)  # Rodando LLM model do Databricks

# 3) Toolkit + agente
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

SYSTEM_PROMPT_PT = """
Você é um analista de dados que responde em português, gerando apenas SQL compatível com Databricks SQL
quando precisar consultar dados.

De preferencia para as views agg_* para totais por dia, filial, canal ou categoria.
"""

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type="openai-tools",
    verbose=True,
    handle_parsing_errors=True,
    system_message=SYSTEM_PROMPT_PT,
    top_k=5,
)


def _extract_text(output) -> str:
    """Modelos como o gpt-oss retornam blocos (reasoning + text); fica só com o texto."""
    if isinstance(output, str):
        try:
            output = json.loads(output)
        except ValueError:
            return output
    if isinstance(output, list):
        return "\n".join(
            b.get("text", "")
            for b in output
            if isinstance(b, dict) and b.get("type") == "text"
        ).strip()
    return str(output)


def ask(question: str, retries: int = 2) -> str:
    """Chame isto do seu endpoint/UI."""
    for _ in range(retries + 1):
        text = _extract_text(agent.invoke({"input": question})["output"])
        if text:
            return text
    return "Não consegui gerar uma resposta. Tente reformular a pergunta."
