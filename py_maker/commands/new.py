"""Create a new project."""
import typer
from rich import print  # pylint: disable=W0622

from py_maker.config.settings import Settings
from py_maker.constants import ExitErrors
from py_maker.pymaker import PyMaker

app = typer.Typer(no_args_is_help=True)
settings = Settings()


@app.callback(invoke_without_command=True)
def new(
    location: str = typer.Argument(..., help="Where to create the project."),
    accept_defaults: bool = typer.Option(
        False, "--yes", "-y", help="Accept all defaults."
    ),
    no_git: bool = typer.Option(
        False, "--no-git", help="Don't Initialize a git repository."
    ),
    no_test: bool = typer.Option(
        False, "--no-test", help="Don't add testing libraries."
    ),
    no_lint: bool = typer.Option(
        False, "--no-lint", help="Don't add linting libraries."
    ),
    no_docs: bool = typer.Option(
        False, "--no-docs", help="Don't add the MkDocs boilerplate."
    ),
) -> None:
    """Create a new Python project."""
    options = {
        "no_git": no_git or not settings.use_git,
        "no_test": no_test or not settings.include_testing,
        "no_lint": no_lint or not settings.include_linters,
        "no_docs": no_docs or not settings.include_mkdocs,
        "accept_defaults": accept_defaults,
    }

    if " " in location:
        print("\n[red]  --> The location cannot contain spaces, [b]Aborting.")
        raise typer.Exit(ExitErrors.LOCATION_ERROR)

    pymaker = PyMaker(location, options)

    pymaker.run()
