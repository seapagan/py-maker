"""Test the config module."""
from typing import cast
from unittest.mock import MagicMock

import pytest
import typer.testing

from py_maker.commands import config

# Setup Typer CLI tester
cli_runner = typer.testing.CliRunner()


@pytest.fixture()
def mock_settings(mocker) -> MagicMock:
    """Fixture to mock the settings module."""
    return cast(MagicMock, mocker.patch("py_maker.commands.config.settings"))


@pytest.fixture()
def mock_header(mocker) -> MagicMock:
    """Fixture to mock the header function."""
    return cast(MagicMock, mocker.patch("py_maker.commands.config.header"))


@pytest.fixture()
def mock_show_table(mocker) -> MagicMock:
    """Fixture to mock the show_table function."""
    return cast(MagicMock, mocker.patch("py_maker.commands.config.show_table"))


def test_show(
    mock_settings: MagicMock, mock_header: MagicMock, mock_show_table: MagicMock
) -> None:
    """Test the `show` command."""
    result = cli_runner.invoke(config.app, ["show"])
    assert result.exit_code == 0
    mock_header.assert_called_once()
    mock_show_table.assert_called_once_with(
        mock_settings.get_attrs.return_value
    )


def test_change(mock_settings: MagicMock, mock_header: MagicMock) -> None:
    """Test the `change` command."""
    result = cli_runner.invoke(config.app, ["change"])
    assert result.exit_code == 0
    mock_header.assert_called_once()
    mock_settings.change_settings.assert_called_once()


def test_token(mock_settings: MagicMock, mock_header: MagicMock) -> None:
    """Test the `token` command."""
    result = cli_runner.invoke(config.app, ["token"])
    assert result.exit_code == 0
    mock_header.assert_called_once()
    mock_settings.change_token.assert_called_once()


def test_edit_config(mock_settings: MagicMock, mock_header: MagicMock) -> None:
    """Test the `edit` command."""
    result = cli_runner.invoke(config.app, ["edit"])
    assert result.exit_code == 0
    mock_header.assert_called_once()
    mock_settings.edit_config.assert_called_once()
