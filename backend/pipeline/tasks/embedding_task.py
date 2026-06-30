"""
Creates embeddings for chunks.

Uses embedding service later.

Currently independent.
"""

from backend.pipeline.base.processing_task import (
    ProcessingTask
)

from backend.pipeline.base.pipeline_context import (
    PipelineContext
)


class EmbeddingTask(ProcessingTask):

    def __init__(
        self,
        embedding_model
    ):
        self.embedding_model = (
            embedding_model
        )

    def execute(
    self,
    context: PipelineContext
        ) -> None:

        """
        Embeddings are generated internally
        by Chroma using the configured
        embedding_function.

        This task remains as an extension
        point for future custom embedding
        pipelines.
        """

        return