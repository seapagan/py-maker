# Task Runner

The task-runner [Poe the
Poet](https://github.com/nat-n/poethepoet){:target="_blank"} is installed as a
development dependency which allows us to run simple tasks (similar to npm
`scripts`).

These are run (from within the virtual environment) using the `poe` command and
then the script name, for example:

```console
$ poe pre
```

You can define your own, but there are 7 specific ones provided with the script.

- `pre` : Run `pre-commit run --all-files`
- `pylint`: Run Pylint on all Python files in the project.
- `mypy` = Run MyPy type-checker on all Python files in the project.
- `flake8` = Run Flake8 linter on all Python files in the project.
- `black` = Run Black code formatter on all Python files in the project.
- `try` = Run Tryceratops linter on all Python files in the project.

- `lint` = Runs pylint, mypy, flake8 and black in sequence

These are defined in the `pyproject.toml` file in the `[tool.poe.tasks]`
section. Take a look at this file if you want to add or remove tasks.
