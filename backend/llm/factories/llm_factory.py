"""
llm_factory.py

Factory for creating
LLM adapters.
"""

from backend.llm.adapters.openrouter_adapter import (
    OpenRouterAdapter
)

from backend.llm.registry.model_registry import (
    MODEL_REGISTRY
)
from backend.llm.adapters.ollama_adapter import (
    OllamaAdapter
)
from backend.llm.adapters.groq_adapter import (
    GroqAdapter
)

class LLMFactory:

    @staticmethod
    def create(
        model_alias: str
    ):

        config = (
            MODEL_REGISTRY[
                model_alias
            ]
        )

        provider = (
            config["provider"]
        )

        if provider == (
            "ollama"
        ):

            return (
                OllamaAdapter(
                    config["model"]
                )
            )

        if provider == (
            "openrouter"
        ):

            return (
                OpenRouterAdapter(
                    config["model"]
                )
            )
        if provider == (
            "groq"
        ):

            return (
                GroqAdapter(
                    config["model"]
                )
            )
        raise ValueError(
            f"Unsupported provider: "
            f"{provider}"
        )