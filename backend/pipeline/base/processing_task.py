"""
Abstract base class for all processing tasks.
"""

from abc import ABC, abstractmethod

from backend.pipeline.base.pipeline_context import (
    PipelineContext
)


class ProcessingTask(ABC):

    @abstractmethod
    def execute(
        self,
        context: PipelineContext
    ) -> None:
        """
        Execute task and update context.
        """
        pass