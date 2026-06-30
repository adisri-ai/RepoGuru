"""
Converts documents into chunks.

Current implementation:
RecursiveCharacterTextSplitter

Future:
AST chunking
Tree-Sitter chunking
"""

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from langchain_core.documents import Document

from backend.pipeline.base.processing_task import (
    ProcessingTask
)

from backend.pipeline.base.pipeline_context import (
    PipelineContext
)


class ChunkTask(ProcessingTask):

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
        )

    def execute(
        self,
        context: PipelineContext
    ) -> None:

        chunks = []
        documents = []

        for document in context.raw_documents:

            texts = self.splitter.split_text(
                document["content"]
            )

            for text in texts:

                chunk = {
                    "content": text,
                    "source": document["path"]
                }

                chunks.append(
                    chunk
                )

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": document["path"]
                        }
                    )
                )

        context.chunks = chunks

        context.documents = documents