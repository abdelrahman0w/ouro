from pathlib import Path

import pytest


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
