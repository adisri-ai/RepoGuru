"""
Pipeline tests.
"""

from backend.pipeline.base.pipeline_context import (
    PipelineContext
)


def test_pipeline_context_creation():

    context = PipelineContext(
        repository=None
    )

    assert context.raw_documents == []
    assert context.chunks == []