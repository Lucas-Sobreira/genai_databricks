# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A hands-on **learning laboratory for Generative AI Engineering on Databricks**. The deliverable is a progressive collection of self-contained, educational Databricks notebooks (`.ipynb`) covering RAG, document parsing/chunking/embeddings, Vector Search, SQL/Python tool calling, MCP, and MLflow evaluation — built around a fictional banking business context with synthetic data only.

The repository currently contains only `Readme.md`, `LICENSE`, and a `.claude/skills/senior-data-engineer/` skill package. No notebooks exist yet; the first requested one is `02_synthetic_data_generation.ipynb` (see `Readme.md` section 13).

**Read `Readme.md` in full before generating any notebook.** It is the authoritative project charter, not background reading — it defines the notebook catalog, structure, and workflow contract below.

## Operating contract (critical — do not deviate)

This is a **learning project for the repo owner**, not a request to autonomously build a system. `Readme.md` is explicit and repeated on this point:

- **Do not** build an autonomous pipeline, connect notebooks into a working end-to-end system, create Jobs/Workflows/orchestration, or execute ingestion/parsing/embedding/retrieval on the user's behalf — unless explicitly asked.
- **Do not** generate the entire notebook catalog at once. Work one notebook at a time and stop for feedback before continuing to the next.
- Act as a mentor/tutor/notebook author/code reviewer — not an autonomous implementer. The user executes and inspects notebooks manually in their own Databricks workspace; Claude Code does not have Databricks execution access.
- Every notebook must use **synthetic or fictional data only**. Never use real confidential/banking/customer data.
- Never claim a notebook was tested in Databricks unless it actually was. Databricks features (Unity Catalog, Vector Search, AI Functions, model serving, preview features) are environment/workspace-dependent — state prerequisites explicitly rather than assuming availability.

### Per-notebook workflow (from `Readme.md` §11)

When asked for a new notebook, follow this sequence and stop at step 7 for feedback rather than auto-continuing:

1. Clarify the learning objective (what it teaches, why it matters).
2. Propose the notebook structure/flow.
3. Generate the notebook.
4. Explain the implementation.
5. Explain what to configure/execute manually in Databricks.
6. Suggest follow-up experiments (e.g., change chunk size/overlap, compare retrieval results, modify the prompt).
7. Wait for feedback before moving to the next notebook.

### Required notebook structure (from `Readme.md` §7)

Every notebook follows this section order: Title/Objective → What We Are Learning → Prerequisites → Conceptual Explanation → Example Data → Implementation → Inspect the Output → Experimentation Section → Common Errors/Limitations → Summary → Suggested Exercises.

### Code style for notebooks (from `Readme.md` §8)

Prefer Python, PySpark, SQL, and Databricks-native APIs with small, readable, explicit, well-commented examples that produce inspectable intermediate results. Avoid overengineering, unnecessary frameworks, hidden automation, and production-deployment code unless explicitly requested — educational clarity outweighs production optimization, though good engineering practice should still be demonstrated where it aids understanding.

## Notebook catalog and progression

`Readme.md` §6 defines the full target catalog, organized in dependency order — later groups assume concepts from earlier ones:

- **Group A — Foundations**: `01_databricks_genai_environment`, `02_synthetic_data_generation` (produces the fictional dataset reused by later notebooks)
- **Group B — Document Processing**: `03_document_ingestion_basics`, `04_document_parsing_ai_parse_document`, `05_document_classification_ai_classify`, `06_information_extraction_ai_extract`
- **Group C — Chunking and Retrieval Prep**: `07_document_chunking_basics`, `08_enriched_chunks_and_search_preparation` (`chunk_to_embed` vs `chunk_to_retrieve` vs `ai_prep_search`), `09_embeddings_basics`
- **Group D — Vector Search and RAG**: `10_databricks_vector_search`, `11_basic_rag_pipeline`, `12_rag_failure_cases_and_improvements`
- **Group E — Tools and Agents**: `13_sql_tools_for_genai`, `14_python_tools_for_genai`, `15_mcp_fundamentals`
- **Group F — MLflow and Evaluation**: `16_mlflow_for_genai_tracking`, `17_rag_evaluation_basics`

Treat this list as the intended sequence, but only build the notebook the user actually asks for next.

## The `senior-data-engineer` skill

`.claude/skills/senior-data-engineer/` is a general-purpose data-engineering skill (Airflow/dbt/Spark/Kafka/Flink pipelines, data quality, streaming) with its own `scripts/` (e.g. `pipeline_orchestrator.py`, `data_quality_validator.py`, `kafka_config_generator.py`) and `references/` (`frameworks.md`, `templates.md`, `tools.md`). It is a reusable/imported skill package, not something built for this project — its production-pipeline orientation is broader in scope than what this repo's notebooks should produce. Use it only for genuinely relevant sub-questions (e.g. data quality dimensions, chunking trade-offs framing); do not let its "production-ready pipeline" framing override the learning-lab constraints above.
