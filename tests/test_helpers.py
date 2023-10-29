"""Test the helpers module."""
from __future__ import annotations

from typing import TYPE_CHECKING

import requests

from py_maker.helpers import (
    exists_on_pypi,
    get_author_and_email_from_git,
    get_current_year,
    get_title,
    pretty_attrib,
    sanitize,
)

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def test_get_author_and_email_from_git() -> None:
    """Test the get_author_and_email_from_git function."""
    author, email = get_author_and_email_from_git()
    assert isinstance(author, str)
    assert isinstance(email, str)


def test_sanitize() -> None:
    """Test the Sanitize function."""
    assert sanitize("my-project-name") == "my_project_name"
    assert sanitize("my-project-name-1.0") == "my_project_name_1_0"
    assert sanitize("my_project_name") == "my_project_name"
    assert sanitize("my_____project_name....end") == "my_project_name_end"


def test_get_title() -> None:
    """Test the get_title function."""
    assert get_title("my-project-name") == "My Project Name"
    assert get_title("my_project_name") == "My Project Name"
    assert get_title(".") == ""


def test_pretty_attrib() -> None:
    """Test the pretty_attrib function."""
    assert pretty_attrib("my_attribute_name") == "My Attribute Name"
    assert pretty_attrib("MY_ATTRIBUTE_NAME") == "My Attribute Name"


def test_get_current_year() -> None:
    """Test the get_current_year function."""
    assert get_current_year().isdigit()
    assert len(get_current_year()) == 4  # noqa: PLR2004


def test_exists_on_pypi_returns_true(mocker: MockerFixture) -> None:
    """Test the exists_on_pypi function - exists."""
    mock_get = mocker.patch.object(requests, "get")
    mock_get.return_value.status_code = 200
    assert exists_on_pypi("requests") is True


def test_exists_on_pypi_returns_false(mocker: MockerFixture) -> None:
    """Test the exists_on_pypi function - does not exist."""
    mock_get = mocker.patch.object(requests, "get")
    mock_get.return_value.status_code = 404
    assert exists_on_pypi("nonexistent_package") is False


def test_exists_on_pypi_returns_false_on_timeout(mocker: MockerFixture) -> None:
    """Test the exists_on_pypi function - timeout."""
    mock_get = mocker.patch.object(requests, "get")
    mock_get.side_effect = requests.exceptions.Timeout
    assert exists_on_pypi("nonexistent_package") is False
