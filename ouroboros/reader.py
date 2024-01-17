import os
import re
from typing import Generator
from typing import List


class Reader:
    _CHECKABLE: List[str] = [".py", ".pyi"]

    def __init__(self, path: str, ignore: List[str] | None = None) -> None:
        self.path = path
        self.ignore = set(ignore) if ignore else set()

    def _is_ignored(self, path: str) -> bool:
        return any(re.search(ignored, path) for ignored in self.ignore)

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
                if self._is_checkable(file) and not self._is_ignored(file):
                    yield os.path.join(dir, file)

    @property
    def read(self) -> Generator:
        for file in self._valid_files:
            yield file, self._read_file(file)

    def __enter__(self):
        return self.read

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
