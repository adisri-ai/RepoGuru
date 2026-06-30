"""
database_service.py
"""

from backend.managers.database_manager import (
    DatabaseManager
)

class DatabaseService:

    def __init__(
        self,
        database_manager: DatabaseManager
    ):
        self.database_manager = (
            database_manager
        )

    def create_repository_database(
        self,
        repo_name: str
    ):

        return (
            self.database_manager
            .create_repository_database(
                repo_name
            )
        )

    def get_database(self):

        return (
            self.database_manager
            .get_active_database()
        )

    def store_documents(
        self,
        documents
    ):

        self.get_database().add_documents(
            documents
        )

    def delete_database(self):

        self.database_manager.delete_active_database()