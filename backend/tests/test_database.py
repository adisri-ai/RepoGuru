"""
Database tests.
"""

from backend.database.collection_manager import (
    CollectionManager
)


def test_collection_name_generation():

    manager = CollectionManager()

    name = manager.create_collection_name(
        "sample_repo"
    )

    assert "sample_repo" in name