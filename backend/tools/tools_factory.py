"""
tools_factory.py

Factory responsible for constructing
all LangChain tools.
"""

from backend.tools.search_codebase_tool import (
    SearchCodebaseTool
)

from backend.tools.read_file_tool import (
    ReadFileTool
)

from backend.tools.dependency_graph_tool import (
    DependencyGraphTool
)

from backend.tools.github_issue_search_tool import (
    GithubIssueSearchTool
 )


class ToolsFactory:

    @staticmethod
    def create_tools(
        retriever , metrics_manager
    ) -> list:

        tools = []

        tools.append(
            SearchCodebaseTool(
                retriever,
                metrics_manager
            ).get_tool()
        )

        tools.append(
            ReadFileTool()
            .get_tool()
        )

        tools.append(
            DependencyGraphTool()
            .get_tool()
        )

        tools.append(
            GithubIssueSearchTool()
            .get_tool()
        )

        return tools