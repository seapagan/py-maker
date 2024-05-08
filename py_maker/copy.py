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


class ProjectGenerator:
    """Class to encapsulate generating the project from the template."""

    def __init__(
        self,
        *,
        location: str,
        choices: ProjectValues,
        options: dict[str, Union[bool, None]],
        use_default_template: bool = True,
        template_folder: str,
    ) -> None:
        """Initialize the Generate class."""
        self.location = location
        self.options = options
        self.choices = choices
        self.use_default_template = use_default_template
        self.template_folder = template_folder

    def run(self) -> None:
        """Generate the project from the template."""
        self.create_folders()
        self.generate_template()

    def create_folders(self) -> None:
        """Create the root folder for the project."""
        try:
            print("--> Creating project folder ... ", end="")
            if self.location != ".":
                self.choices.project_dir.mkdir()
            print("[green]Done[/green]")
        except FileExistsError:
            print(
                f"\n[red]  -> Error: Directory '{self.choices.project_dir}' "
                "already exists.\n"
            )
            sys.exit(ExitErrors.DIRECTORY_EXISTS)
        except PermissionError:
            print(
                "\n[red]  -> Error: Permission denied creating directory "
                f"'{self.choices.project_dir}'\n"
            )
            sys.exit(ExitErrors.PERMISSION_DENIED)

    def copy_files(
        self,
        template_dir: Union[Traversable, Path],
        file_list: list[Path],
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
                    Path(self.choices.project_dir / file).mkdir()
                elif src.suffix == ".jinja":
                    jinja_template = jinja_env.get_template(str(file))
                    dst = self.choices.project_dir / Path(file).with_suffix("")
                    dst.write_text(
                        jinja_template.render(
                            self.choices.model_dump(),
                            slug=self.choices.project_dir.name,
                            options=self.options,
                        )
                    )
                else:
                    dst = self.choices.project_dir / file
                    dst.write_text(src.read_text(encoding="UTF-8"))

    def generate_template(
        self,
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
            if self.use_default_template:
                file_list = get_file_list(template_dir)
                self.copy_files(template_dir, file_list)

            # --------- copy the custom template files if they exist --------- #
            custom_template_dir = Path(self.template_folder)
            if custom_template_dir.exists():
                file_list = get_file_list(custom_template_dir)
                self.copy_files(custom_template_dir, file_list)

            # ---------------- generate the license file next. ------------- #
            if self.choices.license_name != "None":
                license_env = Environment(
                    loader=FileSystemLoader(str(template_dir / "../licenses")),
                    autoescape=True,
                    keep_trailing_newline=True,
                )
                license_template = license_env.get_template(
                    f"{self.choices.license_name}.jinja"
                )
                dst = self.choices.project_dir / "LICENSE.txt"
                dst.write_text(
                    license_template.render(
                        author=self.choices.author, year=get_current_year()
                    )
                )

            # ---------- rename or delete the 'app' dir if required ---------- #
            if not self.choices.standalone:
                Path(self.choices.project_dir / "app").rename(
                    self.choices.project_dir / self.choices.package_name
                )
            else:
                # move the main.py into the root project folder and delete app
                Path(self.choices.project_dir / "app" / "main.py").rename(
                    Path(self.choices.project_dir / "main.py")
                )
                shutil.rmtree(self.choices.project_dir / "app")

            # ----------- remove the 'test' folder if not required ----------- #
            if not self.options["test"]:
                shutil.rmtree(self.choices.project_dir / "tests")
        except OSError as exc:
            print(f"\n[red]  -> {exc}")
            sys.exit(ExitErrors.OS_ERROR)
