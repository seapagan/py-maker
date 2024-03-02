"""Helpers for the config module."""

from __future__ import annotations

import datetime
import re
import shutil
import sys
from importlib import metadata, resources
from pathlib import Path
from typing import TYPE_CHECKING, Union

import requests
import rtoml
from git.config import GitConfigParser
from rich import print  # pylint: disable=redefined-builtin
from rich.console import Console
from rich.table import Table

from py_maker.constants import ExitErrors

if TYPE_CHECKING:  # pragma: no cover
    from importlib.resources.abc import Traversable

SUCCESS_RESPONSE = 200


def get_author_and_email_from_git() -> tuple[str, str]:
    """Get the author name and email from git."""
    config = GitConfigParser()

    try:
        author_name = str(config.get_value("user", "name", ""))
    except KeyError:
        author_name = ""

    try:
        author_email = str(config.get_value("user", "email", ""))
    except KeyError:
        author_email = ""

    return author_name, author_email


def get_file_list(template_dir: Union[Traversable, Path]) -> list[Path]:
    """Return a list of files to be copied to the project directory.

    The root __init__.py file is excluded from the list, as it is only there so
    that the template directory can be treated as a package.
    """
    skip_dirs: list[str] = ["__pycache__"]

    file_list: list[Path] = [
        item.relative_to(str(template_dir))
        for item in template_dir.rglob("*")  # type: ignore
        if set(item.parts).isdisjoint(skip_dirs)
        and item.relative_to(str(template_dir)) != Path("__init__.py")
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
    return str(datetime.datetime.now(tz=datetime.timezone.utc).year)


def header() -> None:
    """Print a header for the application."""
    print("[bold]PyMaker[/bold] - Generate a Python project skeleton.\n")


def show_table(settings: dict[str, str]) -> None:
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
        if "token" not in key:
            table.add_row(pretty_attrib(key), str(value))
        else:
            table.add_row(pretty_attrib(key), "********")
    console.print(table)


def exists_on_pypi(package_name: str) -> bool:
    """Check if the package name is available on PyPI.

    Return True if the package name already exists on PyPI, False otherwise.
    Timeout after 5 seconds, which also returns False.
    """
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url, timeout=5)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        return False
    return response.status_code == SUCCESS_RESPONSE


def get_toml_path() -> Path:
    """Return the full path of the pyproject.toml.

    This only works during development mode, since the pyproject.toml will not
    exist when the application is installed as a package.
    """
    return Path(str(resources.files("py_maker"))) / ".." / "pyproject.toml"


def get_app_version() -> str:
    """Return the API version from the pyproject.toml file.

    We cannot however just find the file on the local file system, as the
    application will be installed as a package, in which case we need to use
    metadata from the package. We still check for the local file first, and only
    if it does not exist, we use the metadata - this allows us to test the
    application locally without installing it.
    """
    toml_path = get_toml_path()

    if toml_path.exists():
        # we are locally developing the package
        try:
            config = rtoml.load(toml_path)
            version: str = config["tool"]["poetry"]["version"]
        except (KeyError, OSError) as exc:
            print(f"Problem getting the Version : {exc}")
            sys.exit(ExitErrors.OS_ERROR)
        except rtoml.TomlParsingError as exc:
            print(f"Invalid 'pyproject.toml' file : {exc}")
            sys.exit(ExitErrors.TOML_ERROR)
        else:
            return version
    else:
        # if we are here then the package must be installed not local dev
        try:
            return metadata.version("pyproject_maker")
        except metadata.PackageNotFoundError as exc:
            print(f"Problem getting the Version : {exc}")
            sys.exit(ExitErrors.OS_ERROR)


def check_cmd_exists(cmd: str) -> bool:
    """Check if the supplied shell command exists."""
    return shutil.which(cmd) is not None
