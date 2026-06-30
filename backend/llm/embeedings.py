"""
embeddings.py

Centralized embedding model provider.

Uses Sentence Transformers instead
of Ollama so it works locally and
on Streamlit Cloud.
"""

from langchain_huggingface import (
    HuggingFaceEmbeddings
)


class EmbeddingProvider:

    def __init__(
        self,
        model_name: str = (
            "BAAI/bge-small-en-v1.5"
        )
    ):

        self._embeddings = (
            HuggingFaceEmbeddings(
                model_name=model_name,
                model_kwargs={
                    "device": "cpu"
                },
                encode_kwargs={
                    "normalize_embeddings": True
                }
            )
        )

    @property
    def embeddings(
        self
    ):

        return self._embeddings