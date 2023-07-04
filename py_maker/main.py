"""Main application entry point."""
import typer

from py_maker.commands import new

app = typer.Typer(
    pretty_exceptions_show_locals=False,
    add_completion=False,
    no_args_is_help=True,
    rich_markup_mode="rich",
)


app.add_typer(new.app, name="new")

if __name__ == "__main__":
    app()
