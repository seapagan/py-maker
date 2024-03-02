"""WIP Class to display a directory tree using Rich to the console.

Heavily influenced by the example in Rich.tree documentation.
"""

from __future__ import annotations

import os
import pathlib

from rich import print  # pylint: disable=redefined-builtin
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree


# create a subclass of pathlib.Path which has an extra method 'expand'. This
# method will expand environment variables and user home directory, and in all
# cases return an absolute path.
class Path(pathlib.Path):
    """Path class with additional methods."""

    _flavour = type(pathlib.Path())._flavour  # type: ignore[attr-defined] # noqa: SLF001

    def expand(self) -> Path:
        """Fully expand and resolve the Path given environment variables."""
        return Path(os.path.expandvars(self)).expanduser().resolve()


class FileTree:
    """Display a directory tree using Rich."""

    def __init__(self, directory: Path) -> None:
        """Initialize the FileTree class."""
        self.directory: Path = directory.expand()

        if not self.directory.is_dir():
            message = f"{self.directory} is not a directory."
            raise NotADirectoryError(message)

    def walk_directory(self, directory: Path, tree: Tree) -> None:
        """Recursively build a Tree with directory contents."""
        # Sort dirs first then by filename
        try:
            paths = sorted(
                directory.iterdir(),
                key=lambda path: (path.is_file(), path.name.lower()),
            )
        except PermissionError:
            # Skip directories that the user does not have permission to access
            return
        paths = sorted(
            Path(directory).iterdir(),
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
            f"{self.directory}",
            guide_style="bright_blue",
        )
        self.walk_directory(self.directory, tree)
        print(tree)
