"""Test the main file."""
import subprocess

import pytest
from typer.testing import CliRunner

from py_maker.main import app

runner = CliRunner()


@pytest.fixture()
def _mock_version(monkeypatch) -> None:
    """Fixture to mock get_app_version function."""
    monkeypatch.setattr("py_maker.main.get_app_version", lambda: "1.0.0")


@pytest.mark.usefixtures("_mock_version")
def test_version_option() -> None:
    """Test the --version option displays the correct version and exits."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "Version: 1.0.0" in result.stdout


def test_new_command() -> None:
    """Test the 'new' command is accessible and behaves as expected."""
    # Assuming 'new' command has a --help option that works
    result = runner.invoke(app, ["new", "--help"])
    assert result.exit_code == 0
    assert "Create a new Python project." in result.stdout


def test_config_command() -> None:
    """Test the 'config' command is accessible and behaves as expected."""
    # Assuming 'config' command has a --help option that works
    result = runner.invoke(app, ["config", "--help"])
    assert result.exit_code == 0
    assert "Show or change the Configuration." in result.stdout


def test_template_command() -> None:
    """Test the 'template' command is accessible and behaves as expected."""
    # Assuming 'template' command has a --help option that works
    result = runner.invoke(app, ["template", "--help"])
    assert result.exit_code == 0
    assert "Utilities for handling template files." in result.stdout


@pytest.mark.e2e()
def test_main_script_execution() -> None:
    """Test the main script execution simulates running the script directly."""
    command = ["python", "py_maker/main.py"]
    result = subprocess.run(
        command,  # noqa: S603
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Usage:" in result.stdout
    assert "Options" in result.stdout
    assert "Commands" in result.stdout

    assert result.stderr == ""
