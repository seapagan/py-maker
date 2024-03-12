"""Class to encapsulate the application."""

from __future__ import annotations

import importlib.resources as pkg_resources
import os
import re
import shutil
import subprocess  # nosec
import sys
from pathlib import Path, PurePath
from typing import TYPE_CHECKING, Union

from git.exc import GitError
from git.repo import Repo
from jinja2 import Environment, FileSystemLoader
from rich import print  # pylint: disable=W0622

from py_maker import template
from py_maker.config import get_settings
from py_maker.constants import MKDOCS_CONFIG, ExitErrors, license_names
from py_maker.github_ctrl import GitHub
from py_maker.helpers import (
    exists_on_pypi,
    get_current_year,
    get_file_list,
    get_title,
    header,
    sanitize,
)
from py_maker.prompt import Confirm, Prompt
from py_maker.schema import ProjectValues

if TYPE_CHECKING:
    from importlib.resources.abc import Traversable


class PyMaker:
    """PyMaker class."""

    def __init__(
        self, location: str, options: dict[str, Union[bool, None]]
    ) -> None:
        """Initialize the PyMaker class."""
        self.choices: ProjectValues = ProjectValues()
        self.location: str = location
        self.options: dict[str, Union[bool, None]] = options

        # this will be updated if we run 'poetry install' later, so other stages
        # that need to know if poetry has been run can check this flag.
        self.poetry_is_run = False
        self.git_is_run = False

        header()

        self.settings = get_settings()

        if len(Path(self.location).parts) > 1:
            print(
                "[red]  -> Error: Location must be a single directory name, "
                "and is relative to the current directory.\n"
            )
            sys.exit(ExitErrors.LOCATION_ERROR)

    def confirm_values(self) -> bool:
        """Confirm the values entered by the user."""
        print(
            "\n[green][bold]Creating a New Python app with the below "
            "settings :\n"
        )

        padding: int = max(len(key) for key, _ in self.choices) + 3

        for key, value in self.choices:
            print(f"{get_title(key).rjust(padding)} : [green]{value}")

        return Confirm.ask("\nIs this correct?", default=True)

    # ------------------------------------------------------------------------ #
    #                   create the project skeleton folders.                   #
    # ------------------------------------------------------------------------ #
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

    # ------------------------------------------------------------------------ #
    #             Copy the template files to the project directory.            #
    # ------------------------------------------------------------------------ #
    def copy_files(
        self, template_dir: Union[Traversable, Path], file_list: list[Path]
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

    def generate_template(self) -> None:
        """Copy the template files to the project directory.

        Any file that has the '.jinja' extension will be passed though the
        template engine before copying. The extension will also be removed.

        ie:
        'README.md.jinja' is copied as 'README.md' after template substitution.
        """
        try:
            # ---------------- copy the default template files --------------- #
            template_dir = pkg_resources.files(template)
            if self.settings.use_default_template:
                file_list = get_file_list(template_dir)
                self.copy_files(template_dir, file_list)

            # --------- copy the custom template files if they exist --------- #
            custom_template_dir = Path(self.settings.template_folder)
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

    # ------------------------------------------------------------------------ #
    #                create the git repository for the project.                #
    # ------------------------------------------------------------------------ #
    def create_git_repo(self) -> None:
        """Create a Git repository for the project and add the first commit."""
        if not self.options["git"]:
            return
        try:
            print("\n--> Creating Git repository ... ", end="")
            repo = Repo.init(self.choices.project_dir)
            repo.index.add(repo.untracked_files)
            repo.index.commit("Initial Commit")
            print("[green]Done[/green]")
            self.git_is_run = True
        except GitError as exc:
            print("Error: ", exc)
            sys.exit(ExitErrors.GIT_ERROR)

    # ------------------------------------------------------------------------ #
    #                       display post-process messages                      #
    # ------------------------------------------------------------------------ #
    def post_process(self) -> None:
        """Display steps to be carried out after the project is created.

        Currently just prints messages on what to do next.
        """
        proj_loc = (
            self.location if self.location != "." else self.choices.project_dir
        )
        run_cmd = (
            f"{self.location}"
            if not self.choices.standalone
            else "python main.py"
        )

        output = f"""
--> [green]Project created successfully.[/green]

[bold]Next steps:[/bold]

    1) Change to the project directory:
        'cd {proj_loc}'
    2) Install the dependencies if not done (creates a virtual environment):
        'poetry install'
    3) Activate the virtual environment:
        'poetry shell'
    4) Run the application:
        '{run_cmd}'
    5) Code!

See the [bold][green]README.md[/green][/bold] file for more information.
        """
        print(output)

    # ------------------------------------------------------------------------ #
    #               get a sanitized package name from user input.              #
    # ------------------------------------------------------------------------ #
    def get_sanitized_package_name(self, pk_name: str) -> str:
        """Return a sanitized package name from user input."""
        while True:
            name = Prompt.ask(
                "Package Name? (Use '-' for standalone script)",
                default=pk_name
                if pk_name != "."
                else sanitize(self.choices.project_dir.name),
            )
            # a single '-' is ok as it means a standalone script.
            if name == "-":
                self.choices.standalone = True
                break

            # note: not happy with this nested if/else, but it works for now.
            # will fix during the next refactor.
            if not re.search(r"[- .]", name):
                if exists_on_pypi(name):
                    print(
                        "\n[red]Warning: Package name already exists on PyPI."
                    )
                    confirm = Confirm.ask(
                        "Do you want to use it anyway?", default=False
                    )
                    if confirm:
                        print(
                            "\n[red]Warning: Using an existing package name "
                            "will mean it [b]cannot be uploaded to PyPI.\n"
                        )
                        break
                else:
                    break
            else:
                print(
                    "\n[red]Error: Package name cannot contain dashes, dots or "
                    "spaces. Please use Underscores if required.\n"
                )
        return name

    # ------------------------------------------------------------------------ #
    #              accept all the default values for the project.              #
    # ------------------------------------------------------------------------ #
    def accept_defaults(self) -> None:
        """Accept the default values for the project."""
        self.choices.name = get_title(PurePath(self.choices.project_dir).name)
        self.choices.package_name = sanitize(self.choices.project_dir.name)
        self.choices.description = ""
        self.choices.author = self.settings.author_name
        self.choices.email = self.settings.author_email
        self.choices.license_name = self.settings.default_license

    def get_input(self) -> None:
        """Get the user input for the project."""
        self.choices.name = Prompt.ask(
            "Name of the Application?",
            default=get_title(PurePath(self.choices.project_dir).name),
        )
        pk_name = sanitize(self.location)

        # if this is not a standalone script, ask for more details, useful
        # for PypI uploads.
        if not self.choices.standalone:
            self.choices.package_name = self.get_sanitized_package_name(pk_name)

        self.choices.homepage = Prompt.ask("Homepage URL?", default=None)

        # offer to create a repo on GitHub, for both type of projects.
        github_username = (
            self.settings.github_username
            if self.settings.github_username
            else "<your GitHub username>"
        )
        repo_name = (
            sanitize(self.choices.project_dir.name)
            if self.choices.package_name == "-"
            else self.choices.package_name
        )
        self.choices.repository = Prompt.ask(
            "Repository URL?",
            default=(
                f"https://github.com/{github_username}/"
                f"{re.sub(r'[_.]+', '-', repo_name.lower())}"
            ),
        )

        self.choices.description = Prompt.ask(
            "Description of the Application?",
        )
        self.choices.author = Prompt.ask(
            "Author Name?", default=self.settings.author_name
        )

        self.choices.email = Prompt.ask(
            "Author Email?", default=self.settings.author_email
        )
        self.choices.license_name = Prompt.ask(
            "Application License?",
            choices=license_names,
            default=self.settings.default_license,
        )

        if not self.confirm_values():
            # User chose not to continue
            print("\n[red]Aborting![/red]")
            sys.exit(ExitErrors.USER_ABORT)

        print()

    # ------------------------------------------------------------------------ #
    #                     run 'poetry install' if required.                    #
    # ------------------------------------------------------------------------ #
    def run_poetry(self) -> None:
        """Run poetry install if required.

        We also create the MkDocs project if enabled.
        """
        if self.options["accept_defaults"] or Confirm.ask(
            "\nShould I Run 'poetry install' now?", default=True
        ):
            os.chdir(self.choices.project_dir)
            subprocess.run(
                ["poetry", "install"],  # noqa: S603, S607
                check=True,
            )
            self.poetry_is_run = True

            if self.options["docs"]:
                print("\n--> Creating MkDocs project")
                subprocess.run(
                    [  # noqa: S603, S607
                        "poetry",
                        "run",
                        "mkdocs",
                        "new",
                        ".",
                    ],
                    check=True,
                )
                # now copy the custom mkdocs.yml file
                (self.choices.project_dir / "mkdocs.yml").write_text(
                    MKDOCS_CONFIG.format(name=self.choices.name)
                )

    # ------------------------------------------------------------------------ #
    #            optionally install and update the pre-commit hooks            #
    # ------------------------------------------------------------------------ #
    def install_precommit(self) -> None:
        """Install pre-commit hooks - IF poetry and git are run.

        This would fail without either of them.
        """
        if (
            self.poetry_is_run
            and self.git_is_run
            and self.settings.install_pre_commit
            and (
                self.options["accept_defaults"]
                or Confirm.ask(
                    "\nDo you want to install and update the [bold]"
                    "pre-commit[/bold] hooks?",
                    default=True,
                )
            )
        ):
            print("\n--> Install and Update pre-commit hooks")
            os.chdir(self.choices.project_dir)
            subprocess.run(
                [  # noqa: S603, S607
                    "poetry",
                    "run",
                    "pre-commit",
                    "install",
                ],
                check=True,
            )
            subprocess.run(
                [  # noqa: S603, S607
                    "poetry",
                    "run",
                    "pre-commit",
                    "autoupdate",
                ],
                check=True,
            )
        else:
            print(
                """\n  [red]Warning: pre-commit hooks not installed or updated.

[/red]  pre-commit needs both 'poetry install' and 'git init' to be run.
  Once this is done, you can install and update the pre-commit hooks later by
  running:

  [bold]$ poetry run pre-commit install[/bold]

  and

  [bold]$ poetry run pre-commit autoupdate[/bold]

  Note that this is totally [bold]optional, but recommended.
                """
            )

    def create_remote_repo(self) -> None:
        """Create a remote repo on GitHub for this new project.

        If creation is successful then adjust the local repo to use the remote.
        and push the existing local repo to the remote.
        """
        if (
            self.options["git"]
            and self.settings.github_token
            and self.choices.repository
            and self.options["github"]
            and (
                self.options["accept_defaults"]
                or Confirm.ask(
                    "\nDo you want to create a remote repository on GitHub?",
                    default=True,
                )
            )
        ):
            print("\n--> Creating remote repository on GitHub")
            os.chdir(self.choices.project_dir)
            # get the repo name only from the full URL
            repo_name = Path(self.choices.repository).name
            github = GitHub(
                self.settings.github_token,
                repo_name,
            )
            new_repo = github.create_repo(description=self.choices.description)
            if new_repo:
                print("--> Pushing new Project to GitHub")
                try:
                    git_url = (
                        new_repo.ssh_url
                        if self.settings.github_protocol == "ssh"
                        else new_repo.html_url
                    )
                    local_repo = Repo(self.choices.project_dir)
                    local_repo.create_remote("origin", git_url)
                    local_repo.remote("origin").push("main")
                except GitError as exc:
                    print(
                        "\n  [red]Warning: Error creating Remote repository."
                        " Please check the GitHub token and try again."
                        f"\n  Error: {exc}[/red]\n"
                    )

        else:
            print(
                "\n  [blue]Info: Remote repository not created."
                " Either you chose not to, or you did not provide a GitHub"
                " Personal Access Token (PAT) in the settings file.\n"
                "        See https://py-maker.seapagan.net/configuration/"
                "#add-a-github-personal-access-token"
                " for more details.\n"
            )

    # ------------------------------------------------------------------------ #
    #             The main application loop is on the .run() method.           #
    # ------------------------------------------------------------------------ #
    def run(self) -> None:
        """Run the full process to create the project.

        We get input from the user, as well as the options passed in from the
        command line. We then create the project skeleton, copy the template
        files, create the license file, create the git repo, optionally run
        'poetry install' and install the 'pre-commit' hooks.
        """
        self.choices.project_dir = Path.cwd() / self.location

        # ensure that the chosen location is empty.
        if (
            self.choices.project_dir.exists()
            and len(os.listdir(self.choices.project_dir)) > 0
        ):
            print(
                "\n[red]Error: The chosen folder is not empty. "
                "Please specify a different location.[/red]\n"
            )
            sys.exit(ExitErrors.FOLDER_NOT_EMPTY)

        print(
            "[green]Creating a new project at[/green] "
            f"{self.choices.project_dir}\n"
        )

        self.choices.standalone = bool(self.options["standalone"])

        if self.options["accept_defaults"]:
            self.accept_defaults()
        else:
            self.get_input()

        if self.options["bare"]:
            self.options["test"] = False
            self.options["lint"] = False
            self.options["docs"] = False
            self.options["git"] = False

        self.create_folders()
        self.generate_template()

        self.run_poetry()
        self.create_git_repo()
        self.install_precommit()

        self.create_remote_repo()

        self.post_process()
