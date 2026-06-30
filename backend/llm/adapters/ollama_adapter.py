from backend.llm.adapters.llm_adapter import (
    LLMAdapter
)

from backend.llm.clients.ollama_client import (
    OllamaClient
)


class OllamaAdapter(
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
            OllamaClient(
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

    def get_llm(
        self
    ):

        return self.llm

    def get_model_name(
        self
    ):

        return self.model_name