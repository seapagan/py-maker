# Task Runner

The task-runner [Poe the
Poet](https://github.com/nat-n/poethepoet){:target="_blank"} is installed in the
new project as a development dependency which allows us to run simple tasks
(similar to npm `scripts`).

These are run (from within the virtual environment) using the `poe` command and
then the script name, for example:

```console
$ poe pre
```

To get a list of all available tasks with a description, run:

```console
$ poe
```

You can define your own, but there are 8 specific ones provided with the script.

- `pre` : Run `pre-commit run --all-files`
- `ruff`: Run Ruff linter on all Python files in the project.
- `format`: Run Ruff Formatter on all Python files in the project.
- `mypy` : Run MyPy type-checker on all Python files in the project.
- `markdown` : Run pymarkdown on all markdown files in the project.

- `lint` = Runs ruff, formatter, mypy, markdown in sequence

If you selected to install MkDocs with this project, then there are some extra
tasks to help with that:

- `docs:publish` : Deploy the documentation to GitHub pages.
- `docs:build` : Build the documentation locally.
- `docs:serve` : Serve the documentation locally. Useful during development.
- `docs:serve:all` : As above, but allows access from other devices on the
  network.

There is also a task to run the tests:

```console
$ poe test
```

Finally, you can generate you CHANGELOG.md file using:

```console
$ poe changelog
```

These are defined in the `pyproject.toml` file in the `[tool.poe.tasks]`
section. Take a look at this file if you want to add or remove tasks.
