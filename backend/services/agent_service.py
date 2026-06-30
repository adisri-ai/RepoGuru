"""
agent_service.py
"""

from backend.llm.agent_factory import (
    AgentFactory
)


class AgentService:

    def __init__(
        self,
        llm,
        tools
    ):

        self.agent = (
            AgentFactory.create_agent(
                llm=llm,
                tools=tools
            )
        )

    def process_query(
        self,
        query: str,
        chat_history : list
    ) -> str:
        messages =  chat_history + [
                {
                    "role": "user",
                    "content": query
                }
            ]
        print(self.agent)   
        print(type(self.agent))
        response = self.agent.invoke(
            {
                "messages": messages
            }
        )

        return response["messages"][-1].content