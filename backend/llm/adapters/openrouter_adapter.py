"""
openrouter_adapter.py

Adapter for OpenRouter models.
"""

from backend.llm.adapters.llm_adapter import (
    LLMAdapter
)

from backend.llm.clients.openrouter_client import (
    OpenRouterClient
)


class OpenRouterAdapter(
    LLMAdapter
):

    def __init__(
        self,
        model_name: str
    ):

        self.model_name = model_name

        self.client = (
            OpenRouterClient(
                model_name=model_name
            )
        )

        self.llm = (
            self.client.llm
)
    def invoke(
        self,
        messages
    ):

        return self.llm.invoke(
            messages
        )

    def get_model_name(
        self
    ) -> str:

        return self.model_name

    def get_llm(
        self
    ):

        return self.llm