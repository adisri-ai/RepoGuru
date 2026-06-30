"""
openrouter_client.py

Centralized OpenRouter client.

Keeps interface identical
to OllamaClient.
"""

import os

from langchain_openai import (
    ChatOpenAI
)


class OpenRouterClient:

    def __init__(
        self,
        model_name: str,
        temperature: float = 0
    ):

        self._llm = ChatOpenAI(
            model=model_name,
            api_key="",
            base_url=
            "https://openrouter.ai/api/v1",
            temperature=temperature
        )

    @property
    def llm(
        self
    ):
        return self._llm