from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

from ouro.imports_graph import ImportsGraph
from ouro.nodes_initializer import Node
from ouro.nodes_initializer import NodesInitializer
from ouro.reader import Reader


class Checker:
    def __init__(
        self,
        path: str,
        ignore: Union[List[str], None] = None,
        categorize: bool = True,
    ):
        _reader = Reader(path, ignore)
        _nodes = NodesInitializer(_reader).nodes
        self.categorize = categorize
        self._imports_graph = ImportsGraph(list(_nodes.values()))
        self._cycles: Dict = {}

    def _handle_node_cycle_only(
        self,
        node: "Node",
        node_import: "Node",
        lineno: int,
        path: List["Node"],
        is_from: bool,
    ):
        if not self._cycles.get(node.name):
            self._cycles[node.name] = []

        in_def = any(
            def_begin <= lineno <= def_end for def_begin, def_end in node.defs
        )
        path_from_import_to_file = [node.name for node in path]

        self._cycles[node.name].append(
            {
                node_import.name: {
                    "lineno": lineno,
                    "in_def": in_def,
                    "is_from": is_from,
                },
                "path_from_import_to_file": path_from_import_to_file,
            }
        )

    def _handle_node_cycle_categorize(
        self,
        node: "Node",
        node_import: "Node",
        lineno: int,
        path: List["Node"],
        is_from: bool,
    ):
        if not self._cycles.get(node.name):
            self._cycles[node.name] = {
                "critical": [],
                "import_from_in_def": [],
                "direct_import": [],
                "direct_import_in_def": [],
            }

        in_def = any(
            def_begin <= lineno <= def_end for def_begin, def_end in node.defs
        )
        path_from_import_to_file = [node.name for node in path]
        categories_map = {
            "critical": (is_from and not in_def),
            "import_from_in_def": (is_from and in_def),
            "direct_import": (not is_from and not in_def),
            "direct_import_in_def": (not is_from and in_def),
        }

        for category, condition in categories_map.items():
            if condition:
                self._cycles[node.name][category].append(
                    {
                        node_import.name: {
                            "lineno": lineno,
                            "in_def": in_def,
                            "is_from": is_from,
                        },
                        "path_from_import_to_file": path_from_import_to_file,
                    }
                )

    def _check_node(
        self, node: "Node", node_imports: List[Tuple["Node", bool, int]]
    ) -> None:
        for node_import, is_from, lineno in node_imports:
            is_cyclic, path = self._imports_graph.is_reachable(
                node_import, node
            )

            if not is_cyclic:
                continue

            if self.categorize:
                self._handle_node_cycle_categorize(
                    node, node_import, lineno, path, is_from
                )
            else:
                self._handle_node_cycle_only(
                    node, node_import, lineno, path, is_from
                )

    def _check_all(self):
        for node, node_imports in self._imports_graph:
            self._check_node(node, node_imports)

    @property
    def cycles(self) -> Dict:
        self._check_all()
        return self._cycles

    def get_possible_origins(
        self, cycles: Dict, num_possibilities: int = 3
    ) -> List[str]:
        if self.categorize:
            cycle_iter = (
                cycle_info
                for cycle in cycles.values()
                for category in cycle.values()
                for cycle_info in category
            )
        else:
            cycle_iter = (
                cycle_info for cycle in cycles.values() for cycle_info in cycle
            )

        paths = [
            cycle_info["path_from_import_to_file"] for cycle_info in cycle_iter
        ]
        if not paths:
            return []

        counts = {}
        for path in paths:
            counts[path] = counts.get(path, 0) + 1

        sorted_paths = sorted(counts, key=counts.get, reverse=True)
        most_common_paths = sorted_paths[:num_possibilities]
        most_common_paths.reverse()

        possible_origins = []
        for path in most_common_paths:
            if path in cycles and any(
                path in cycle_info["path_from_import_to_file"]
                for cycle_info in cycle_iter
            ):
                possible_origins.append(path)

        return possible_origins
