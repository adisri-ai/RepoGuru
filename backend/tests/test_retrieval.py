"""
Retrieval tests.
"""

from backend.retrieval.context_builder import (
    ContextBuilder
)


class MockDocument:

    def __init__(self):

        self.page_content = (
            "Sample content"
        )

        self.metadata = {
            "source": "test.py"
        }


def test_context_builder():

    builder = ContextBuilder()

    context = builder.build(
        [MockDocument()]
    )

    assert "test.py" in context