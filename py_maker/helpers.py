"""Helpers for the config module."""
from __future__ import annotations

import re
from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Union

from git.config import GitConfigParser
from rich import print  # pylint: disable=redefined-builtin
from rich.console import Console
from rich.table import Table

if TYPE_CHECKING:  # pragma: no cover
    from importlib.resources.abc import Traversable
    from pathlib import Path


def get_author_and_email_from_git() -> tuple[str, str]:
    """Get the author name and email from git."""
    config = GitConfigParser()

    return (
        str(config.get_value("user", "name", "")),
        str(config.get_value("user", "email", "")),
    )


def get_file_list(template_dir: Union[Traversable, Path]):
    """Return a list of files to be copied to the project directory."""
    skip_dirs: List = ["__pycache__"]

    file_list: List[str] = [
        item.relative_to(template_dir)  # type: ignore
        for item in template_dir.rglob("*")  # type: ignore
        if set(item.parts).isdisjoint(skip_dirs)
    ]

    return file_list


def sanitize(input_str: Union[str, Path]) -> str:
    """Replace any dashes in the supplied string by underscores.

    Python needs underscores in library names, not dashes.
    """
    return str(input_str).replace("-", "_")


def get_title(key: str) -> str:
    """Get a 'titlized' version of the supplied string.

    This removes dashes or underscore and titlizes each word.
    """
    return re.sub("[_-]", " ", key).title() if key != "." else ""


def pretty_attrib(attr: str) -> str:
    """Return a pretty version of the attribute name."""
    return attr.replace("_", " ").title()


def get_current_year() -> str:
    """Get the current year."""
    return str(datetime.now().year)


def header() -> None:
    """Print a header for the application."""
    print("[bold]PyMaker[/bold] - Generate a Python project skeleton.\n")


def show_table(settings: Dict[str, str]):
    """Show User data in a tabulated format."""
    console = Console()
    table = Table(
        show_header=True,
        header_style="bold blue",
        title_style="bold cyan",
        title_justify="left",
    )
    table.add_column("Setting")
    table.add_column("Value")

    for key, value in settings.items():
        table.add_row(pretty_attrib(key), str(value))
    console.print(table)
