"""
Pipeline orchestrator.

Acts as Template Method implementation.

Workflow:

Parser
→ Chunk
→ Embed
→ Store
"""

from backend.pipeline.base.pipeline_context import (
    PipelineContext
)

from backend.pipeline.base.processing_task import (
    ProcessingTask
)


class ProcessingPipeline:

    def __init__(
        self,
        tasks: list[ProcessingTask]
    ):
        self._tasks = tasks

    def execute(
        self,
        context: PipelineContext
    ) -> None:
        """
        Execute all tasks sequentially.
        """

        for task in self._tasks:
            task.execute(context)