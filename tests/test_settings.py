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

    @pytest.fixture()
    def setting_file_linux(
        self,
        fs: FakeFilesystem,
    ) -> FakeFilesystem:
        """Create a settings file."""
        fs.os = OSType.LINUX
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
            ["open", str(Path.home() / ".pymaker/config.toml")]
        )

    # ---------------------------- unfinished test --------------------------- #
    def test_edit_config_linux_first_match(
        self, mocker: MockerFixture, setting_file_linux: FakeFilesystem
    ) -> None:
        """Test the edit config function on linux."""
        assert setting_file_linux.is_linux
        mocker.patch("platform.system", return_value="Linux")
        mock_call = mocker.patch("subprocess.call")
        settings = Settings("pymaker")
        settings.edit_config()

        mock_call.assert_called_once_with(
            ["xdg-open", str(Path.home() / ".pymaker/config.toml")]
        )

    def test_edit_config_linux_third_match(
        self, mocker: MockerFixture, setting_file_linux: FakeFilesystem
    ) -> None:
        """Test the edit config function on linux."""
        call_count = [0]

        def side_effect(_) -> int:
            call_count[0] += 1
            if call_count[0] <= 2:  # noqa: PLR2004
                raise FileNotFoundError
            return 0

        assert setting_file_linux.is_linux
        mocker.patch("platform.system", return_value="Linux")
        mock_call = mocker.patch("subprocess.call", side_effect=side_effect)
        settings = Settings("pymaker")
        settings.edit_config()

        assert mock_call.call_count == 3  # noqa: PLR2004

    def test_edit_config_linux_no_editor(
        self, mocker: MockerFixture, setting_file_linux: FakeFilesystem, capsys
    ) -> None:
        """Test the edit config function on linux when editor not found."""
        assert setting_file_linux.is_linux
        mocker.patch("platform.system", return_value="Linux")
        mock_call = mocker.patch(
            "subprocess.call", side_effect=FileNotFoundError
        )
        settings = Settings("pymaker")
        settings.edit_config()

        output = capsys.readouterr().out

        call_args_expected = ["xdg-open", "sensible-editor", "nano", "vi"]
        call_args_processed = [
            call.args[0][0] for call in mock_call.call_args_list
        ]

        assert call_args_processed == call_args_expected
        assert mock_call.call_count == 4  # noqa: PLR2004
        assert (
            "No editor found. Please edit the settings file manually" in output
        )

    # -------------------------- end unfinished test ------------------------- #

    def test_change_token(
        self, setting_file: FakeFilesystem, mocker: MockerFixture
    ) -> None:
        """Test the change token function."""
        mock_ask = mocker.patch(
            "py_maker.config.settings.Prompt.ask", return_value="new_token"
        )
        settings = Settings("pymaker")
        settings.change_token()
        assert settings.github_token == "new_token"  # noqa: S105
        mock_ask.assert_called_once_with("Github Token?", default="test_token")

    def test_change_settings(
        self, setting_file: FakeFilesystem, mocker: MockerFixture, capsys
    ) -> None:
        """Test the change settings function."""
        mock_table = mocker.patch("py_maker.config.settings.show_table")
        mock_get_user_settings = mocker.patch(
            "py_maker.config.settings.Settings.get_user_settings"
        )
        settings = Settings("pymaker")
        settings_list = settings.list_settings()

        settings.change_settings()
        output = capsys.readouterr().out

        mock_table.assert_called_once_with(settings_list)
        mock_get_user_settings.assert_called_once()
        assert "Enter new settings:" in output

    def test_get_user_settings_file_exists(
        self, setting_file: FakeFilesystem, mocker: MockerFixture
    ) -> None:
        """Test the get user settings function."""
        mocker.patch(
            "py_maker.config.settings.get_author_and_email_from_git",
            return_value=("Test User", "testuser@testing.com"),
        )
        mocker.patch(
            "py_maker.config.settings.Prompt.ask",
            side_effect=["New User", "new_user@testuser.com", "newuser", "MIT"],
        )

        settings = Settings("pymaker")
        settings.get_user_settings(missing=False)

        assert settings.author_name == "New User"
        assert settings.author_email == "new_user@testuser.com"
        assert settings.github_username == "newuser"
        assert settings.default_license == "MIT"

    def test_get_user_settings_no_file_exists(
        self, fs: FakeFilesystem, mocker: MockerFixture, capsys
    ) -> None:
        """Test the get user settings function."""
        mocker.patch(
            "py_maker.config.settings.get_author_and_email_from_git",
            return_value=("Test User", "testuser@testing.com"),
        )
        mocker.patch(
            "py_maker.config.settings.Prompt.ask",
            side_effect=["New User", "new_user@testuser.com", "newuser", "MIT"],
        )
        # ensure the post_create_hook does nothing
        mocker.patch(
            "py_maker.config.settings.Settings.__post_create_hook__",
            return_value=None,
        )
        fs.create_dir(Path.home() / ".pymaker")

        settings = Settings("pymaker")
        settings.get_user_settings(missing=True)

        output = capsys.readouterr().out

        assert "Settings file is missing, creating now." in output

        assert settings.author_name == "New User"
        assert settings.author_email == "new_user@testuser.com"
        assert settings.github_username == "newuser"
        assert settings.default_license == "MIT"
