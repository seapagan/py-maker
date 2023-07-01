"""Create a new project."""
import sys
from pathlib import Path, PurePath
from typing import TypedDict

import typer
from rich import print  # plylint: disable=W0622
from rich.prompt import Confirm, Prompt

from py_maker.commands.helpers import (
    get_author_and_email_from_git,
    get_title,
    license_names,
)


class ValuesDict(TypedDict):
    """A typed dict for the values entered by the user."""

    project_dir: Path
    name: str
    author: str
    email: str
    license: str


app = typer.Typer()


def header() -> None:
    """Print a header for the application."""
    print("[bold]PyMaker[/bold] - Generate a Python project skeleton.\n")


def confirm_values(values: ValuesDict) -> bool:
    """Confirm the values entered by the user."""
    print(
        "\n[green][bold]Creating a New Python app with the below settings :\n"
    )

    padding: int = max([len(key) for key in values.keys()]) + 1

    for key, value in values.items():
        print(f"{key.title().rjust(padding)} : [green]{value}")

    return Confirm.ask("\nIs this correct?", default=True)


@app.callback(invoke_without_command=True)
def new(
    location: str = typer.Argument(..., help="Where to create the project.")
) -> None:
    """Create a new Python project."""
    header()

    values: ValuesDict = {
        "project_dir": Path(""),
        "name": "",
        "email": "",
        "author": "",
        "license": "",
    }

    values["project_dir"] = Path.cwd() / location

    print(f"[green]Creating a new project at[/green] {values['project_dir']}\n")

    git_author, git_email = get_author_and_email_from_git()

    values["name"] = Prompt.ask(
        "Name of the Application?",
        default=get_title(PurePath(values["project_dir"]).name),
    )
    values["author"] = Prompt.ask("Author Name?", default=git_author)

    values["email"] = Prompt.ask("Author Email?", default=git_email)
    values["license"] = Prompt.ask(
        "Application License?",
        choices=license_names,
        default="MIT",
        case_insensitive=True,
    )

    confirm = confirm_values(values)

    if not confirm:
        # User chose not to continue
        print("\n[red]Aborting![/red]")
        sys.exit(0)
