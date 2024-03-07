"""Deal with template files."""

import importlib.resources as pkg_resources
from pathlib import Path
from typing import TYPE_CHECKING

import typer
from rich import print  # pylint: disable=redefined-builtin

from py_maker import template
from py_maker.config import get_settings
from py_maker.constants import ExitErrors
from py_maker.helpers import get_file_list, header
from py_maker.prompt import Confirm

if TYPE_CHECKING:
    from importlib.abc import Traversable

app = typer.Typer(no_args_is_help=True)


@app.command()
def dump(
    *,
    local: bool = typer.Option(
        False,
        "--local",
        "-l",
        help=(
            "Dump the template files to the local directory instead of the "
            "[b]~/.pymaker[/b] folder."
        ),
    ),
) -> None:
    """Dump the template files.

    By default this will dump all the default template files to the
    [b]template[/b] sub-folder in the [b]~/.pymaker[/b] folder, however, if you
    specify [b]--local[/b] it will dump them to a [b]template[/b] sub-folder of
    your current directory.
    """
    header()
    template_source: Traversable = pkg_resources.files(template)
    settings = get_settings()

    try:
        if not local:
            output_folder = Path.home() / ".pymaker" / "template"
            output_folder.mkdir(parents=True, exist_ok=True)
        else:
            output_folder = Path.cwd()

        if any(output_folder.iterdir()) and not Confirm.ask(
            f"[red]The output folder:[/red] {output_folder} "
            "[red]is not empty, do you want to continue?[/red]",
            default=False,
        ):
            raise typer.Exit(ExitErrors.USER_ABORT)

        file_list: list[Path] = get_file_list(template_source)

        for file in file_list:
            src_path = template_source.joinpath(str(file))
            with pkg_resources.as_file(src_path) as src:
                if src.is_dir():
                    Path(output_folder / file).mkdir(
                        parents=True, exist_ok=True
                    )
                else:
                    dst = output_folder / file
                    dst.write_text(src.read_text(encoding="utf-8"))

        print(f"[green]  -> Template files dumped to:[/green] {output_folder}")

        set_default = Confirm.ask(
            f"\n[green]Set the template folder to:[/green] {output_folder}?",
            default=True,
        )

        if set_default:
            print("[green]  -> Template folder set[/green]")
            settings.template_folder = str(output_folder)

            if Confirm.ask(
                "[green]Disable the default template folder?", default=False
            ):
                print("[green]  -> Default template folder disabled[/green]")
                settings.use_default_template = False

            settings.save()

    except OSError as exc:
        print(f"\n[red]  -> Error dumping template:[/red] {exc}")
        raise typer.Exit(ExitErrors.OS_ERROR) from exc


@app.command()
def default(action: str) -> None:
    """Enable or disable using the INTERNAL templates.

    [b]action[/b] can be either [b]enable[/b] or [b]disable[/b].

    [b]enable[/b] will enable the internal template
    [b]disable[/b] will disable the internal template folder
    """
    settings = get_settings()
    header()
    if action == "enable":
        settings.use_default_template = True
        settings.save()
        print(
            "[green]  -> Default template folder enabled:[/green] "
            f"{settings.template_folder}"
        )
    elif action == "disable":
        settings.use_default_template = False
        settings.save()
        print("[green]  -> Default template folder disabled[/green]")
    else:
        print(
            f"[red]  -> Invalid action:[/red] {action}\n"
            "[red]  -> Action must be either:[/red] enable or disable"
        )
        raise typer.Exit(ExitErrors.INVALID_ACTION)


@app.command(name="set")
def set_template() -> None:
    """Set the template folder to the current directory.

    The [i]'Use Default Template'[/i] setting [b][red]will not be changed[/b].
    """
    settings = get_settings()
    header()
    if not Confirm.ask(
        "[red]Are you sure you want to set the template folder to the "
        "current folder?[/red]",
        default=False,
    ):
        raise typer.Exit(ExitErrors.USER_ABORT)
    settings.template_folder = str(Path.cwd())
    settings.save()

    print(
        "[green]  -> Template folder set to:[/green] "
        f"{settings.template_folder}"
    )
    print(
        "[yellow]  -> The 'Use Default Template' setting has not been "
        "changed.\n"
        "[yellow]     You can change this with the '[b][i]pymaker template "
        "default'[/i][/b] command.\n"
    )


@app.command(name="reset")
def reset_template() -> None:
    """Reset the template folder to the default.

    This is currrently [b]~/.pymaker/template[/b].
    The [i]'Use Default Template'[/i] setting [b][red]will not be changed[/b].
    """
    settings = get_settings()
    header()
    if not Confirm.ask(
        "[red]Are you sure you want to reset the template folder to the "
        "default?[/red]",
        default=False,
    ):
        raise typer.Exit(ExitErrors.USER_ABORT)

    settings.template_folder = str(Path.home() / ".pymaker" / "template")
    settings.save()
    print(
        "[green]  -> Template folder reset to:[/green] "
        f"{settings.template_folder}"
    )
    print(
        "[yellow]  -> The 'Use Default Template' setting has not been "
        "changed.\n"
        "[yellow]     You can change this with the '[b][i]pymaker template "
        "default'[/i][/b] command.\n"
    )
