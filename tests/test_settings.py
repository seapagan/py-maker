"""Tests for the Settings class.""" ""
import os
import tempfile
from pathlib import Path

import rtoml

from py_maker.config.settings import Settings


def test_settings():
    """Test that the Settings class works as expected."""
    test_author = "John Doe"
    # Create a temporary directory to store the settings file
    with tempfile.TemporaryDirectory() as tmpdir:
        # Set the settings folder to the temporary directory
        settings_folder = Path(tmpdir) / ".pymaker"
        os.makedirs(settings_folder)

        # Set the settings path to the temporary directory
        settings_path = settings_folder / "config.toml"

        # Create a new Settings object with the temporary settings path
        settings = Settings(settings_path=settings_path)

        # Test that the default settings are correct
        assert settings.schema_version == "1.0"
        assert settings.author_name == ""
        assert settings.author_email == ""
        assert settings.default_license == ""

        # Test that we can set and get a setting
        settings.set("author_name", test_author)
        assert settings.get("author_name") == test_author

        # Test that the settings are saved to the file
        settings.save()
        loaded_settings = rtoml.load(settings_path)
        assert loaded_settings["pymaker"]["author_name"] == test_author

        # Test that we can load the settings from the file
        settings2 = Settings(settings_path=settings_path)
        assert settings2.get("author_name") == test_author
