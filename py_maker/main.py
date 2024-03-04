"""Main application entry point."""

from typing import Optional

import typer
from rich import print  # pylint: disable=redefined-builtin

from py_maker.commands import config, new, template
from py_maker.helpers import get_app_version

app = typer.Typer(
    pretty_exceptions_show_locals=False,
    add_completion=False,
    no_args_is_help=True,
    rich_markup_mode="rich",
)


@app.callback(invoke_without_command=True)
def main(
    version: Optional[bool] = typer.Option(
        None, "-v", "--version", is_eager=True
    ),
) -> None:
    """Generate a Python project skeleton."""
    if version:
        print(
            "\n[green]PyMaker - Generate a Python project skeleton."
            f"\n[/green]Version: {get_app_version()}; "
            "\u00a9 Grant Ramsay 2023\n"
        )
        raise typer.Exit


app.add_typer(new.app, name="new", help="Create a new Python project.")
app.add_typer(
    config.app, name="config", help="Show or change the Configuration."
)
app.add_typer(
    template.app, name="template", help="Utilities for handling template files."
)


def run_app() -> None:
    """Run the main application.

    Breaking it out like this for testing.
    """
    app()


if __name__ == "__main__":
    run_app()
