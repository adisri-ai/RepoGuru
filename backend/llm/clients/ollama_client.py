"""
ollama_client.py

Centralized LLM provider.

Allows future migration to:
- Gemini
- OpenAI
- Claude

without affecting services.
"""

from langchain_ollama import ChatOllama


class OllamaClient:

    def __init__(
        self,
        model_name: str = "llama3.2:3b",
        temperature: float = 0
    ):

        self._llm = ChatOllama(
            model=model_name,
            temperature=temperature
        )

    @property
    def llm(self):
        return self._llm