"""Class to encapsulate the application."""
import re
import sys
from pathlib import Path, PurePath

from git.config import GitConfigParser
from rich import print
from rich.prompt import Confirm, Prompt

from py_maker.constants import license_names
from py_maker.schema import ProjectSettings, ProjectValues


class PyMaker:
    """PyMaker class."""

    def __init__(self, location: str) -> None:
        """Initialize the PyMaker class."""
        self.choices: ProjectValues = ProjectValues()
        self.location: str = location

        if len(Path(self.location).parts) > 1:
            self.header()
            print(
                "[red]  -> Error: Location must be a single directory name.\n"
            )
            sys.exit(1)

    def confirm_values(self) -> bool:
        """Confirm the values entered by the user."""
        print(
            "\n[green][bold]Creating a New Python app with the below "
            "settings :\n"
        )

        padding: int = max([len(key) for key, _ in self.choices]) + 3

        for key, value in self.choices:
            print(f"{self.get_title(key).rjust(padding)} : [green]{value}")

        return Confirm.ask("\nIs this correct?", default=True)

    def get_title(self, key: str) -> str:
        """Get the title for the application."""
        return re.sub("[_-]", " ", key).title() if key != "." else ""

    @staticmethod
    def header() -> None:
        """Print a header for the application."""
        print("[bold]PyMaker[/bold] - Generate a Python project skeleton.\n")

    @staticmethod
    def get_author_and_email_from_git() -> tuple[str, str]:
        """Get the author name and email from git."""
        config = GitConfigParser()

        return (
            str(config.get_value("user", "name", None)),
            str(config.get_value("user", "email", None)),
        )

    # ------------------------------------------------------------------------ #
    #             The main application loop is on the .run()method.            #
    # ------------------------------------------------------------------------ #
    def run(self) -> None:
        """The main entry point for the application."""
        self.header()

        self.choices.project_dir = Path.cwd() / self.location

        print(
            "[green]Creating a new project at[/green] "
            f"{self.choices.project_dir}\n"
        )

        git_author, git_email = self.get_author_and_email_from_git()

        self.choices.name = Prompt.ask(
            "Name of the Application?",
            default=self.get_title(PurePath(self.choices.project_dir).name),
        )
        self.choices.author = Prompt.ask("Author Name?", default=git_author)

        self.choices.email = Prompt.ask("Author Email?", default=git_email)
        self.choices.license = Prompt.ask(
            "Application License?",
            choices=license_names,
            default="MIT",
            case_insensitive=True,
        )

        if not self.confirm_values():
            # User chose not to continue
            print("\n[red]Aborting![/red]")
            sys.exit(0)

        # print(self.choices.model_dump_json(indent=2))

        # settings: ProjectSettings = ProjectSettings(**self.choices.model_dump())
        # print(settings.model_dump_json(indent=2))
