"""Control the settings of the project.

Allows reading from a settings file and writing to it.
"""
import os
import platform
import subprocess  # nosec
from typing import List, Literal, Optional

from rich import print  # pylint: disable=redefined-builtin
from simple_toml_settings import TOMLSettings

from py_maker.constants import license_names
from py_maker.helpers import get_author_and_email_from_git, show_table
from py_maker.prompt import Prompt


class Settings(TOMLSettings):
    """The main settings class."""

    # define our settings
    # the schema_version is used to track changes to the settings file but will
    # be unused until we have a stable release. Expect the schema layout to
    # change at any time until then!
    author_name: str = ""
    author_email: str = ""
    github_username: Optional[str] = ""
    github_token: Optional[str] = ""
    github_protocol: Literal["ssh", "https"] = "ssh"
    default_license: str = "None"
    use_default_template: bool = True
    use_git: bool = True
    include_mkdocs: bool = True
    include_testing: bool = True
    include_linters: bool = True
    install_pre_commit: bool = True
    create_remote: bool = True

    # cant use Pathlike here as it breaks rtoml

    def __post_init__(self) -> None:
        """Set the settings file path."""
        super().__post_init__()
        self.template_folder: str = str(self.settings_folder / "template")

    def __post_create_file__(self):
        """Automatically called after the settings file is created.

        Here, we will ask the user for default settings.
        """
        print("here we are!!")
        self.get_user_settings(missing=True)

    def get_user_settings(self, missing: bool = False) -> None:
        """Ask the user for their settings and save to the settings file.

        We read the user's name and email from git, and use that as the default,
        letting them change it if they want.
        """
        git_author, git_email = get_author_and_email_from_git()

        if missing:
            print(
                "--> [green]Settings file is missing, creating now. "
                "Please confirm defaults:\n"
            )

        self.author_name = Prompt.ask(
            "Author Name?",
            default=git_author if missing else self.author_name,
        )
        self.author_email = Prompt.ask(
            "Author Email?",
            default=git_email if missing else self.author_email,
        )
        self.github_username = Prompt.ask(
            "Github Username? \[optional]",  # noqa W605 # type: ignore
            default="" if missing else self.github_username,
        )
        self.default_license = Prompt.ask(
            "Application License?",
            choices=license_names,
            default="MIT" if missing else self.default_license,
        )

        self.save()
        print("\n--> [green]Settings file saved.\n")

    def change_settings(self) -> None:
        """Allow the user to change settings."""
        show_table(self.list_settings())

        print("\n--> [green]Enter new settings:\n")
        self.get_user_settings()

        self.save()

    def change_token(self) -> None:
        """Allow the user to add a GitHub PAT."""
        print("--> [green]Enter a GitHub Personal Access Token:\n")
        self.github_token = Prompt.ask(
            "Github Token?",
            default=self.github_token,
        )

        self.save()

    def edit_config(self) -> None:
        """Open the default editor to edit the settings file."""
        if platform.system() == "Windows":  # Windows
            os.startfile(self.settings_file)  # type: ignore # nosec
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(
                ["open", self.settings_folder / self.settings_file_name]
            )  # nosec
        else:  # Linux
            # we will loop through a list of editors until we find one that
            # exists on the system.
            editor_list: List[str] = [
                "xdg-open",
                "sensible-editor",
                "nano",
                "vi",  # if all else fails 🤣
            ]
            for editor in editor_list:
                try:
                    subprocess.call(
                        [editor, self.settings_folder / self.settings_file_name]
                    )  # nosec
                    break
                except FileNotFoundError:
                    pass
            else:
                print(
                    "--> [red]No editor found. Please edit the settings file "
                    "manually.\n"
                )


settings = Settings("pymaker")
