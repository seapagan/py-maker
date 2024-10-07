"""Test suite for the helper functions."""

import datetime
from importlib import metadata
from pathlib import Path

import pytest
import requests

from py_maker.constants import ExitErrors
from py_maker.helpers import (
    check_cmd_exists,
    exists_on_pypi,
    get_app_version,
    get_author_and_email_from_git,
    get_current_year,
    get_file_list,
    get_title,
    header,
    pretty_attrib,
    sanitize,
    show_table,
)


def test_get_author_and_email_from_git(mocker) -> None:
    """Test getting the username and email from Git."""
    mocker.patch(
        "py_maker.helpers.GitConfigParser.get_value",
        side_effect=lambda _, key, __: {
            "name": "John Doe",
            "email": "john@example.com",
        }[key],
    )
    author, email = get_author_and_email_from_git()
    assert author == "John Doe"
    assert email == "john@example.com"


def test_get_author_and_email_from_git_no_config(mocker) -> None:
    """Test getting username and email from Git when no config found."""
    mocker.patch(
        "py_maker.helpers.GitConfigParser.get_value",
        side_effect=KeyError("Config not found"),
    )
    author, email = get_author_and_email_from_git()
    assert author == ""
    assert email == ""


def test_get_author_and_email_from_git_no_name(mocker) -> None:
    """Test getting username and email from Git when the username is missing."""

    # Mock get_value to return an email but raise KeyError for the name
    def get_value_mock(_, key, __) -> str:
        if key == "email":
            return "john@example.com"
        msg = f"{key} not found"
        raise KeyError(msg)

    mocker.patch(
        "py_maker.helpers.GitConfigParser.get_value", side_effect=get_value_mock
    )
    author, email = get_author_and_email_from_git()
    assert author == ""  # Expect default empty string
    assert email == "john@example.com"


def test_get_author_and_email_from_git_no_email(mocker) -> None:
    """Test getting username and email from Git when the email is missing."""

    # Mock get_value to return a name but raise KeyError for the email
    def get_value_mock(_, key, __) -> str:
        if key == "name":
            return "John Doe"
        msg = f"{key} not found"
        raise KeyError(msg)

    mocker.patch(
        "py_maker.helpers.GitConfigParser.get_value", side_effect=get_value_mock
    )
    author, email = get_author_and_email_from_git()
    assert author == "John Doe"
    assert email == ""  # Expect default empty string


def test_get_file_list(fs) -> None:
    """Test the 'get_file_list' helper."""
    fs.create_file("/template/__init__.py")
    fs.create_file("/template/module.py")
    file_list = get_file_list(Path("/template"))
    assert Path("module.py") in file_list
    assert Path("__init__.py") not in file_list


def test_exists_on_pypi_true(mocker) -> None:
    """Test the 'exists_on_pypi' helper."""
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200))
    assert exists_on_pypi("existing_package") is True


def test_exists_on_pypi_timeout(mocker) -> None:
    """Test the 'exists_on_pypi' giving a timeout."""
    mocker.patch("requests.get", side_effect=requests.exceptions.Timeout)
    assert exists_on_pypi("package") is False


def test_exists_on_pypi_network_error(mocker) -> None:
    """Test exists_on_pypi returns False on network error."""
    mocker.patch(
        "requests.get", side_effect=requests.exceptions.ConnectionError
    )
    assert not exists_on_pypi("some_package")


def test_exists_on_pypi_server_error(mocker) -> None:
    """Test the 'exists_on_pypi' function handles server error responses."""
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=500))
    assert exists_on_pypi("some_package") is False


def test_get_app_version_installed_package(mocker) -> None:
    """Test getting app version from installed package metadata."""
    mocker.patch("py_maker.helpers.metadata.version", return_value="1.0.1")
    mocker.patch("py_maker.helpers.Path.exists", return_value=False)
    assert get_app_version() == "1.0.1"


def test_get_app_version_local_dev(mocker, fs_setup) -> None:
    """Test get_app_version returns the correct version from pyproject.toml."""
    mocker.patch("py_maker.helpers.get_toml_path", return_value=Path(fs_setup))
    version = get_app_version()
    assert version == "1.2.3"


def test_get_app_version_error_handling(mocker, fs) -> None:  # noqa: ARG001
    """Test get_app_version exits with error when version cant be retrieved."""
    mocker.patch("py_maker.helpers.Path.exists", return_value=False)
    mocker.patch(
        "py_maker.helpers.metadata.version",
        side_effect=metadata.PackageNotFoundError("package not found"),
    )
    with pytest.raises(SystemExit) as exc_info:
        get_app_version()
    assert exc_info.value.code == ExitErrors.OS_ERROR


def test_get_app_version_key_error(mocker, fs) -> None:
    """Test get_app_version handles KeyError when version key is missing."""
    toml_content = """
[tool.poetry]
name = "py_maker"
description = "A sample project"
authors = ["Author <author@example.com>"]
    """
    fs.create_file(
        "/fake/path/to/py_maker/pyproject.toml", contents=toml_content
    )

    mocker.patch(
        "py_maker.helpers.get_toml_path",
        return_value=Path("/fake/path/to/py_maker/pyproject.toml"),
    )

    with pytest.raises(SystemExit) as e:
        get_app_version()
    assert e.value.code == ExitErrors.OS_ERROR


def test_get_app_version_os_error(mocker, fs) -> None:  # noqa: ARG001
    """Test get_app_version handles OSError with an issue reading the file."""
    mocker.patch(
        "py_maker.helpers.get_toml_path",
        return_value=Path("/fake/path/to/py_maker/pyproject.toml"),
    )

    mocker.patch("py_maker.helpers.rtoml.load", side_effect=OSError)

    with pytest.raises(SystemExit) as e:
        get_app_version()
    assert e.value.code == ExitErrors.OS_ERROR


def test_get_app_version_invalid_toml_format(mocker, fs) -> None:
    """Test get_app_version handles invalid TOML format gracefully."""
    # Setup an invalid TOML file content
    toml_content = "invalid TOML content"
    fs.create_file(
        "/fake/path/to/py_maker/pyproject.toml", contents=toml_content
    )

    # Mock get_toml_path to return the path of the created TOML file
    mocker.patch(
        "py_maker.helpers.get_toml_path",
        return_value=Path("/fake/path/to/py_maker/pyproject.toml"),
    )

    with pytest.raises(SystemExit) as e:
        get_app_version()
    assert e.value.code == ExitErrors.TOML_ERROR


def test_get_app_version_missing_tool_poetry_section(mocker, fs) -> None:
    """Test get_app_version handles missing 'tool.poetry' section."""
    # Setup a TOML file without the 'tool.poetry' section
    toml_content = """
[package]
name = "py_maker"
    """
    fs.create_file(
        "/fake/path/to/py_maker/pyproject.toml", contents=toml_content
    )

    # Mock get_toml_path to return the path of the created TOML file
    mocker.patch(
        "py_maker.helpers.get_toml_path",
        return_value=Path("/fake/path/to/py_maker/pyproject.toml"),
    )

    with pytest.raises(SystemExit) as e:
        get_app_version()
    assert e.value.code == ExitErrors.OS_ERROR


def test_sanitize_with_dash() -> None:
    """Test sanitize replaces dashes with underscores."""
    assert sanitize("test-name") == "test_name"


def test_sanitize_with_path() -> None:
    """Test sanitize works with Path objects containing dashes."""
    assert sanitize("/path/to/test-name") == "/path/to/test_name"


def test_get_title_with_dashes() -> None:
    """Test get_title replaces dashes and titlizes the string."""
    assert get_title("test-name") == "Test Name"


def test_get_title_with_underscore() -> None:
    """Test get_title replaces underscores and titlizes the string."""
    assert get_title("test_name") == "Test Name"


def test_get_title_with_dot() -> None:
    """Test get_title returns an empty string for a single dot."""
    assert get_title(".") == ""


def test_pretty_attrib() -> None:
    """Test pretty_attrib formats attribute names nicely."""
    assert pretty_attrib("test_name") == "Test Name"


def test_get_current_year() -> None:
    """Test get_current_year returns the current year as a string."""
    current_year = str(datetime.datetime.now(tz=datetime.timezone.utc).year)
    assert get_current_year() == current_year


def test_header(mocker) -> None:
    """Test header prints the correct header information."""
    mock_print = mocker.patch("py_maker.helpers.print")
    header()
    mock_print.assert_called_once_with(
        "[bold]PyMaker[/bold] - Generate a Python project skeleton.\n"
    )


def test_show_table(mocker) -> None:
    """Test show_table displays user data in a table format."""
    mock_console = mocker.patch("py_maker.helpers.Console")
    settings = {"name": "Test", "token": "secret"}
    show_table(settings)
    mock_console.return_value.print.assert_called_once()


def test_check_cmd_exists_true(mocker) -> None:
    """Test check_cmd_exists returns True when command exists."""
    mocker.patch("shutil.which", return_value="/path/to/git")
    assert check_cmd_exists("git") is True


def test_check_cmd_exists_false(mocker) -> None:
    """Test check_cmd_exists returns False when command does not exist."""
    mocker.patch("shutil.which", return_value=None)
    assert check_cmd_exists("nonexistent_cmd") is False
