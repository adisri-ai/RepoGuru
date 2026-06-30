"""
retrieval_service.py
"""

from backend.retrieval.retriever import (
    Retriever
)

from backend.retrieval.reranker import (
    Reranker
)

from backend.retrieval.context_builder import (
    ContextBuilder
)


class RetrievalService:

    def __init__(
        self,
        retriever: Retriever
    ):

        self.retriever = retriever
        self.reranker = Reranker()
        self.builder = ContextBuilder()

    def retrieve_context(
        self,
        query: str
    ) -> str:

        docs = self.retriever.retrieve(
            query=query
        )

        docs = self.reranker.rerank(
            query=query,
            documents=docs
        )

        return self.builder.build(
            docs
        )