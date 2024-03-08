"""Test the settings module."""

from pathlib import Path

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem
from pytest_mock import MockerFixture

from py_maker.config import Settings, get_settings

FAKE_TOML = """
[pymaker]
author_email = "testuser@testing.com"
author_name = "Test User"
"""


@pytest.fixture()
def setting_file(fs: FakeFilesystem) -> FakeFilesystem:
    """Create a settings file."""
    config_dir = Path.home() / ".pymaker"
    fs.create_dir(config_dir)
    fs.create_file(
        str(config_dir / "config.toml"),
        contents=FAKE_TOML,
    )
    return fs


class TestSettings:
    """Test the settings module."""

    def test_settings(self, setting_file: FakeFilesystem) -> None:
        """Test the settings module creates properly."""
        settings = get_settings()
        assert settings.author_email == "testuser@testing.com"
        assert settings.author_name == "Test User"

        assert isinstance(settings, Settings)

    def test_settings_singleton(self, setting_file: FakeFilesystem) -> None:
        """Test the settings is a singleton."""
        settings = get_settings()
        settings2 = get_settings()
        assert settings is settings2

    def test_post_create_hook(
        self, fs: FakeFilesystem, mocker: MockerFixture
    ) -> None:
        """Test the post create hook."""
        mock_get_settings = mocker.patch(
            "py_maker.config.Settings.get_user_settings"
        )
        fs.create_dir(Path.home())
        _ = Settings("pymaker")

        assert mock_get_settings.called
