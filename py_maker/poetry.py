"""This file contains functions related to using Poetry."""

import os
import subprocess
from typing import Union

from rich import print as rprint

from py_maker.constants import MKDOCS_CONFIG
from py_maker.prompt.prompt import Confirm
from py_maker.schema import ProjectValues


def poetry_install(
    options: dict[str, Union[bool, None]], choices: ProjectValues
) -> bool:
    """Run poetry install if required.

    We also create the MkDocs project if enabled.
    """
    if options["accept_defaults"] or Confirm.ask(
        "\nShould I Run 'poetry install' now?", default=True
    ):
        os.chdir(choices.project_dir)
        subprocess.run(  # noqa: S603
            ["poetry", "install"],  # noqa: S607
            check=True,
        )

        if options["docs"]:
            rprint("\n--> Creating MkDocs project")
            subprocess.run(  # noqa: S603
                [  # noqa: S607
                    "poetry",
                    "run",
                    "mkdocs",
                    "new",
                    ".",
                ],
                check=True,
            )
            # now copy the custom mkdocs.yml file
            (choices.project_dir / "mkdocs.yml").write_text(
                MKDOCS_CONFIG.format(name=choices.name)
            )
        return True

    rprint(
        "[red]\n--> Skipping 'poetry install'. This also skips creating the "
        "MkDocs project."
    )
    return False
