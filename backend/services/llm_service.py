"""
llm_service.py

Facade for all
LLM operations.
"""

from backend.managers.llm_manager import (
    LLMManager
)

from backend.llm.registry.model_registry import (
    MODEL_REGISTRY
)


class LLMService:

    def __init__(
        self,
        llm_manager: LLMManager
    ):

        self.llm_manager = (
            llm_manager
        )

    def switch_model(
        self,
        model_name: str
    ):

        self.llm_manager.switch_model(
            model_name
        )

    def get_current_model(
        self
    ):

        return (
            self.llm_manager
            .get_active_model()
        )

    def get_available_models(
        self
    ):

        return list(
            MODEL_REGISTRY.keys()
        )

    def get_llm(
        self
    ):

        return (
            self.llm_manager
            .get_active_llm()
        )

    def generate_response(
        self,
        messages
    ):

        adapter = (
            self.llm_manager
            .get_active_adapter()
        )

        return adapter.invoke(
            messages
        )