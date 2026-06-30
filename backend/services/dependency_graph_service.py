"""
dependency_graph_service.py

Builds repository dependency graph.
"""

import os
import ast

import networkx as nx


class DependencyGraphService:

    def build_graph(
        self,
        repository_path: str
    ):

        graph = nx.DiGraph()

        for root, _, files in os.walk(
            repository_path
        ):

            for file in files:

                if not file.endswith(".py"):
                    continue

                full_path = os.path.join(
                    root,
                    file
                )

                relative_path = os.path.relpath(
                    full_path,
                    repository_path
                )

                graph.add_node(
                    relative_path
                )

                try:

                    with open(
                        full_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        tree = ast.parse(
                            f.read()
                        )

                    for node in ast.walk(
                        tree
                    ):

                        if isinstance(
                            node,
                            ast.Import
                        ):

                            for alias in node.names:

                                graph.add_edge(
                                    relative_path,
                                    alias.name
                                )

                        elif isinstance(
                            node,
                            ast.ImportFrom
                        ):

                            if node.module:

                                graph.add_edge(
                                    relative_path,
                                    node.module
                                )

                except Exception:
                    pass

        return graph