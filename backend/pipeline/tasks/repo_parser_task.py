"""
Reads repository source files.

Converts files into raw text documents.
"""

from pathlib import Path

from backend.pipeline.base.processing_task import (
    ProcessingTask
)

from backend.pipeline.base.pipeline_context import (
    PipelineContext
)


class RepoParserTask(ProcessingTask):

    def execute(
        self,
        context: PipelineContext
    ) -> None:

        documents = []

        for file_path in context.source_files:

            try:

                content = Path(
                    file_path
                ).read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                documents.append(
                    {
                        "path": str(file_path),
                        "content": content
                    }
                )

            except Exception:
                continue

        context.raw_documents = documents