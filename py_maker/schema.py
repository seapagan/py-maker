"""Define some Pydantic schemas for the application."""
from pathlib import Path

from pydantic import BaseModel


class ProjectValues(BaseModel):
    """Class to define the values schema."""

    project_dir: Path = Path("")
    name: str = ""
    author: str = ""
    email: str = ""
    license: str = ""
