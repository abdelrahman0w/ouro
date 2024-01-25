from pathlib import Path

from ouro.nodes_initializer import NodesInitializer
from ouro.reader import Reader


def test_nodes_initializer(mock_git_dir, mock_gitignore):
    test_pkg_dir = Path(__file__).resolve().parent / "test_pkg"

    nodes_initializer = NodesInitializer(Reader(test_pkg_dir))
    for _, node in nodes_initializer.nodes.items():
        if node.name.endswith("another_module.py"):
            imp_with_path_1, is_from, lineno = node.imports.pop()
            imp_with_path_2, is_from, lineno = node.imports.pop()
            assert any(
                imp.endswith("test_pkg/module.py")
                for imp in [imp_with_path_1.name, imp_with_path_2.name]
            )
            assert is_from is True
            assert lineno == 1
