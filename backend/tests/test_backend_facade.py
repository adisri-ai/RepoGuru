"""
Backend facade tests.
"""

from backend.main import (
    BackendFacade
)


def test_facade_creation():

    facade = BackendFacade()

    assert facade is not None