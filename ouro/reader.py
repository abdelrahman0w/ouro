import re
from pathlib import Path
from typing import Generator
from typing import List
from typing import Union

import pathspec


class Reader:
    _CHECKABLE: List[str] = [".py", ".pyi"]

    def __init__(
        self,
        path: str,
        ignore: Union[List[str], None] = None,
    ) -> None:
        self.path = Path(path)
        self._ignore = set(ignore) if ignore else set()
        self._ignore.add(r"\.git(?=[\/\\])")

    @property
    def _gitignore(self) -> Union[pathspec.PathSpec, None]:
        git_ignore = Path(self.path) / ".gitignore"

        if git_ignore.exists():
            gitignore_content = git_ignore.read_text().splitlines()
            gitignore_content = [
                line
                for line in gitignore_content
                if not line.startswith("#") and line.strip()
            ]

            return pathspec.PathSpec.from_lines(
                "gitwildmatch",
                gitignore_content,
            )

        return None

    def _is_ignored(self, file_path: Path) -> bool:
        if self._gitignore:
            return bool(self._gitignore.check_file(file_path).include) or any(
                re.search(ignored, str(file_path)) for ignored in self._ignore
            )
        else:
            return any(re.search(ignored, str(file_path)) for ignored in self._ignore)

    def _is_checkable(self, file_path: Path) -> bool:
        return Path(file_path).suffix in Reader._CHECKABLE

    def _read_file(self, file_path: Path) -> str:
        return Path(file_path).read_text()

    @property
    def _valid_files(self) -> Generator:
        for file in self.path.rglob("*"):
            if self._is_checkable(file) and not self._is_ignored(file):
                yield file

    @property
    def files(self) -> Generator:
        for file in self._valid_files:
            yield file, self._read_file(file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
