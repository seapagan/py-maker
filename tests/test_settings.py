"""Test the settings module."""

import os
from collections.abc import Generator
from pathlib import Path
from typing import Any

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem, OSType
from pytest_mock import MockerFixture

from py_maker.config import Settings, get_settings


class TestSettings:
    """Test the settings module."""

    FAKE_TOML = """
[pymaker]
author_email = "testuser@testing.com"
author_name = "Test User"
github_token = "test_token"
"""

    CONFIG_FOLDER = ".pymaker"
    CONGIG_FILE = "config.toml"

    @pytest.fixture()
    def setting_file(self, fs: FakeFilesystem) -> FakeFilesystem:
        """Create a settings file."""
        config_dir = Path.home() / self.CONFIG_FOLDER
        fs.create_dir(config_dir)
        fs.create_file(
            str(config_dir / self.CONGIG_FILE),
            contents=self.FAKE_TOML,
        )
        return fs

    @pytest.fixture()
    def setting_file_windows(
        self, fs: FakeFilesystem, mocker
    ) -> Generator[FakeFilesystem, Any, None]:
        """Create a settings file."""
        fs.os = OSType.WINDOWS
        os.startfile = mocker.Mock()
        config_dir = Path.home() / self.CONFIG_FOLDER
        fs.create_dir(config_dir)
        fs.create_file(
            str(config_dir / self.CONGIG_FILE),
            contents=self.FAKE_TOML,
        )
        yield fs
        os.startfile = None

    @pytest.fixture()
    def setting_file_macos(
        self,
        fs: FakeFilesystem,
    ) -> FakeFilesystem:
        """Create a settings file."""
        fs.os = OSType.MACOS
        config_dir = Path.home() / self.CONFIG_FOLDER
        fs.create_dir(config_dir)
        fs.create_file(
            str(config_dir / self.CONGIG_FILE),
            contents=self.FAKE_TOML,
        )
        return fs

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

    def test_template_folder_set(self, setting_file: FakeFilesystem) -> None:
        """Test the template folder is set."""
        settings = get_settings()
        assert settings.template_folder == str(
            Path.home() / ".pymaker/template"
        )

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

    def test_edit_config_windows(
        self, mocker: MockerFixture, setting_file_windows: FakeFilesystem
    ) -> None:
        """Test the edit config function on windows."""
        assert setting_file_windows.is_windows_fs
        mocker.patch("platform.system", return_value="Windows")

        settings = Settings("pymaker")
        settings.edit_config()
        assert os.startfile.called

    def test_edit_config_macos(
        self, mocker: MockerFixture, setting_file_macos: FakeFilesystem
    ) -> None:
        """Test the edit config function on macos."""
        assert setting_file_macos.is_macos
        mocker.patch("platform.system", return_value="Darwin")
        mock_subprocess = mocker.patch("subprocess.call")
        settings = Settings("pymaker")
        settings.edit_config()

        mock_subprocess.assert_called_once_with(
            ["open", "/home/seapagan/.pymaker/config.toml"]
        )

    def test_edit_config_linux(
        self, mocker: MockerFixture, setting_file: FakeFilesystem
    ) -> None:
        """Test the edit config function on linux."""
