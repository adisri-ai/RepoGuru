"""
repository_service.py
"""

from backend.repository.github_loader import (
    GithubLoader
)

from backend.repository.repo_cloner import (
    RepoCloner
)

from backend.repository.repo_scanner import (
    RepoScanner
)

from backend.repository.repo_cleanup import (
    RepoCleanup
)


class RepositoryService:

    def __init__(self):

        self.loader = GithubLoader()
        self.cloner = RepoCloner()
        self.scanner = RepoScanner()
        self.cleanup = RepoCleanup()

    def load_repository(
        self,
        github_url: str
    ):

        repository = (
            self.loader.load(
                github_url
            )
        )

        repository = (
            self.cloner.clone(
                repository
            )
        )

        return repository

    def scan_repository(
        self,
        repository
    ):

        return (
            self.scanner.scan(
                repository
            )
        )

    def cleanup_repository(
        self,
        repository
    ):

        self.cleanup.cleanup(
            repository
        )