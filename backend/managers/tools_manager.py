"""
tools_manager.py

Central tool registry.

Acts like a Tool Factory.
"""

class ToolsManager:

    def __init__(self):

        self._tools = {}

    def register_tool(
        self,
        name: str,
        tool
    ) -> None:

        self._tools[name] = tool

    def get_tool(
        self,
        name: str
    ):

        return self._tools.get(name)

    def get_all_tools(
        self
    ) -> list:

        return list(
            self._tools.values()
        )

    def clear_tools(
        self
    ) -> None:

        self._tools.clear()