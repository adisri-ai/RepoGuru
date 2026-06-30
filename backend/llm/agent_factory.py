"""
agent_factory.py

Creates LangChain agent using
local prompts.
"""

import langchain.agents as la

from backend.config.prompts import (
    SYSTEM_PROMPT
)


class AgentFactory:

    @staticmethod
    def create_agent(
        llm,
        tools
    ):
        llm_with_tools = (
            llm.bind_tools(
                tools
            )
        )

        return la.create_agent(
            model=llm_with_tools,
            tools=tools,
            system_prompt=SYSTEM_PROMPT
        )