"""Test the PyMaker class.

These tests are not complete.
"""
import shutil
from collections.abc import Iterator
from pathlib import Path

import pytest

from py_maker.pymaker import PyMaker


@pytest.fixture()
def test_project_dir(
    tmp_path_factory: pytest.TempPathFactory,
) -> Iterator[Path]:
    """Create a temporary directory for testing."""
    project_dir: Path = tmp_path_factory.mktemp("test_project")
    yield project_dir
    shutil.rmtree(project_dir)


@pytest.fixture()
def test_pymaker(test_project_dir: pytest.TempPathFactory) -> PyMaker:
    """Create a PyMaker instance for testing."""
    pymaker = PyMaker(location="test_project", options={})
    pymaker.choices.name = "test_project"
    pymaker.choices.author = "Test Author"
    pymaker.choices.email = "test@example.com"
    pymaker.choices.license_name = "MIT"
    pymaker.choices.description = "A test project"
    pymaker.choices.project_dir = Path(str(test_project_dir)) / "test_project"
    return pymaker


def test_create_folders(test_pymaker: PyMaker) -> None:
    """Test that the create_folders method creates the project directory."""
    test_pymaker.create_folders()
    assert test_pymaker.choices.project_dir.is_dir()


def test_copy_files(test_pymaker: PyMaker) -> None:
    """Test that the copy_files method copies the template files."""
    test_pymaker.create_folders()

    # this test needs updating to add assertions that the files are copied
    # properly. The 'pyfakefs' package will be useful here.
