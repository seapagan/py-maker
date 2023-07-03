"""Some constants needed for the rest of the App."""
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

license_names: list[str] = [license["name"] for license in LICENCES]

static_file_list: list[str] = [
    ".gitignore",
    ".markdownlint.json",
    ".pre-commit-config.yaml",
]
dynamic_file_list: list[str] = [
    "README.md.jinja",
    "pyproject.toml.jinja",
]

new_dir_list: list[str] = ["app", "tests"]
