"""
Stores embeddings inside vector database.

Database implementation
will be injected later.
"""

from backend.pipeline.base.processing_task import (
    ProcessingTask
)

from backend.pipeline.base.pipeline_context import (
    PipelineContext
)


class StoreTask(ProcessingTask):

    def __init__(
        self,
        database_service
    ):
        self.database_service = (
            database_service
        )

    def execute(
    self,
    context: PipelineContext
    ) -> None:

        self.database_service.store_documents(
            context.documents
        )

        context.repository.indexed = True