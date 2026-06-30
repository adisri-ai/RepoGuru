"""
model_registry.py

Central registry of supported LLMs.

Additional providers such as:
- OpenRouter
- Groq
- Gemini

can be added later without
changing the rest of the system.
"""

MODEL_REGISTRY = {
    "openai/gpt-oss-120b": {

        "provider": "groq",

        "model": "openai/gpt-oss-120b"
    },
    "openai/gpt-oss-20b": {

        "provider": "groq",
        "model": "openai/gpt-oss-20b"
    },
    "qwen/qwen3-32b": {

        "provider": "groq",
        "model": "qwen/qwen3-32b"
    },
    "moonshotai/kimi-k2-instruct": {

        "provider": "groq",
        "model": "moonshotai/kimi-k2-instruct"
    },
    "llama3.2:3b": {

        "provider":
        "ollama",

        "model":
        "llama3.2:3b"
    }

}

DEFAULT_MODEL = (
    "qwen/qwen3-32b"
)