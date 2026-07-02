"""
read_file_tool.py

Returns full file content.
"""

from pathlib import Path

from langchain_core.tools import tool


class ReadFileTool:

    def get_tool(self):

        @tool
        def read_file(
            file_path: str
        ) -> str:
            """
            Read the complete contents of a file
            from the repository.

            Use when specific implementation
            details are required.
            """

            try:

                return Path(
                    file_path
                ).read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

            except Exception as ex:

                return str(ex)

        return read_file