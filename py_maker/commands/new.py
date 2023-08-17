"""Create a new project."""
import typer
from rich import print  # pylint: disable=W0622

from py_maker.constants import ExitErrors
from py_maker.pymaker import PyMaker

app = typer.Typer(no_args_is_help=True)


@app.callback(invoke_without_command=True)
def new(
    location: str = typer.Argument(..., help="Where to create the project."),
    no_git: bool = typer.Option(
        False, "--no-git", help="Don't Initialize a git repository."
    ),
    no_test: bool = typer.Option(
        False, "--no-test", help="Don't add testing libraries."
    ),
    no_lint: bool = typer.Option(
        False, "--no-lint", help="Don't add linting libraries."
    ),
) -> None:
    """Create a new Python project."""
    options = {
        "no_git": no_git,
        "no_test": no_test,
        "no_lint": no_lint,
    }

    if " " in location:
        print("\n[red]  --> The location cannot contain spaces, [b]Aborting.")
        raise typer.Exit(ExitErrors.LOCATION_ERROR)

    pymaker = PyMaker(location, options)

    pymaker.run()
