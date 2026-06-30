"""
database_manager.py

Responsible for:

- Creating collections
- Maintaining active collection
- Managing vector store lifecycle
"""

from backend.database.chroma_db import ChromaDB
from backend.database.collection_manager import CollectionManager


class DatabaseManager:

    def __init__(
        self,
        embedding_function,
        persist_directory: str
    ):
        self.embedding_function = embedding_function
        self.persist_directory = persist_directory

        self.collection_manager = (
            CollectionManager()
        )

        self.active_db = None

    def create_repository_database(
        self,
        repo_name: str
    ) -> ChromaDB:

        collection_name = (
            self.collection_manager
            .create_collection_name(
                repo_name
            )
        )

        self.active_db = ChromaDB(
            collection_name=collection_name,
            embedding_function=self.embedding_function,
            persist_directory=self.persist_directory
        )

        return self.active_db

    def get_active_database(
        self
    ) -> ChromaDB:

        if self.active_db is None:
            raise RuntimeError(
                "No active database."
            )

        return self.active_db

    def delete_active_database(
        self
    ) -> None:

        if self.active_db:
            self.active_db.delete_collection()

        self.active_db = None