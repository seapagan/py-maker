"""Create a new project."""

from typing import Annotated, Optional, Union

import typer
from rich import print  # pylint: disable=W0622

from py_maker.config import get_settings
from py_maker.constants import ExitErrors
from py_maker.pymaker import PyMaker

app = typer.Typer(no_args_is_help=True)


@app.callback(invoke_without_command=True)
def new(
    location: Annotated[
        str,
        typer.Argument(
            ..., help="Where to create the project.", show_default=False
        ),
    ],
    accept_defaults: Annotated[
        bool, typer.Option("--yes", "-y", help="Accept all defaults.")
    ] = False,
    git: Annotated[
        Optional[bool],
        typer.Option(help="Initialize a git repository.", show_default=False),
    ] = None,
    test: Annotated[
        Optional[bool],
        typer.Option(help="Add testing libraries.", show_default=False),
    ] = None,
    lint: Annotated[
        Optional[bool],
        typer.Option(help="Add linting libraries.", show_default=False),
    ] = None,
    docs: Annotated[
        Optional[bool],
        typer.Option(help="Add the MkDocs boilerplate.", show_default=False),
    ] = None,
    standalone: Annotated[
        Optional[bool],
        typer.Option(
            "--standalone",
            "-s",
            help="Create a standalone project, not a package.",
            show_default=False,
        ),
    ] = False,
    bare: Annotated[
        Optional[bool],
        typer.Option(
            "--bare",
            "-b",
            help=(
                "Create a basic project, without any testing, "
                "docs, linting or Git repository."
            ),
            show_default=False,
        ),
    ] = False,
    github: Annotated[
        Optional[bool],
        typer.Option(
            help="Create a remote repository on GitHub for the project "
            "and push the initial commit.",
            show_default=False,
        ),
    ] = None,
) -> None:
    """Create a new Python project."""
    settings = get_settings()

    options: dict[str, Union[bool, None]] = {
        "git": settings.use_git if git is None else git,
        "test": settings.include_testing if test is None else test,
        "lint": settings.include_linters if lint is None else lint,
        "docs": settings.include_mkdocs if docs is None else docs,
        "github": settings.create_remote if github is None else github,
        "accept_defaults": accept_defaults,
        "standalone": standalone,
        "bare": bare,
    }

    if " " in location:
        print("\n[red]  --> The location cannot contain spaces, [b]Aborting.")
        raise typer.Exit(ExitErrors.LOCATION_ERROR)

    pymaker = PyMaker(location, options)

    pymaker.run()
