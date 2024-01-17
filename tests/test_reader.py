import os

from ouroboros.reader import Reader


def test_reader():
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)),
    )

    with Reader(
        path=os.path.join(BASE_DIR, "tests", "test_pkg"),
        ignore=["ignore*"],
    ) as reader:
        files_lst, content_lst = zip(*reader)

    assert len(files_lst) == 4
    assert len(content_lst) == 4
    assert "INVALID" not in " ".join(content_lst)
