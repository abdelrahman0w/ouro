from pathlib import Path

from ouro.imports_graph import ImportsGraph
from ouro.reader import Reader


def test_imports_graph():
    test_pkg_dir = Path(__file__).resolve().parent / "test_pkg"

    graph = ImportsGraph(Reader(test_pkg_dir))
    for path, node in graph:
        if path.endswith("another_module.py"):
            assert node._imports[0].name == "test_pkg/module.py"
