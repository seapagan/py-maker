"""Helpers for the config module."""
from datetime import datetime
from typing import Dict

from git.config import GitConfigParser
from rich import print  # pylint: disable=redefined-builtin
from rich.console import Console
from rich.table import Table


def get_author_and_email_from_git() -> tuple[str, str]:
    """Get the author name and email from git."""
    config = GitConfigParser()

    return (
        str(config.get_value("user", "name", "")),
        str(config.get_value("user", "email", "")),
    )


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
        table.add_row(pretty_attrib(key), value)
    console.print(table)
