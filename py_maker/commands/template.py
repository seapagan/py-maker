"""Deal with template files."""
import importlib.resources as pkg_resources
from pathlib import Path

import typer
from rich import print  # pylint: disable=redefined-builtin

from py_maker import template
from py_maker.config import Settings
from py_maker.constants import ExitErrors
from py_maker.helpers import get_file_list, header
from py_maker.prompt import Confirm

app = typer.Typer(no_args_is_help=True)


@app.command()
def dump(
    local: bool = typer.Option(
        False,
        "--local",
        "-l",
        help=(
            "Dump the template files to the local directory instead of the "
            "[b]~/.pymaker[/b] folder."
        ),
    )
) -> None:
    """Dump the template files.

    By default this will dump all the default template files to the
    [b]template[/b] sub-folder in the [b]~/.pymaker[/b] folder, however, if you
    specify [b]--local[/b] it will dump them to a [b]template[/b] sub-folder of
    your current directory.
    """
    header()
    template_source = pkg_resources.files(template)

    try:
        if not local:
            output_folder = Path.home() / ".pymaker" / "template"
        else:
            output_folder = Path.cwd() / "template"
            output_folder.mkdir(parents=True, exist_ok=True)

        file_list = get_file_list(template_source)

        for file in file_list:
            with pkg_resources.as_file(template_source / file) as src:
                if src.is_dir():
                    Path(output_folder / file).mkdir(
                        parents=True, exist_ok=True
                    )
                else:
                    dst = output_folder / file
                    dst.write_text(src.read_text(encoding="utf-8"))

        print(f"[green]  -> Template files dumped to:[/green] {output_folder}")

        set_default = Confirm.ask(
            f"\n[green]Set default template folder to:[/green] {output_folder}?"
        )
        if set_default:
            s = Settings()
            s.template_folder = str(output_folder)
            s.use_default_template = False
            s.save()

    except OSError as err:
        print(f"\n[red]  -> Error dumping template:[/red] {err}")
        typer.Exit(ExitErrors.OS_ERROR)


@app.command()
def default(action: str) -> None:
    """Enable or disable the default template folder.

    [b]action[/b] can be either [b]enable[/b] or [b]disable[/b].
    """
    header()
    s = Settings()
    if action == "enable":
        s.use_default_template = True
        s.save()
        print(
            f"[green]  -> Default template folder enabled:[/green] "
            f"{s.template_folder}"
        )
    elif action == "disable":
        s.use_default_template = False
        s.save()
        print("[green]  -> Default template folder disabled[/green]")
    else:
        print(
            f"[red]  -> Invalid action:[/red] {action}\n"
            f"[red]  -> Action must be either:[/red] enable or disable"
        )
        typer.Exit(ExitErrors.INVALID_ACTION)
