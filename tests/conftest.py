from pathlib import Path

import pytest


def pytest_configure(config):
    git_dir = Path(__file__).parent / "test_pkg" / ".git"
    gitignore = Path(__file__).parent / "test_pkg" / ".gitignore"

    if git_dir.exists():
        for child in git_dir.iterdir():
            child.unlink()
        git_dir.rmdir()

    if gitignore.exists():
        gitignore.unlink()


@pytest.fixture
def mock_git_dir():
    git_dir = Path(__file__).parent / "test_pkg" / ".git"
    git_dir.mkdir()

    tmp_file = git_dir / "tmp_file.py"
    tmp_file.write_text("print('INVALID')")

    yield git_dir
    for child in git_dir.iterdir():
        child.unlink()
    git_dir.rmdir()


@pytest.fixture
def mock_gitignore():
    content = """
    \r# TEST COMMENT
    \rvenv/
    """

    gitignore = Path(__file__).parent / "test_pkg" / ".gitignore"
    gitignore.write_text(content)

    yield gitignore
    gitignore.unlink()
