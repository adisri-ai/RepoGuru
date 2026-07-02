"""
search_codebase_tool.py

Semantic search tool.
"""

from langchain_core.tools import tool

from backend.retrieval.retriever import (
    Retriever
)

from backend.retrieval.reranker import (
    Reranker
)

from backend.retrieval.context_builder import (
    ContextBuilder
)

from backend.managers.retreival_metrics_manager import (
    RetrievalMetricsManager
)


class SearchCodebaseTool:

    def __init__(
        self,
        retriever: Retriever,
        metrics_manager: RetrievalMetricsManager
    ):
        self.retriever = retriever
        self.reranker = Reranker()
        self.builder = ContextBuilder()
        self.metrics_manager = (
            metrics_manager
        )

    def get_tool(self):

        @tool
        def search_codebase(
            query: str
        ) -> str:
            """
            Search repository source code,
            classes, functions, modules,
            architecture and implementation details.

            Use this tool whenever the user asks
            questions about repository contents.
            """

            results = (
                self.retriever
                .retrieve_with_scores(
                    query=query,
                    top_k=5
                )
            )

            documents = [
                doc
                for doc, _
                in results
            ]

            scores = [
                score
                for _, score
                in results
            ]

            if scores:

                similarities = [
                    1 / (1 + score)
                    for score in scores
                ]

                avg_similarity = (
                    sum(similarities)
                    /
                    len(similarities)
                )

                self.metrics_manager.add_score(
                    avg_similarity
                )

            ranked = (
                self.reranker.rerank(
                    query,
                    documents
                )
            )

            return (
                self.builder.build(
                    ranked
                )
            )

        return search_codebase