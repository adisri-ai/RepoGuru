"""
dependency_graph_tool.py

Provides dependency analysis.
"""

from pathlib import Path

from langchain_core.tools import tool


class DependencyGraphTool:

    def get_tool(self):

        @tool
        def dependency_graph(
            file_path: str
        ) -> str:
            """
            Extract import statements.
            """

            try:

                lines = Path(
                    file_path
                ).read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).splitlines()

                imports = []

                for line in lines:

                    line = line.strip()

                    if (
                        line.startswith(
                            "import "
                        )
                        or
                        line.startswith(
                            "from "
                        )
                    ):
                        imports.append(line)

                return "\n".join(imports)

            except Exception as ex:

                return str(ex)

        return dependency_graph