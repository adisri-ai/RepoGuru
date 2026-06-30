"""
Shared state object passed through the pipeline.

Each task can read and update the context.
"""

from dataclasses import dataclass, field
from pathlib import Path

from backend.models.repository import Repository


@dataclass
class PipelineContext:

    repository: Repository

    source_files: list[Path] = field(default_factory=list)

    raw_documents: list = field(default_factory=list)

    chunks: list = field(default_factory=list)

    documents: list = field(default_factory=list)

    embeddings: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)