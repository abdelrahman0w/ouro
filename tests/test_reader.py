from pathlib import Path

from ouroboros.reader import Reader


def test_reader(mock_git_dir, mock_gitignore):
    test_pkg_dir = Path(__file__).resolve().parent / "test_pkg"

    assert Path.exists(test_pkg_dir / ".gitignore")

    with Reader(path=test_pkg_dir, ignore=["ignore*"]) as reader:
        files_lst, content_lst = zip(*reader)

    assert len(files_lst) == 4
    assert len(content_lst) == 4
    assert "INVALID" not in " ".join(content_lst)
