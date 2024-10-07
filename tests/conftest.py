"""Set up the test environment."""

import os
from collections.abc import Generator
from pathlib import Path
from typing import Any

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem, OSType


class CONSTANTS:
    """Define some constants for the tests."""

    FAKE_TOML = """
    [pymaker]
author_email = "testuser@testing.com"
author_name = "Test User"
github_token = "test_token"
"""
    CONFIG_FOLDER = ".pymaker"
    CONGIG_FILE = "config.toml"
    TEST_USER = "Test User"
    TEST_EMAIL = "testuser@testing.com"
    NEW_USER = "New User"
    NEW_EMAIL = "new_user@testuser.com"
    MOCK_ASK_PATH = "py_maker.config.settings.Prompt.ask"
    MOCK_PLATFORM_PATH = "platform.system"
    MOCK_SUBPROCESS_PATH = "subprocess.call"


@pytest.fixture
def fs_setup(fs) -> str:
    """A fixture to set up the fake file system before each test."""
    toml_content = """
[project]
name = "py_maker"
version = "1.2.3"
description = "A sample project"
authors = [{name='Author',email='author@example.com'}]
"""
    toml_path = "/fake/path/to/py_maker/pyproject.toml"
    fs.create_file(toml_path, contents=toml_content)
    return toml_path


@pytest.fixture
def setting_file(fs: FakeFilesystem) -> FakeFilesystem:
    """Create a settings file."""
    config_dir = Path.home() / CONSTANTS.CONFIG_FOLDER
    fs.create_dir(config_dir)
    fs.create_file(
        str(config_dir / CONSTANTS.CONGIG_FILE),
        contents=CONSTANTS.FAKE_TOML,
    )
    return fs


@pytest.fixture
def setting_file_windows(
    fs: FakeFilesystem, mocker
) -> Generator[FakeFilesystem, Any, None]:
    """Create a settings file."""
    fs.os = OSType.WINDOWS
    os.startfile = mocker.Mock()
    config_dir = Path.home() / CONSTANTS.CONFIG_FOLDER
    fs.create_dir(config_dir)
    fs.create_file(
        str(config_dir / CONSTANTS.CONGIG_FILE),
        contents=CONSTANTS.FAKE_TOML,
    )
    yield fs
    os.startfile = None


@pytest.fixture
def setting_file_macos(
    fs: FakeFilesystem,
) -> FakeFilesystem:
    """Create a settings file."""
    fs.os = OSType.MACOS
    config_dir = Path.home() / CONSTANTS.CONFIG_FOLDER
    fs.create_dir(config_dir)
    fs.create_file(
        str(config_dir / CONSTANTS.CONGIG_FILE),
        contents=CONSTANTS.FAKE_TOML,
    )
    return fs


@pytest.fixture
def setting_file_linux(
    fs: FakeFilesystem,
) -> FakeFilesystem:
    """Create a settings file."""
    fs.os = OSType.LINUX
    config_dir = Path.home() / CONSTANTS.CONFIG_FOLDER
    fs.create_dir(config_dir)
    fs.create_file(
        str(config_dir / CONSTANTS.CONGIG_FILE),
        contents=CONSTANTS.FAKE_TOML,
    )
    return fs
