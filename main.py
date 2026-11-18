"""
file: main.py - RAG Agent

 - Retrieve + Generate

      - Retrieve: User query -> Embed (embeddings.py) -> Vector Search (embeddings.py) -> Return Top-K Chunks
      - Generate: (agent) Assemble prompt -> Inject context -> LLM Call -> Grounded Response
"""
