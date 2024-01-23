import ast
from collections import defaultdict
from pathlib import Path
from typing import Dict
from typing import List
from typing import Union

from ouro.reader import Reader


class Node:
    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name
        self._parent: Union["Node", None] = None
        self._imports: List["Node"] = []
        self._imported_from: Dict[str, List[int]] = defaultdict(list)

    def add(self, item: "Node") -> None:
        self._imports.append(item)


class ImportsGraph:
    def __init__(self, reader_obj: "Reader") -> None:
        self._prj = reader_obj.read
        self._nodes: Dict[str, "Node"] = {}

        self._parse()

    def _get_node(self, file: str) -> "Node":
        if file not in self._nodes:
            self._nodes[file] = Node(file)

        return self._nodes[file]

    def _get_imports(
        self, content: str
    ) -> List[Union[ast.Import, ast.ImportFrom]]:
        return [
            node
            for node in ast.walk(ast.parse(content))
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom)
        ]

    def _get_class_defs(self, content: str) -> List[ast.ClassDef]:
        return [
            node
            for node in ast.walk(ast.parse(content))
            if isinstance(node, ast.ClassDef)
        ]

    def _get_func_defs(self, content: str) -> List[ast.FunctionDef]:
        return [
            node
            for node in ast.walk(ast.parse(content))
            if isinstance(node, ast.FunctionDef)
        ]

    def _get_module_path(
        self, node: Union[ast.ImportFrom, ast.Import]
    ) -> Union[str, None]:
        if isinstance(node, ast.Import):
            return (
                f"{Path(*(node.names[0].name.split('.')))}.py"
                if node.names
                else None
            )
        elif isinstance(node, ast.ImportFrom):
            return (
                f"{Path(*(node.module.split('.')))}.py"
                if node.module
                else None
            )

        return None

    def _handle_import(
        self,
        importing_node: "Node",
        imported: Union[ast.ImportFrom, ast.Import],
    ) -> None:
        imported_module_path = self._get_module_path(imported)
        if imported_module_path:
            imported_node = self._get_node(imported_module_path)
            imported_node._imported_from[importing_node.name].append(
                imported.lineno
            )
            importing_node.add(imported_node)

    def _parse(self) -> None:
        for file, content in self._prj:
            node = self._get_node(file)
            imports = self._get_imports(content)

            for imp in imports:
                self._handle_import(node, imp)

    def __iter__(self):
        return iter(self._nodes.items())
