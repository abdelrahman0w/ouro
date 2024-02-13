import ast
from pathlib import Path
from typing import Dict
from typing import List
from typing import Set
from typing import Tuple
from typing import Union

from ouro.reader import Reader


class Node:
    def __init__(
        self,
        file_path: Path,
    ) -> None:
        self.file_path = file_path
        self.imports: Set[Tuple["Node", bool, int]] = set()  # (node, is_from, lineno)
        self.defs: Set[Tuple[int, int]] = set()  # (lineno, end_lineno)


class NodesInitializer:
    def __init__(self, path: str, ignore: Union[List[str], None] = None) -> None:
        self.nodes: Dict[Path, "Node"] = {}

        with Reader(path, ignore=ignore) as reader_obj:
            self._files = reader_obj.files
            self._prg_path = reader_obj.path

        self._initialize()

    def _get_node(self, file_path: Path) -> "Node":
        if file_path not in self.nodes:
            self.nodes[file_path] = Node(file_path)

        return self.nodes[file_path]

    def _get_imports(
        self, file_content: str
    ) -> List[Union[ast.Import, ast.ImportFrom]]:
        return [
            node
            for node in ast.walk(ast.parse(file_content))
            if isinstance(node, (ast.Import, ast.ImportFrom))
        ]

    def _get_defs(
        self, content: str
    ) -> List[Union[ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef]]:
        return [
            node
            for node in ast.walk(ast.parse(content))
            if isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                ),
            )
        ]

    def _module_path_from_parent(
        self, node: Union[ast.ImportFrom, ast.Import]
    ) -> Union[Path, None]:
        if isinstance(node, ast.Import):
            if not node.names:
                return None

            module_path = self._prg_path.parent / Path(
                *(node.names[0].name.split("."))
            ).with_suffix(".py")
        elif isinstance(node, ast.ImportFrom):
            if not node.module:
                return None

            path_1 = self._prg_path.parent / Path(
                *(node.module.split("."))
            ).with_suffix(".py")
            path_2 = (
                self._prg_path.parent
                / Path(*(node.module.split(".")))
                / Path(node.names[0].name).with_suffix(".py")
            )
            module_path = path_1 if path_1 and path_1.is_file() else path_2

        return module_path if module_path and module_path.is_file() else None

    def _get_module_path(
        self, node: Union[ast.ImportFrom, ast.Import]
    ) -> Union[Path, None]:
        if isinstance(node, ast.Import):
            if not node.names:
                return None

            module_path = self._prg_path / Path(
                *(node.names[0].name.split("."))
            ).with_suffix(".py")
        elif isinstance(node, ast.ImportFrom):
            if not node.module:
                return None

            path_1 = self._prg_path / Path(*(node.module.split("."))).with_suffix(".py")
            path_2 = (
                self._prg_path
                / Path(*(node.module.split(".")))
                / Path(node.names[0].name).with_suffix(".py")
            )
            module_path = path_1 if path_1 and path_1.is_file() else path_2

        return module_path if module_path and module_path.is_file() else None

    def _initialize(self) -> None:
        for file_path, content in self._files:
            node = self._get_node(file_path)
            imports = self._get_imports(content)
            defs = self._get_defs(content)

            for def_ in defs:
                node.defs.add(
                    (def_.lineno, def_.end_lineno)
                    if def_.end_lineno
                    else (def_.lineno, def_.lineno)
                )

            for import_module in imports:
                if imported_module_path := self._get_module_path(
                    import_module
                ) or self._module_path_from_parent(import_module):
                    imported_node = self._get_node(imported_module_path)

                    if isinstance(import_module, ast.ImportFrom):
                        node.imports.add((imported_node, True, import_module.lineno))
                    else:
                        node.imports.add((imported_node, False, import_module.lineno))
