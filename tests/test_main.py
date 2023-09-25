"""Test the main app loop."""
from typer.testing import CliRunner

from py_maker.main import app

runner = CliRunner()


def test_app() -> None:
    """Test the main app entry point."""
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "Usage" in result.stdout


def test_new() -> None:
    """Test the new command with no arguments shows help."""
    result = runner.invoke(app, ["new"])
    assert result.exit_code == 0
    assert "--help" in result.stdout
