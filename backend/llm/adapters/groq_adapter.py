"""
groq_adapter.py
"""

from backend.llm.adapters.llm_adapter import (
    LLMAdapter
)

from backend.llm.clients.groq_client import (
    GroqClient
)


class GroqAdapter(
    LLMAdapter
):

    def __init__(
        self,
        model_name: str
    ):

        self.model_name = (
            model_name
        )

        self.client = (
            GroqClient(
                model_name
            )
        )

    def invoke(
        self,
        messages
    ):

        return (
            self.client.llm.invoke(
                messages
            )
        )

    def get_model_name(
        self
    ) -> str:

        return (
            self.model_name
        )

    def get_llm(
        self
    ):

        return (
            self.client.llm
        )