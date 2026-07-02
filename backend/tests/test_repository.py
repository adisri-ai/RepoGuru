"""
Repository tests.
"""

from backend.repository.github_loader import (
    GithubLoader
)


def test_valid_repository_url():

    loader = GithubLoader()

    repo = loader.load(
        "https://github.com/user/repo"
    )

    assert repo.owner == "user"
    assert repo.repo_name == "repo"


def test_invalid_repository_url():

    loader = GithubLoader()

    try:

        loader.load(
            "invalid-url"
        )

        assert False

    except ValueError:

        assert True