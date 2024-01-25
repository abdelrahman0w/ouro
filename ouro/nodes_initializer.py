import ast
from pathlib import Path
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

from ouro.reader import Reader


class Node:
    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name
        self.imports: List[
            Tuple["Node", bool, int]
        ] = []  # (node, is_from, lineno)
        self.defs: List[Tuple[int, int]] = []

    def add(self, item: "Node", is_from: bool, lineno: int) -> None:
        self.imports.append((item, is_from, lineno))


class NodesInitializer:
    def __init__(self, reader_obj: "Reader") -> None:
        self._prg_path = reader_obj.path
        self._prj = reader_obj.read
        self.nodes: Dict[str, "Node"] = {}

        self._initialize()

    def _get_node(self, file: str) -> "Node":
        if file not in self.nodes:
            self.nodes[file] = Node(file)

        return self.nodes[file]

    def _get_imports(
        self, content: str
    ) -> List[Union[ast.Import, ast.ImportFrom]]:
        return [
            node
            for node in ast.walk(ast.parse(content))
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom)
        ]

    def _get_defs(
        self, content: str
    ) -> List[Union[ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef]]:
        return [
            node
            for node in ast.walk(ast.parse(content))
            if isinstance(node, ast.FunctionDef)
            or isinstance(node, ast.AsyncFunctionDef)
            or isinstance(node, ast.ClassDef)
        ]

    def _get_module_path(
        self, node: Union[ast.ImportFrom, ast.Import]
    ) -> Union[Tuple[str, str], None]:
        if isinstance(node, ast.Import):
            if not node.names:
                return None

            path = Path(
                Path(self._prg_path) / Path(*(node.names[0].name.split(".")))
            ).with_suffix(".py")
            if not Path.exists(path):
                path = Path(
                    Path(self._prg_path).parent
                    / Path(*(node.names[0].name.split(".")))
                ).with_suffix(".py")

            return (str(path), str(path))
        elif isinstance(node, ast.ImportFrom):
            if not node.module:
                return None

            path_1 = Path(
                Path(self._prg_path) / Path(*(node.module.split(".")))
            ).with_suffix(".py")
            if not Path.exists(path_1):
                path_1 = Path(
                    Path(self._prg_path).parent
                    / Path(*(node.module.split(".")))
                ).with_suffix(".py")

            path_2 = Path(
                Path(self._prg_path)
                / Path(*(node.module.split(".")))
                / Path(node.names[0].name)
            ).with_suffix(".py")
            if not Path.exists(path_2):
                path_2 = Path(
                    Path(self._prg_path).parent
                    / Path(*(node.module.split(".")))
                    / Path(node.names[0].name)
                ).with_suffix(".py")

            return (str(path_1), str(path_2))

        return None

    def _initialize(self) -> None:
        for file, content in self._prj:
            node = self._get_node(file)
            node.defs = [
                (def_.lineno, def_.end_lineno)
                if def_.end_lineno
                else (def_.lineno, def_.lineno)
                for def_ in self._get_defs(content)
            ]

            imports = self._get_imports(content)
            for import_ in imports:
                imported_module_paths = self._get_module_path(import_)
                if imported_module_paths:
                    path_1, path_2 = imported_module_paths
                    imported_node_1 = self._get_node(path_1)
                    imported_node_2 = self._get_node(path_2)

                    if isinstance(import_, ast.ImportFrom):
                        node.add(imported_node_1, True, import_.lineno)
                        node.add(imported_node_2, True, import_.lineno)
                    else:
                        node.add(imported_node_1, False, import_.lineno)
                        node.add(imported_node_2, False, import_.lineno)
