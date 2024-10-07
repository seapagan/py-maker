"""Hook for MkDocs to support Google-style admonitions."""

import re
from typing import Any


def on_page_markdown(markdown: str, **_: dict[str, Any]) -> str:
    """Hook into the markdown rendering."""

    def replace_admonition(match: re.Match[str]) -> str:
        """Actually replace the admonition."""
        type_map: dict[str, str] = {
            "NOTE": "note",
            "TIP": "tip",
            "WARNING": "warning",
            "IMPORTANT": "info",
            "CAUTION": "danger",
        }
        original_type: str = match.group(1)
        admonition_type: str = type_map[
            original_type
        ]  # Direct mapping without .lower()
        content: str = match.group(2).strip()

        # Convert original type to title case
        title_case_type: str = original_type.title()

        # Remove '>' from the beginning of each line and strip whitespace
        content_lines: list[str] = [
            line.lstrip(">").strip() for line in content.split("\n")
        ]

        # Remove any empty lines at the start of the content
        while content_lines and not content_lines[0]:
            content_lines.pop(0)

        # Indent each non-empty line
        indented_content: str = "\n".join(
            f"    {line}" if line else "" for line in content_lines
        )

        return (
            f'!!! {admonition_type} "{title_case_type}"\n\n{indented_content}\n'
        )

    # Use a single regex to match all admonition types and their content
    pattern: str = (
        r"^> \[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\]\n>"
        r"([\s\S]*?)(?=\n(?!>)|\Z)"
    )

    return re.sub(pattern, replace_admonition, markdown, flags=re.MULTILINE)
