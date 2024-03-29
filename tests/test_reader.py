from pathlib import Path

from ouro.reader import Reader


def test_reader(mock_git_dir, mock_gitignore):
    test_pkg_dir = Path(__file__).resolve().parent / "test_pkg"

    assert Path.exists(test_pkg_dir / ".gitignore")

    with Reader(path=test_pkg_dir, ignore=["ignore*"]) as reader:
        files_lst, content_lst = zip(*reader.files)

    assert len(files_lst) == 6
    assert len(content_lst) == 6
    assert "INVALID" not in " ".join(content_lst)
