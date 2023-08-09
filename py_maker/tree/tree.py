"""WIP Class to display a directory tree using Rich to the console.

Heavily influenced by the example in Rich.tree documentation.
"""

import pathlib

from rich import print
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree


class FileTree:
    """Display a directory tree using Rich."""

    def __init__(self, directory: pathlib.Path) -> None:
        """Initialize the FileTree class."""
        self.directory = directory

    def walk_directory(self, directory: pathlib.Path, tree: Tree) -> None:
        """Recursively build a Tree with directory contents."""
        # Sort dirs first then by filename
        paths = sorted(
            pathlib.Path(directory).iterdir(),
            key=lambda path: (path.is_file(), path.name.lower()),
        )
        for path in paths:
            if path.is_dir():
                style = "dim" if path.name.startswith("__") else ""
                branch = tree.add(
                    f"[bold cyan]:open_file_folder: [link file://{path}]"
                    f"{escape(path.name)}",
                    style=style,
                    guide_style=style,
                )
                self.walk_directory(path, branch)
            else:
                text_filename = Text(path.name, "green")
                text_filename.stylize(f"link file://{path}")
                file_size = path.stat().st_size
                text_filename.append(f" ({decimal(file_size)})", "blue")
                icon = "🐍 " if path.suffix == ".py" else "📄 "
                tree.add(Text(icon) + text_filename)

    def show(self) -> None:
        """Print a directory tree to the console."""
        tree = Tree(
            f":open_file_folder: [link file://{self.directory}]"
            "{self.directory}",
            guide_style="bright_blue",
        )
        self.walk_directory(self.directory, tree)
        print(tree)
