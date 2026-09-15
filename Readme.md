# Databricks GenAI Notebook Lab

## 1. Project Overview

This repository is a **hands-on learning laboratory for Generative AI Engineering in Databricks**.

The purpose of this project is to generate a collection of **practical, educational Databricks notebooks** that demonstrate how GenAI concepts can be implemented using realistic examples and synthetic data.

I already have a conceptual understanding of several topics, including:

- RAG (Retrieval-Augmented Generation)
- Vector Databases and Databricks Vector Search
- Document Parsing
- Document Chunking
- Embeddings
- Enriched chunks
- `chunk_to_embed`
- `chunk_to_retrieve`
- `ai_parse_document`
- `ai_prep_search`
- `ai_classify`
- `ai_extract`
- SQL and Python Tools
- MCP (Model Context Protocol)
- MLflow
- Evaluation and monitoring

My objective is to transform this theoretical knowledge into **practical implementations that I can execute, inspect, modify, and understand inside Databricks**.

---

## 2. Important: What This Project Is — and Is Not

### This project IS:

- A collection of educational Databricks notebooks.
- A practical reference for GenAI engineering concepts.
- A set of examples that I can execute manually in my Databricks workspace.
- A way to understand how individual components work.
- A progressive learning path from fundamentals to more advanced architectures.
- A place to experiment with synthetic PDFs, CSVs, text files, and structured datasets.

### This project IS NOT:

- An autonomous data pipeline.
- An application that automatically ingests and processes all available files.
- A production-ready RAG platform.
- A fully automated ETL/ELT framework.
- A system that decides and executes the entire architecture without my intervention.
- A project where Claude Code should execute the complete implementation on my behalf.

### Core principle

**Claude Code should generate notebooks and educational code examples. I should execute, inspect, modify, and connect those examples in Databricks.**

The goal is learning through implementation—not outsourcing the implementation.

---

## 3. Role of Claude Code

Claude Code should act as a:

- GenAI Engineering mentor
- Databricks technical tutor
- Notebook author
- Code reviewer
- Architecture explainer
- Learning-path guide

Claude Code should **not** act as an autonomous pipeline builder.

### Expected behavior

When I ask for a topic, Claude should:

1. Explain the concept briefly.
2. Explain where it fits in a GenAI architecture.
3. Generate a **self-contained example notebook**.
4. Use synthetic or clearly defined sample data.
5. Include comments explaining the important code.
6. Explain the expected inputs and outputs.
7. Explain how I can execute the notebook in Databricks.
8. Explain what I should inspect and experiment with.
9. Suggest follow-up exercises.

### Do not:

- Automatically build the entire project.
- Automatically connect all notebooks into a pipeline.
- Assume that every notebook must be production-ready.
- Create orchestration, Jobs, Workflows, or deployment pipelines unless I explicitly request them.
- Execute ingestion, parsing, embedding, or retrieval workflows on my behalf.
- Replace the learning process with a fully automated implementation.
- Generate large amounts of code without explaining the underlying concepts.

---

## 4. Learning Approach

The project should be organized as a collection of **independent but conceptually connected notebooks**.

Each notebook should focus on one specific concept or a small group of closely related concepts.

The notebooks should be:

- Educational
- Self-contained
- Easy to execute
- Easy to inspect
- Easy to modify
- Focused on one learning objective
- Explicit about prerequisites
- Clear about what is real Databricks functionality versus simulated data

### Preferred learning cycle

```text
Concept
   ↓
Example Notebook
   ↓
Manual Execution in Databricks
   ↓
Inspect Data / Outputs
   ↓
Modify Parameters or Code
   ↓
Experiment
   ↓
Understand Trade-offs
   ↓
Move to the Next Concept
```

---

## 5. Example Business Context

To make the examples realistic, we can use a fictional banking environment.

The fictional institution may have:

- Product documentation
- Operational procedures
- Compliance policies
- Customer service manuals
- Technical documentation
- Structured operational data

All data must be fictional or synthetically generated.

**Never use confidential banking data, customer information, credentials, or proprietary documents.**

The business context is only a vehicle for learning. The notebooks should focus on the technical concepts rather than building a complete banking product.

---

## 6. Notebook Catalog

The repository should contain a progressive collection of notebooks.

The following is the initial suggested catalog. The list can evolve as the project develops.

### Group A — Foundations

#### `01_databricks_genai_environment.ipynb`

**Objective:** Understand the environment and the basic building blocks.

Topics:

- Databricks workspace organization
- Notebooks
- Python and SQL cells
- DataFrames
- Unity Catalog concepts
- Delta tables
- Model / AI capability overview

The notebook should be introductory and should not attempt to build a complete application.

---

#### `02_synthetic_data_generation.ipynb`

**Objective:** Create realistic fake data for the subsequent examples.

Topics:

- Synthetic documents
- Synthetic CSV data
- Structured and unstructured data
- Document metadata
- Reproducible sample data

Examples:

- Fictional banking products
- Fictional operational procedures
- Fictional compliance policies
- Fictional transaction records
- Fictional customer service questions

The notebook should generate or define sample data that can be reused by other notebooks.

---

### Group B — Document Processing

#### `03_document_ingestion_basics.ipynb`

**Objective:** Understand how documents and files can be made available in Databricks.

Topics:

- PDF, CSV, TXT, and other file types
- File paths and volumes
- Reading files
- Binary files versus structured data
- Basic metadata
- Raw document representation

**Important:**

This notebook should demonstrate ingestion concepts using explicit example paths or synthetic files.

It should not automatically scan the workspace and ingest every available file.

---

#### `04_document_parsing_ai_parse_document.ipynb`

**Objective:** Understand document parsing and how unstructured files become usable content.

Topics:

- Document parsing
- `ai_parse_document`
- Text extraction
- Document structure
- Pages
- Headings
- Tables
- Parsing limitations

The notebook should show example input, parsing logic, and expected output.

It should explain any Databricks prerequisites and clearly distinguish actual Databricks functionality from mocked examples.

---

#### `05_document_classification_ai_classify.ipynb`

**Objective:** Understand how AI can classify documents.

Topics:

- Classification
- Categories
- Prompt-based classification
- `ai_classify`
- Structured outputs
- Validation

Example categories:

- Product
- Operations
- Compliance
- Customer Service
- Technical

The notebook should use a small sample dataset and demonstrate the classification process.

---

#### `06_information_extraction_ai_extract.ipynb`

**Objective:** Understand how structured information can be extracted from documents.

Topics:

- Information extraction
- `ai_extract`
- Schema design
- Structured output
- Metadata enrichment
- Validation of extracted fields

Example fields:

- Document category
- Product name
- Department
- Effective date
- Policy type
- Applicable process

The notebook should focus on the extraction concept rather than building a full document-processing pipeline.

---

### Group C — Chunking and Retrieval Preparation

#### `07_document_chunking_basics.ipynb`

**Objective:** Understand why and how documents are divided into chunks.

Topics:

- Why chunking is necessary
- Fixed-size chunking
- Overlap
- Recursive chunking
- Semantic chunking
- Chunk size trade-offs
- Context preservation

The notebook should implement simple examples and allow experimentation with chunk size and overlap.

---

#### `08_enriched_chunks_and_search_preparation.ipynb`

**Objective:** Understand how chunks can be enriched and prepared for retrieval.

Topics:

- Enriched chunks
- Metadata enrichment
- Document context
- Section context
- `ai_prep_search`
- `chunk_to_embed`
- `chunk_to_retrieve`

The notebook should explicitly demonstrate the difference between:

- Original chunk content
- Enriched chunk content
- Content used for embeddings
- Content returned to the LLM

Use small, inspectable examples.

---

#### `09_embeddings_basics.ipynb`

**Objective:** Understand embeddings from a practical perspective.

Topics:

- What embeddings represent
- Text to vector transformation
- Embedding dimensions
- Similarity
- Cosine similarity
- Semantic proximity

The notebook should include simple examples that allow me to compare similar and unrelated texts.

It should explain the difference between understanding embeddings conceptually and using a production embedding model.

---

### Group D — Vector Search and RAG

#### `10_databricks_vector_search.ipynb`

**Objective:** Understand how Databricks Vector Search can be used for semantic retrieval.

Topics:

- Vector Search concepts
- Vector indexes
- Source Delta tables
- Embeddings
- Similarity search
- Top-k retrieval
- Metadata filtering
- Index prerequisites

The notebook should demonstrate the required steps using explicit example data.

It should not assume that the Vector Search infrastructure already exists.

If configuration is required, explain it clearly instead of hiding it behind automation.

---

#### `11_basic_rag_pipeline.ipynb`

**Objective:** Build a minimal RAG example.

Topics:

- User question
- Retrieval
- Context construction
- Prompt template
- LLM response
- Grounded answers
- Source references

The notebook should be intentionally simple.

Expected flow:

```text
Question
   ↓
Retrieve Relevant Chunks
   ↓
Build Context
   ↓
Send Context + Question to LLM
   ↓
Generate Answer
   ↓
Display Sources
```

The notebook should not introduce agents, MCP, or complex orchestration yet.

---

#### `12_rag_failure_cases_and_improvements.ipynb`

**Objective:** Understand why RAG systems fail and how to improve them.

Topics:

- Poor chunking
- Irrelevant retrieval
- Missing context
- Ambiguous questions
- Hallucinations
- Top-k selection
- Metadata filtering
- Prompt improvements

The notebook should include examples of failure cases and experiments to improve retrieval or answer quality.

---

### Group E — Tools and Agents

#### `13_sql_tools_for_genai.ipynb`

**Objective:** Understand how SQL tools can complement RAG.

Topics:

- Tool calling
- SQL tools
- Structured data
- Deterministic queries
- Tool inputs and outputs
- RAG versus SQL

Example:

```text
Question:
"What is the procedure for blocking an account?"
→ RAG

Question:
"How many accounts were blocked last month?"
→ SQL Tool
```

The notebook should use a fictional structured dataset.

---

#### `14_python_tools_for_genai.ipynb`

**Objective:** Understand how Python tools can complement an LLM application.

Topics:

- Python functions as tools
- Input schemas
- Output schemas
- Validation
- Deterministic calculations
- Error handling
- Tool calling

The examples should be safe, simple, and focused on understanding tool invocation.

---

#### `15_mcp_fundamentals.ipynb`

**Objective:** Understand MCP through a practical example.

Topics:

- What MCP is
- MCP clients and servers
- MCP tools
- MCP resources
- MCP prompts
- MCP versus direct tool calling
- Security considerations

The notebook should demonstrate MCP concepts with a minimal example.

If MCP requires a separate local Python component, explain that architecture clearly.

Do not force MCP into Databricks if the environment does not directly support the desired integration.

---

### Group F — MLflow and Evaluation

#### `16_mlflow_for_genai_tracking.ipynb`

**Objective:** Understand how MLflow can support GenAI experimentation.

Topics:

- Experiment tracking
- Parameters
- Outputs
- Traces
- Model interactions
- Retrieval logging
- Evaluation artifacts

The notebook should demonstrate the relevant MLflow capabilities available in the environment.

---

#### `17_rag_evaluation_basics.ipynb`

**Objective:** Understand how to evaluate a RAG application.

Topics:

- Evaluation datasets
- Expected answers
- Retrieval relevance
- Context quality
- Answer correctness
- Groundedness
- Failure analysis

The notebook should compare different retrieval or prompting approaches using a small evaluation dataset.

---

## 7. Notebook Design Standard

Every notebook should follow a consistent educational structure.

### Recommended structure

```text
1. Title and Objective
2. What We Are Learning
3. Prerequisites
4. Conceptual Explanation
5. Example Data
6. Implementation
7. Inspect the Output
8. Experimentation Section
9. Common Errors / Limitations
10. Summary
11. Suggested Exercises
```

### Example notebook introduction

Each notebook should begin with something similar to:

```markdown
# Document Chunking Basics

## Objective

Understand why documents are divided into chunks
and how chunk size and overlap affect retrieval.

## What We Will Learn

- Why chunking is necessary
- How fixed-size chunking works
- How overlap affects context
- How to inspect the resulting chunks

## Prerequisites

- Basic Python
- Basic Databricks notebook usage
- A sample text document
```

---

## 8. Code Generation Guidelines

When generating notebook code:

### Prefer:

- Python
- PySpark
- SQL
- Databricks-native APIs
- Small, readable examples
- Explicit variables
- Clear comments
- Inspectable intermediate results
- Reusable functions when they improve understanding

### Avoid:

- Overengineering
- Unnecessary frameworks
- Complex abstractions
- Hidden automation
- Excessive configuration
- Production deployment code unless explicitly requested
- Large end-to-end pipelines when a small example is sufficient

### Important distinction

The notebooks should prioritize **educational clarity over production optimization**.

However, the code should still demonstrate good engineering practices where they help understanding.

---

## 9. Synthetic Data Guidelines

All examples should use synthetic or fictional data.

Possible data types:

### Unstructured

- PDF documents
- TXT files
- Markdown files
- HTML-like documents
- Policy manuals
- Product guides
- Operational procedures

### Structured

- CSV files
- Delta tables
- Product records
- Fictional transaction data
- Fictional operational metrics
- Evaluation datasets

Synthetic data should be realistic enough to demonstrate the concepts.

It should include enough variety to expose meaningful differences in parsing, chunking, retrieval, and tool usage.

---

## 10. Important Databricks Considerations

Databricks features can depend on:

- Workspace configuration
- Runtime version
- Region
- Model serving availability
- Unity Catalog
- SQL warehouse configuration
- Vector Search availability
- AI Functions availability
- Permissions
- Preview features

Therefore:

- Do not assume every feature is available.
- Identify prerequisites before using a feature.
- Explain workspace-specific configuration.
- Clearly label preview or environment-dependent functionality.
- Do not fabricate execution results.
- Do not claim that a notebook was tested in Databricks unless it was actually tested there.

If a feature cannot be executed in the current environment, provide:

1. A conceptual explanation.
2. A representative notebook example.
3. The expected Databricks implementation.
4. The prerequisites or limitations.

---

## 11. How We Should Work Together

When I request a new notebook, follow this process:

### Step 1 — Clarify the learning objective

Explain what the notebook will teach and why it matters.

### Step 2 — Propose the notebook structure

Show the sections and the expected flow.

### Step 3 — Generate the notebook

Create the notebook code or notebook-compatible content.

### Step 4 — Explain the implementation

Explain the important code and Databricks concepts.

### Step 5 — Explain execution

Tell me what I need to configure or execute manually in Databricks.

### Step 6 — Suggest experiments

Give me exercises such as:

- Change chunk size.
- Change overlap.
- Add metadata.
- Compare retrieval results.
- Modify the prompt.
- Test irrelevant questions.
- Compare SQL and RAG.
- Inspect intermediate outputs.

### Step 7 — Wait for my feedback

Do not automatically continue to the next phase.

Do not generate the entire repository unless I explicitly ask for it.

---

## 12. Definition of Success

This project is successful when I can independently:

- Explain the purpose of each GenAI component.
- Execute the example notebooks in Databricks.
- Modify the implementations.
- Understand the input and output of each step.
- Connect the components into a larger architecture when appropriate.
- Explain the trade-offs between different approaches.
- Identify limitations and failure cases.
- Build a small GenAI application using the concepts I practised.

The objective is not to have Claude build a complete system.

The objective is for **me to become capable of building these systems myself**.

---

## 13. First Task

Start by helping me create the first notebook:

**`02_synthetic_data_generation.ipynb`**

The notebook should generate a small, realistic fictional dataset containing:

- 10–20 fictional banking documents or document-like records.
- Different categories, such as Products, Operations, Compliance, and Customer Service.
- Metadata such as document ID, title, category, and content.
- A small structured CSV-like dataset that may be useful for future SQL tool examples.

Before generating the notebook, explain:

1. What data we should create.
2. Why this data is useful for the future notebooks.
3. What the notebook will and will not do.
4. How I can use its output in later exercises.

Do not create the entire GenAI pipeline at this stage.
