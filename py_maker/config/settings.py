"""Control the settings of the project.

Allows reading from a settings file and writing to it.
"""
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import List

import rtoml


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
        print(attrs)
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


@lru_cache()
def get_settings():
    """Get the settings.

    This is a read-only function that returns an instance of the settings class.
    """
    return Settings()
