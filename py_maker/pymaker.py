"""Class to encapsulate the application."""
import importlib.resources as pkg_resources
import os
import re
import sys
from pathlib import Path, PurePath

from git.config import GitConfigParser
from jinja2 import Environment, FileSystemLoader
from rich import print
from rich.prompt import Confirm, Prompt

from py_maker import template
from py_maker.constants import (
    dynamic_file_list,
    license_names,
    new_dir_list,
    static_file_list,
)
from py_maker.schema import ProjectValues


class PyMaker:
    """PyMaker class."""

    def __init__(self, location: str) -> None:
        """Initialize the PyMaker class."""
        self.choices: ProjectValues = ProjectValues()
        self.location: str = location

        self.header()

        if len(Path(self.location).parts) > 1:
            print(
                "[red]  -> Error: Location must be a single directory name, "
                "and is relative to the current direcotry.\n"
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
    #                   create the project skeleton folders.                   #
    # ------------------------------------------------------------------------ #
    def create_folders(self) -> None:
        """Create the folders for the project."""
        try:
            os.mkdir(self.choices.project_dir)
            for new_dir in new_dir_list:
                os.mkdir(self.choices.project_dir / new_dir)
        except FileExistsError:
            print(
                f"\n[red]  -> Error: Directory '{self.choices.project_dir}' "
                "already exists.\n"
            )
            sys.exit(2)
        except PermissionError:
            print(
                "\n[red]  -> Error: Permission denied creating directory "
                f"'{self.choices.project_dir}'\n"
            )
            sys.exit(3)

    # ------------------------------------------------------------------------ #
    #             Copy the template files to the project directory.            #
    # ------------------------------------------------------------------------ #
    def copy_template_files(self) -> None:
        """Copy the template files to the project directory."""
        template_dir = pkg_resources.files(template)

        # ------------------- copy the static files first. ------------------- #
        for file in static_file_list:
            with pkg_resources.as_file(template_dir / "static" / file) as src:
                dst = Path(self.choices.project_dir) / file
                dst.write_text(src.read_text())

        # ------------------ generate the license file next. ----------------- #
        license_env = Environment(
            loader=FileSystemLoader(str(template_dir / "licenses"))
        )
        license_template = license_env.get_template(
            f"{self.choices.license}.jinja"
        )
        dst = Path(self.choices.project_dir) / "LICENSE.txt"
        dst.write_text(
            license_template.render(author=self.choices.author, year="2021")
        )

        # ------------------ now generate the dynamic files. ----------------- #
        dynamic_env = Environment(
            loader=FileSystemLoader(str(template_dir / "dynamic"))
        )
        for file in dynamic_file_list:
            template_file = dynamic_env.get_template(file)
            dst = Path(self.choices.project_dir) / Path(file).with_suffix("")
            dst.write_text(
                template_file.render(
                    self.choices.model_dump(), slug=self.location
                )
            )

        # ----------------- finally populate the app folder. ----------------- #
        for file in ["main.py", "__init__.py"]:
            with pkg_resources.as_file(template_dir / "app" / file) as src:
                dst = Path(self.choices.project_dir) / "app" / file
                dst.write_text(src.read_text())

    # ------------------------------------------------------------------------ #
    #             The main application loop is on the .run()method.            #
    # ------------------------------------------------------------------------ #
    def run(self) -> None:
        """The main entry point for the application."""
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
        self.choices.description = Prompt.ask(
            "Description of the Application?",
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

        self.create_folders()
        self.copy_template_files()
