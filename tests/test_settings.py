"""Tests for the Settings class."""
import tempfile
from pathlib import Path

import pytest
import rtoml

from py_maker.config.settings import Settings


@pytest.mark.skip(reason="Needs changing to new implementation")
def test_settings() -> None:
    """Test that the Settings class works as expected."""
    test_author = "John Doe"
    # Create a temporary directory to store the settings file
    with tempfile.TemporaryDirectory() as tmpdir:
        # Set the settings folder to the temporary directory
        settings_folder = Path(tmpdir) / ".pymaker"
        settings_folder.mkdir()

        # Set the settings path to the temporary directory
        settings_path = settings_folder / "config.toml"

        # Create a new Settings object with the temporary settings path
        settings = Settings(settings_file_name=settings_path)  # type: ignore

        # Test that the default settings are correct
        assert settings.schema_version == "none"
        assert settings.author_name == ""
        assert settings.author_email == ""
        assert settings.default_license == "None"

        # Test that we can set and get a setting
        settings.set("author_name", test_author)
        assert settings.get("author_name") == test_author

        # Test that the settings are saved to the file
        settings.save()
        loaded_settings = rtoml.load(settings_path)
        assert loaded_settings["pymaker"]["author_name"] == test_author

        # Test that we can load the settings from the file
        settings2 = Settings(settings_file_name=settings_path)  # type: ignore
        assert settings2.get("author_name") == test_author
