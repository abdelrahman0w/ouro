# from pathlib import Path
# from ouro.imports_graph import ImportsGraph
# from ouro.nodes_initializer import NodesInitializer
# from ouro.reader import Reader
# def test_nodes_initializer(mock_git_dir, mock_gitignore):
#     test_pkg_dir = Path(__file__).resolve().parent / "test_pkg"
#     nodes = NodesInitializer(Reader(test_pkg_dir)).nodes
#     graph = ImportsGraph(list(nodes.values())).graph
