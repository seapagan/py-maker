"""Test the pydantic schemas."""

from pathlib import Path

import pytest
from pydantic import ValidationError

from py_maker.schema import ProjectSettings, ProjectValues


def test_project_settings_creation_success() -> None:
    """Test successful creation of a ProjectSettings instance."""
    settings = ProjectSettings(
        description="A test project",
        package_name="test_package",
        author="John Doe",
        email="john.doe@example.com",
        license_name="MIT",
    )
    assert settings.description == "A test project"
    assert settings.package_name == "test_package"
    assert settings.author == "John Doe"
    assert settings.email == "john.doe@example.com"
    assert settings.license_name == "MIT"


def test_project_values_creation_success() -> None:
    """Test successful creation of a ProjectValues instance with all fields."""
    values = ProjectValues(
        description="A test project",
        package_name="test_package",
        author="John Doe",
        email="john.doe@example.com",
        license_name="MIT",
        project_dir=Path("/path/to/project"),
        name="Test Project",
        standalone=True,
        homepage="https://example.com",
        repository="https://github.com/example/test_project",
    )
    assert values.project_dir == Path("/path/to/project")
    assert values.name == "Test Project"
    assert values.standalone is True
    assert values.homepage == "https://example.com"
    assert values.repository == "https://github.com/example/test_project"


def test_project_values_optional_fields() -> None:
    """Test ProjectValues instance creation with optional fields missing."""
    values = ProjectValues(
        description="A test project",
        package_name="test_package",
        author="John Doe",
        email="john.doe@example.com",
        license_name="MIT",
        project_dir=Path("/path/to/project"),
        name="Test Project",
    )
    assert values.homepage is None
    assert values.repository is None


def test_project_settings_defaults() -> None:
    """Test that ProjectSettings fields have correct defaults."""
    settings = ProjectSettings()
    assert settings.description == ""
    assert settings.package_name == ""
    assert settings.author == ""
    assert settings.email == ""
    assert settings.license_name == ""


def test_project_values_defaults() -> None:
    """Test that ProjectValues fields have correct defaults and types."""
    values = ProjectValues()
    assert values.project_dir == Path()
    assert values.name == ""
    assert values.standalone is False  # Noting the default is False, not None
    assert values.homepage is None
    assert values.repository is None


def test_project_values_type_validation() -> None:
    """Test that ProjectValues correctly validates field types."""
    # Example of testing for correct type validation
    with pytest.raises(ValidationError):
        ProjectValues(standalone="not a boolean")  # type: ignore

    with pytest.raises(ValidationError):
        ProjectValues(project_dir=123)  # type: ignore
