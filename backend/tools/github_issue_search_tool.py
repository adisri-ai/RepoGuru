"""
github_issue_search_tool.py

Search GitHub issues
using GitHub REST API.
"""

import requests

from langchain_core.tools import tool


class GithubIssueSearchTool:

    def get_tool(self):

        @tool
        def github_issue_search(
            repository: str,
            query: str
        ) -> str:
            """
            Search GitHub issues.
            """

            url = (
                "https://api.github.com/"
                f"search/issues"
                f"?q={query}+repo:{repository}"
            )

            response = requests.get(
                url,
                timeout=10
            )

            if response.status_code != 200:
                return (
                    "Issue search failed."
                )

            data = response.json()

            issues = []

            for item in (
                data.get(
                    "items",
                    []
                )[:5]
            ):
                issues.append(
                    f"""
Title:
{item['title']}

State:
{item['state']}
"""
                )

            return "\n".join(issues)

        return github_issue_search