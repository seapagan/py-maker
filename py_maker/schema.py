"""Define some Pydantic schemas for the application."""
from pathlib import Path

from pydantic import BaseModel


class ProjectSettings(BaseModel):
    """Base Settings schema for the application."""

    description: str = ""
    package_name: str = ""
    author: str = ""
    email: str = ""
    license: str = ""


class ProjectValues(ProjectSettings):
    """Class to define the values schema.

    Extends the ProjectSettings schema.
    """

    project_dir: Path = Path("")
    name: str = ""
