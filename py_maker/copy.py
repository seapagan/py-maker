"""Functions to copy files and the templates to the project directory."""

import importlib.resources as pkg_resources
import shutil
import sys
from importlib.resources.abc import Traversable
from pathlib import Path
from typing import Union

from jinja2 import Environment, FileSystemLoader
from rich import print  # pylint: disable=W0622

from py_maker import template
from py_maker.constants import ExitErrors
from py_maker.helpers import get_current_year, get_file_list
from py_maker.schema import ProjectValues


def create_folders(location: str, project_dir: Path) -> None:
    """Create the root folder for the project."""
    try:
        print("--> Creating project folder ... ", end="")
        if location != ".":
            project_dir.mkdir()
        print("[green]Done[/green]")
    except FileExistsError:
        print(
            f"\n[red]  -> Error: Directory '{project_dir}' " "already exists.\n"
        )
        sys.exit(ExitErrors.DIRECTORY_EXISTS)
    except PermissionError:
        print(
            "\n[red]  -> Error: Permission denied creating directory "
            f"'{project_dir}'\n"
        )
        sys.exit(ExitErrors.PERMISSION_DENIED)


def copy_files(
    template_dir: Union[Traversable, Path],
    file_list: list[Path],
    choices: ProjectValues,
    options: dict[str, Union[bool, None]],
) -> None:
    """Copy the template files to the project directory.

    Expand the jinja templates before copying.
    """
    jinja_env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    for file in file_list:
        with pkg_resources.as_file(template_dir / file) as src:  # type: ignore
            if src.is_dir():
                Path(choices.project_dir / file).mkdir()
            elif src.suffix == ".jinja":
                jinja_template = jinja_env.get_template(str(file))
                dst = choices.project_dir / Path(file).with_suffix("")
                dst.write_text(
                    jinja_template.render(
                        choices.model_dump(),
                        slug=choices.project_dir.name,
                        options=options,
                    )
                )
            else:
                dst = choices.project_dir / file
                dst.write_text(src.read_text(encoding="UTF-8"))


def generate_template(
    choices: ProjectValues,
    options: dict[str, Union[bool, None]],
    template_folder: str,
    *,
    use_default_template: bool = True,
) -> None:
    """Copy the template files to the project directory.

    Any file that has the '.jinja' extension will be passed though the
    template engine before copying. The extension will also be removed.

    ie:
    'README.md.jinja' is copied as 'README.md' after template substitution.
    """
    try:
        # ---------------- copy the default template files --------------- #
        template_dir = pkg_resources.files(template)
        if use_default_template:
            file_list = get_file_list(template_dir)
            copy_files(template_dir, file_list, choices, options)

        # --------- copy the custom template files if they exist --------- #
        custom_template_dir = Path(template_folder)
        if custom_template_dir.exists():
            file_list = get_file_list(custom_template_dir)
            copy_files(custom_template_dir, file_list, choices, options)

        # ---------------- generate the license file next. ------------- #
        if choices.license_name != "None":
            license_env = Environment(
                loader=FileSystemLoader(str(template_dir / "../licenses")),
                autoescape=True,
                keep_trailing_newline=True,
            )
            license_template = license_env.get_template(
                f"{choices.license_name}.jinja"
            )
            dst = choices.project_dir / "LICENSE.txt"
            dst.write_text(
                license_template.render(
                    author=choices.author, year=get_current_year()
                )
            )

        # ---------- rename or delete the 'app' dir if required ---------- #
        if not choices.standalone:
            Path(choices.project_dir / "app").rename(
                choices.project_dir / choices.package_name
            )
        else:
            # move the main.py into the root project folder and delete app
            Path(choices.project_dir / "app" / "main.py").rename(
                Path(choices.project_dir / "main.py")
            )
            shutil.rmtree(choices.project_dir / "app")

        # ----------- remove the 'test' folder if not required ----------- #
        if not options["test"]:
            shutil.rmtree(choices.project_dir / "tests")
    except OSError as exc:
        print(f"\n[red]  -> {exc}")
        sys.exit(ExitErrors.OS_ERROR)
