from typing import Dict
from typing import List
from typing import Tuple

from ouro.nodes_initializer import Node


class ImportsGraph:
    def __init__(self, nodes: List["Node"]) -> None:
        self.nodes = nodes
        self.num_nodes = len(nodes)
        self.graph: Dict["Node", List[Tuple["Node", bool, int]]] = {
            node: [
                (node_import, is_from, lineno)
                for node_import, is_from, lineno in node.imports
                if node_import in nodes
            ]
            for node in self.nodes
        }

    def is_reachable(
        self, source: "Node", destination: "Node"
    ) -> Tuple[bool, List["Node"]]:
        visited = {node: False for node in self.nodes}
        queue = [source]
        visited[source] = True
        path: Dict["Node", "Node"] = {}

        while queue:
            current_node = queue.pop(0)

            if current_node == destination:
                return True, self.find_path(source, destination, path)

            for node_import, _, _ in self.graph[current_node]:
                if not visited[node_import]:
                    queue.append(node_import)
                    visited[node_import] = True
                    path[node_import] = current_node

        return False, []

    def find_path(
        self, source: "Node", destination: "Node", path: Dict["Node", "Node"]
    ) -> List["Node"]:
        node = destination
        path_list = [node]

        while node != source:
            node = path[node]
            path_list.append(node)

        path_list.reverse()
        return path_list

    def __iter__(self):
        return iter(self.graph.items())
