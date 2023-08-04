"""Main application entry point."""
import typer

from py_maker.commands import config, new, template

app = typer.Typer(
    pretty_exceptions_show_locals=False,
    add_completion=False,
    no_args_is_help=True,
    rich_markup_mode="rich",
)


app.add_typer(new.app, name="new", help="Create a new Python project.")
app.add_typer(
    config.app, name="config", help="Show or change the Configuration."
)
app.add_typer(
    template.app, name="template", help="Utilities for handling template files."
)

if __name__ == "__main__":
    app()
