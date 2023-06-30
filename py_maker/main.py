"""Main application entry point."""
import typer

app = typer.Typer(
    pretty_exceptions_show_locals=False,
    add_completion=False,
    no_args_is_help=True,
)


@app.command()
def main():
    """Main application entry point."""
    typer.echo("Hello World!")


if __name__ == "__main__":
    app()
