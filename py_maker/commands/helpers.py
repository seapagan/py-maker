"""Helper functions for the CLI commands.""" ""
import re
from typing import Dict, List

from git.config import GitConfigParser

LICENCES: List[Dict[str, str]] = [
    {"name": "None", "url": ""},
    {"name": "Apache2", "url": "https://opensource.org/licenses/Apache-2.0"},
    {"name": "BSD3", "url": "https://opensource.org/licenses/BSD-3-Clause"},
    {"name": "BSD2", "url": "https://opensource.org/licenses/BSD-2-Clause"},
    {"name": "GPL", "url": "https://opensource.org/licenses/gpl-license"},
    {"name": "LGPL", "url": "https://opensource.org/licenses/lgpl-license"},
    {"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    {"name": "MPL2", "url": "https://opensource.org/licenses/MPL-2.0"},
    {"name": "CDDL", "url": "https://opensource.org/licenses/CDDL-1.0"},
    {"name": "EPL", "url": "https://opensource.org/licenses/EPL-2.0"},
]

license_names = [license["name"] for license in LICENCES]


def get_title(location: str):
    """Get the title for the application."""
    return re.sub("[_-]", " ", location).title() if location != "." else ""


def get_author_and_email_from_git():
    """Get the author name and email from git."""
    config = GitConfigParser()

    return config.get_value("user", "name", None), config.get_value(
        "user", "email", None
    )
