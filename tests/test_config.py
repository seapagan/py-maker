"""Integration tests for the config command."""
from unittest.mock import patch

from typer.testing import CliRunner

from py_maker.commands.config import app


def test_show_config() -> None:
    """Test the show command."""
    runner = CliRunner()
    with patch("py_maker.config.settings.Settings.get_attrs") as mock_get_attrs:
        mock_get_attrs.return_value = {"key1": "value1", "key2": "value2"}
        result = runner.invoke(app, ["show"])
        assert result.exit_code == 0
        assert "Key1" in result.stdout
        assert "value1" in result.stdout
        assert "Key2" in result.stdout
        assert "value2" in result.stdout


def test_change_config() -> None:
    """Test the change command."""
    runner = CliRunner()
    with patch(
        "py_maker.config.settings.Settings.change_settings"
    ) as mock_change_settings:
        result = runner.invoke(app, ["change"])
        assert result.exit_code == 0
        mock_change_settings.assert_called_once()
