"""Control the settings of the project.

Allows reading from a settings file and writing to it.
"""
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

import rtoml
from rich import print  # pylint: disable=redefined-builtin

from py_maker.constants import license_names
from py_maker.helpers import get_author_and_email_from_git, show_table
from py_maker.prompt import Prompt


@dataclass
class Settings:
    """The main settings class."""

    ignore_list: List = field(
        default_factory=lambda: [
            "settings_folder",
            "settings_path",
            "ignore_list",
        ]
    )
    settings_folder: Path = Path.home() / ".pymaker"
    settings_path: Path = settings_folder / "config.toml"

    # define our settings
    schema_version: str = "1.0"
    author_name: str = ""
    author_email: str = ""
    default_license: str = ""

    def __post_init__(self):
        """Create the settings folder if it doesn't exist."""
        if not self.settings_folder.exists():
            self.settings_folder.mkdir(parents=True)
            self.get_user_settings(missing=True)

        self.load()

    def get_attrs(self) -> Dict[str, str]:
        """Return a dictionary of our setting values."""
        return {
            a: getattr(self, a)
            for a in dir(self)
            if not a.startswith("__")
            and a not in self.ignore_list
            and not callable(getattr(self, a))
        }

    def save(self) -> None:
        """Save the settings to the settings file."""
        rtoml.dump({"pymaker": self.get_attrs()}, self.settings_path)

    def load(self) -> None:
        """Load the settings from the settings file."""
        try:
            settings = rtoml.load(self.settings_path)
        except FileNotFoundError:
            self.save()
            return

        for key, value in settings["pymaker"].items():
            setattr(self, key, value)

    def get(self, key: str):
        """Get a setting by key."""
        try:
            return getattr(self, key)
        except AttributeError:
            return None

    def set(self, key: str, value, autosave: bool = True):
        """Set a setting by key and value.

        If autosave is True (the default), the settings will be saved to the
        settings file each time it is called.
        """
        setattr(self, key, value)
        if autosave:
            self.save()

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
        self.default_license = Prompt.ask(
            "Application License?",
            choices=license_names,
            default="MIT" if missing else self.default_license,
        )

        self.save()
        print("\n--> [green]Settings file saved.\n")

    def list_settings(self) -> Dict[str, str]:
        """Return a dictionary of settings."""
        return self.get_attrs()

    def change_settings(self) -> None:
        """Allow the user to change settings."""
        show_table(self.list_settings())

        print("\n--> [green]Enter new settings:\n")
        self.get_user_settings()

        self.save()
