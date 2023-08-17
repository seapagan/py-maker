"""Test the PyMaker class.

These tests are not complete.
"""
import shutil
from collections.abc import Iterator  # noqa: TC003
from pathlib import Path

import pytest

from py_maker.pymaker import PyMaker


@pytest.fixture()
def test_project_dir(tmp_path_factory) -> Iterator[Path]:
    """Create a temporary directory for testing."""
    project_dir: Path = tmp_path_factory.mktemp("test_project")
    yield project_dir
    shutil.rmtree(project_dir)


@pytest.fixture()
def test_pymaker(test_project_dir) -> PyMaker:
    """Create a PyMaker instance for testing."""
    pymaker = PyMaker(location="test_project", options={})
    pymaker.choices.name = "test_project"
    pymaker.choices.author = "Test Author"
    pymaker.choices.email = "test@example.com"
    pymaker.choices.license = "MIT"
    pymaker.choices.description = "A test project"
    pymaker.choices.project_dir = Path(test_project_dir) / "test_project"
    return pymaker


def test_create_folders(test_pymaker):
    """Test that the create_folders method creates the project directory."""
    test_pymaker.create_folders()
    assert test_pymaker.choices.project_dir.is_dir()


def test_copy_files(test_pymaker: PyMaker):
    """Test that the copy_files method copies the template files."""
    test_pymaker.create_folders()

    # TODO: Add assertions to test that the files were copied correctly
