# Two pipelines

1 - Offline -> Index:

    - Load Documents (documents.py) -> Chunk (documents.py) -> Embed (embeddings.py) -> Store in VectorDB (db/)

2 - Online -> Retrieve and Generate:

      - Retrieve: User query -> Embed (embeddings.py) -> Vector Search (embeddings.py) -> Return Top-K Chunks
      - Generate: (agent) Assemble prompt -> Inject context -> LLM Call -> Grounded Response

## My thoughts

- what i have atm?
  - LLM class that calls LLM
  - a persistence class for DB -> DB engine

- What i need to build?
  - an Embedding Class:
    - api call to embedding model
    - an embed function
    - a vector search functionality that return Top-K chunks

  - Document class:
    - Loading different file type
      - turn the file into a text (string)
    - a Chunk function that takes the file's content and chunk them properly

- Add a functionality for LLM (agent) for using RAG

(RAG)[https://myengineeringpath.dev/genai-engineer/rag/]
