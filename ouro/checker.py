from typing import Dict
from typing import List
from typing import Tuple

from ouro.imports_graph import ImportsGraph
from ouro.nodes_initializer import Node
from ouro.nodes_initializer import NodesInitializer
from ouro.reader import Reader


class Checker:
    def __init__(self, path: str) -> None:
        _reader = Reader(path)
        _nodes = NodesInitializer(_reader).nodes
        self._imports_graph = ImportsGraph(list(_nodes.values()))
        self._cycles: Dict = {}

    def _check_node(
        self, node: "Node", node_imports: List[Tuple["Node", bool, int]]
    ) -> None:
        for node_import, is_from, lineno in node_imports:
            is_cyclic, path = self._imports_graph.is_reachable(
                node_import, node
            )
            if is_cyclic:
                if not self._cycles.get(node.name):
                    self._cycles[node.name] = []

                self._cycles[node.name].append(
                    {
                        node_import.name: {
                            "lineno": lineno,
                            "in_def": any(
                                [
                                    def_begin <= lineno <= def_end
                                    for def_begin, def_end in node.defs
                                ]
                            ),
                            "is_from": is_from,
                        },
                        "path_from_import_to_file": [
                            node.name for node in path
                        ],
                    }
                )

    def _check_all(self):
        for node, node_imports in self._imports_graph:
            self._check_node(node, node_imports)

    @property
    def cycles(self) -> Dict:
        self._check_all()
        return self._cycles

    @staticmethod
    def get_possible_origin(cycles: Dict, num_origins: int = 3) -> List[str]:
        paths = []
        for cycle in cycles.values():
            for cycle_info in cycle:
                paths.extend(cycle_info["path_from_import_to_file"])

        if not paths:
            return []

        counts = {}
        for path in paths:
            counts[path] = counts.get(path, 0) + 1

        sorted_paths = sorted(counts, key=counts.get, reverse=True)
        most_common_paths = sorted_paths[:num_origins]
        most_common_paths.reverse()

        possible_origins = []
        for path in most_common_paths:
            if path in cycles and any(
                path in cycle_info["path_from_import_to_file"]
                for cycle in cycles.values()
                for cycle_info in cycle
            ):
                possible_origins.append(path)

        return possible_origins
