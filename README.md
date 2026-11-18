# rag-agent

A small RAG (Retrieval-Augmented Generation) agent built on OpenAI-compatible local models, Postgres/pgvector and Valkey.

## Pipelines

1. **Index (offline):** load documents → chunk → embed → store in pgvector
2. **Retrieve + generate (online):** embed query → vector search top-K chunks → inject context → LLM call → grounded answer

## Layout

| Path | Purpose |
|------|---------|
| `llm/` | `LLM` client (OpenAI Responses API) with tool-calling loop and structured output |
| `tools/` | Agent tools (sandboxed file read/write, Valkey session facts) and schema generation |
| `db/` | SQLAlchemy engine, enables the `vector` extension |
| `rag/` | Document loading/chunking and embeddings (WIP) |
| `main.py` | Entry point (WIP) |

## Requirements

- Python 3.13+
- Postgres with [pgvector](https://github.com/pgvector/pgvector)
- Valkey on `localhost:6379`
- An OpenAI-compatible chat server (e.g. `llama-server` on `:8080`) and embedding server (`:8081`)

## Setup

```sh
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then edit values
```

## Status

Work in progress — embeddings, document chunking and the RAG agent loop are being built.
