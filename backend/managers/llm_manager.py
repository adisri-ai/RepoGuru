"""
llm_manager.py

Maintains active model.
Supports runtime switching.
"""

from backend.llm.factories.llm_factory import (
    LLMFactory
)


class LLMManager:

    def __init__(
        self,
        default_model: str
    ):

        self.active_adapter = (
            LLMFactory.create(
                default_model
            )
        )

    def switch_model(
        self,
        model_name: str
    ):

        self.active_adapter = (
            LLMFactory.create(
                model_name
            )
        )

    def get_active_adapter(
        self
    ):

        return (
            self.active_adapter
        )

    def get_active_llm(
        self
    ):

        return (
            self.active_adapter
            .get_llm()
        )

    def get_active_model(
        self
    ):

        return (
            self.active_adapter
            .get_model_name()
        )