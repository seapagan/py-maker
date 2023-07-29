"""Control the settings of the project.

Allows reading from a settings file and writing to it.
"""
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

import rtoml

from py_maker.helpers import get_author_and_email_from_git
from py_maker.prompt import Prompt


@dataclass
class Settings:
    """The main settings class."""

    # settings file path
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
    user_name: str = ""
    user_email: str = ""
    default_license: str = ""

    def __post_init__(self):
        """Create the settings folder if it doesn't exist."""
        if not self.settings_folder.exists():
            self.settings_folder.mkdir(parents=True)
            self.settings_path.touch()

        self.load()

    def save(self):
        """Save the settings to the settings file."""
        attrs = {
            a: getattr(self, a)
            for a in dir(self)
            if not a.startswith("__")
            and a not in self.ignore_list
            and not callable(getattr(self, a))
        }
        rtoml.dump({"pymaker": attrs}, self.settings_path)

    def load(self):
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


def get_user_settings():
    """Ask the user for their settings and save to the settings file.

    We read the user's name and email from git, and use that as the default,
    letting them change it if they want.
    """
    git_author, git_email = get_author_and_email_from_git()
    default = Settings()

    default.user_name = Prompt.ask("Author Name?", default=git_author)
    default.user_email = Prompt.ask("Author Email?", default=git_email)
