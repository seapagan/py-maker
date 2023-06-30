"""Create a new project."""
import sys
from pathlib import Path

import typer
from rich import print  # plylint: disable=W0622
from rich.prompt import Confirm, Prompt

from py_maker.commands.helpers import (
    get_author_and_email_from_git,
    get_title,
    license_names,
)

app = typer.Typer()


def header():
    """Print a header for the application."""
    print("PyMaker - Generate a Python project skeleton.\n")


@app.callback(invoke_without_command=True)
def new(
    location: str = typer.Argument(..., help="Where to create the project.")
):
    """Create a new Python project."""
    header()
    local_cwd = Path.cwd() / location
    print(f"[green]Creating a new project at[/green] {local_cwd}\n")

    git_author, git_email = get_author_and_email_from_git()

    app_name = Prompt.ask(
        "Name of the Application?", default=get_title(location)
    )
    app_author = Prompt.ask("Author Name?", default=git_author)
    app_email = Prompt.ask("Author Email?", default=git_email)
    app_licence = Prompt.ask(
        "Application License?",
        choices=license_names,
        default="MIT",
    )

    print(
        "\n[green]You wish to create a New Python app with the below "
        "settings :[/green]\n"
    )
    print(f"Application Name    : [green]{app_name}")
    print(f"Application Author  : [green]{app_author}")
    print(f"Author Email        : [green]{app_email}")
    print(f"Application License : [green]{app_licence}")

    confirm = Confirm.ask("\nIs this correct?", default=True)

    if not confirm:
        # User chose not to continue
        print("\n[red]Aborting![/red]")
        sys.exit(0)
