"""
file: embeddings.py

- Interact with Embedding Model API (OpenAI-compatiable)
- Embed document chunks
- Vector search returning Top-K chunks
"""

sentence = "Chunking is the process of splitting documents into retrievable units. The vector database indexes chunks, not whole documents. Retrieval returns chunks, not whole documents. The granularity of your chunks determines both what can be retrieved and what context the LLM receives."

from dotenv import load_dotenv


class Embedding:
    def __init__(base_url="http://localhost:8081/v1", api_key="None") -> None:
        pass
