"""
tools_service.py
"""

from backend.managers.tools_manager import (
    ToolsManager
)


class ToolsService:

    def __init__(
        self,
        tools_manager: ToolsManager
    ):
        self.tools_manager = tools_manager

    def register_tool(
        self,
        name: str,
        tool
    ):

        self.tools_manager.register_tool(
            name,
            tool
        )

    def get_tools(self):

        return (
            self.tools_manager
            .get_all_tools()
        )