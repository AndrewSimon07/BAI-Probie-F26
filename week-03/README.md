# Week 03 - RAG System

A simple RAG (Retrieval-Augmented Generation) system.

## Setup

```bash
# Install dependencies
uv sync
```

Create `.env` with your OpenRouter API key:

```bash
echo "OPENROUTER_API_KEY=your-openrouter-api-key" > .env
```

Get the key from the BAI Probie GitHub homepage

## Usage
To populate your vector database, first run the ingestion pipeline:

```bash
python -m src.scripts.ingest
```

Type facts to persist them to the Vector Database, type 'search' to search, or 'quit' to exit. Try to enter facts that are not in the LLM's pretrained knowledge. For example, a good fact to enter would be "My dog's name is Fido," and a bad example would be "The capital of France is Paris" - the first fact will truly test whether your RAG system works since it contains knowledge outside the LLM's purview.

Run the RAG chat agent:

```bash
python -m src.scripts.run_agent
```

## Structure

- `src/services/embedding/` - OpenAI embedding generation
- `src/services/vector_database/` - ChromaDB vector storage
- `src/agent/` - RAG agent implementation
- `src/scripts/ingest.py` - Interactive CLI for ingesting facts (with Rich formatting)

## Assignment Tasks (TODOs)

Implement the following. Keep code async and production-grade.

- Vector DB:
  - `src/services/vector_database/service.py::VectorDatabaseService.add_fact`
  - `src/services/vector_database/service.py::VectorDatabaseService.query`
  - `src/services/vector_database/service.py::VectorDatabaseService.format_query_results`
- System prompt:
  - `src/agent/system_prompt.py::RAG_AGENT_SYSTEM_PROMPT`
 - Agent tool:
   - `src/agent/rag_agent.py::perform_rag`

Verification:
- Ingest a few short facts via `python -m src.scripts.ingest`
- Search within the ingest script to confirm nearest neighbors
- Start the chat via `python -m src.scripts.run_agent`
- Ask a question; the answer must be grounded in retrieved facts and list sources
