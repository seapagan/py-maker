"""Some constants needed for the rest of the App."""

from enum import IntEnum

LICENCES: list[dict[str, str]] = [
    {"name": "None", "url": ""},
    {"name": "Apache2", "url": "https://opensource.org/licenses/Apache-2.0"},
    {"name": "BSD3", "url": "https://opensource.org/licenses/BSD-3-Clause"},
    {"name": "BSD2", "url": "https://opensource.org/licenses/BSD-2-Clause"},
    {"name": "GPL2", "url": "https://opensource.org/licenses/gpl-2.0"},
    {"name": "GPL3", "url": "https://opensource.org/licenses/gpl-3.0"},
    {"name": "LGPL", "url": "https://opensource.org/licenses/lgpl-license"},
    {"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    {"name": "MPL2", "url": "https://opensource.org/licenses/MPL-2.0"},
    {"name": "CDDL", "url": "https://opensource.org/licenses/CDDL-1.0"},
    {"name": "EPL2", "url": "https://opensource.org/licenses/EPL-2.0"},
]

license_names: list[str] = [license_dict["name"] for license_dict in LICENCES]


class ExitErrors(IntEnum):
    """Exit errors.

    Error codes for the application.
    """

    LOCATION_ERROR = 1
    DIRECTORY_EXISTS = 2
    GIT_ERROR = 3
    FOLDER_NOT_EMPTY = 4
    PERMISSION_DENIED = 5
    USER_ABORT = 6
    OS_ERROR = 7
    INVALID_ACTION = 8
    TOML_ERROR = 9


MKDOCS_CONFIG = """
site_name: {name}

# default to using the material theme
theme:
  name: material

# default plugins here are to minify the html, css and js plus enable the search
# plugin. Adjust to your liking.
plugins:
  - search
  - minify:
      minify_html: true
      minify_css: true
      minify_js: true
      htmlmin_opts:
        remove_comments: true
        remove_empty_space: true

# edit these MARKDOWN extensions to your liking
markdown_extensions:
  - admonition
  - pymdownx.snippets
  - pymdownx.superfences
  - pymdownx.highlight
  - attr_list
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
"""
