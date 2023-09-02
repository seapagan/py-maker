"""Helpers for the config module."""
from __future__ import annotations

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, Union

import requests
import tomli
from git.config import GitConfigParser
from rich import print  # pylint: disable=redefined-builtin
from rich.console import Console
from rich.table import Table

from py_maker.constants import ExitErrors

if TYPE_CHECKING:  # pragma: no cover
    from importlib.resources.abc import Traversable


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
    return re.sub(r"[-_.]+", "_", str(input_str))


def get_title(key: str) -> str:
    """Get a 'titlized' version of the supplied string.

    This removes dashes or underscore and titlizes each word.
    """
    return re.sub(r"[-_.]+", " ", key).title() if key != "." else ""


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


def exists_on_pypi(package_name: str) -> bool:
    """Check if the package name is available on PyPI.

    Return True if the package name already exists on PyPI, False otherwise.
    Timeout after 5 seconds, which also returns False.
    """
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return False
    return response.status_code == 200


def get_toml_path() -> Path:
    """Return the full path of the pyproject.toml."""
    script_dir = Path(os.path.dirname(os.path.realpath(__name__)))

    return script_dir / "pyproject.toml"


def get_api_version() -> str:
    """Return the API version from the pyproject.toml file."""
    try:
        with get_toml_path().open("rb") as file:
            config = tomli.load(file)
            version = config["tool"]["poetry"]["version"]

            return version

    except (KeyError, OSError) as exc:
        print(f"Problem getting the Version : {exc}")
        sys.exit(ExitErrors.OS_ERROR)
