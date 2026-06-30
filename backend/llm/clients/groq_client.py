"""
groq_client.py

Centralized Groq provider.
"""

import os

from langchain_groq import (
    ChatGroq
)


class GroqClient:

    def __init__(
        self,
        model_name: str,
        temperature: float = 0
    ):

        self._llm = ChatGroq(
            model=model_name,
            api_key=os.getenv(
                "GROQ_API_KEY"
            ),
            temperature=temperature
        )

    @property
    def llm(
        self
    ):

        return (
            self._llm
        )