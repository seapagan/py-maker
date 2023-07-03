"""Create a new project."""
import typer

from py_maker.pymaker import PyMaker

app = typer.Typer()


@app.callback(invoke_without_command=True)
def new(
    location: str = typer.Argument(..., help="Where to create the project.")
) -> None:
    """Create a new Python project."""
    pymaker = PyMaker(location)

    pymaker.run()
