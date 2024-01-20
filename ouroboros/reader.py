import os
import re
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
        self.path = path
        self._ignore = set(ignore) if ignore else set()

    @property
    def _gitignore(self) -> Union[pathspec.PathSpec, None]:
        git_ignore = os.path.join(self.path, ".gitignore")

        if os.path.exists(git_ignore):
            with open(git_ignore, "r") as file:
                gitignore_content = file.read().splitlines()
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

    def _is_ignored(self, path: str) -> bool:
        if self._gitignore:
            return bool(self._gitignore.check_file(path).include) or any(
                re.search(ignored, path) for ignored in self._ignore
            )
        else:
            return any(re.search(ignored, path) for ignored in self._ignore)

    def _is_checkable(self, file_name: str) -> bool:
        _, ext = os.path.splitext(file_name)
        return ext in Reader._CHECKABLE

    def _read_file(self, file_name: str) -> str:
        with open(file_name, "r") as readable:
            return readable.read()

    @property
    def _valid_files(self) -> Generator:
        for dir, _, files in os.walk(self.path):
            if self._is_ignored(dir):
                continue

            for file in files:
                file_path = os.path.join(dir, file)
                if self._is_checkable(file_path) and not self._is_ignored(file_path):
                    yield file_path

    @property
    def read(self) -> Generator:
        for file in self._valid_files:
            yield file, self._read_file(file)

    def __enter__(self):
        return self.read

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
