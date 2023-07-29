"""Helpers for the config module."""
from datetime import datetime

from git.config import GitConfigParser


def get_author_and_email_from_git() -> tuple[str, str]:
    """Get the author name and email from git."""
    config = GitConfigParser()

    return (
        str(config.get_value("user", "name", None)),
        str(config.get_value("user", "email", None)),
    )


def get_current_year() -> str:
    """Get the current year."""
    return str(datetime.now().year)
