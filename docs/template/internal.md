# The Internal Template

By default, the generated application will have a basic template that you can
use to get started, this template is stored inside the package itself. It will
contain all you need to get started, including a basic `README.md` file.

The dependency management is handled by
[Poetry](<https://python-poetry.org/>){:target="_blank"}, and we include a
`pyproject.toml` file with several useful dependencies:

- [PyTest](https://docs.pytest.org/en/stable/contents.html){:target="_blank"}
  for testing, along with several useful plugins.
- [Ruff](https://docs.astral.sh/ruff/){:target="_blank"} for linting and
  formatting. This replaces the need for `flake8`, `black`, `isort` and more.
  The default `pyproject.toml` contains a quite strict configuration by default,
  but you can modify it to suit your needs.
- [MyPy](https://mypy.readthedocs.io/en/stable/){:target="_blank"} for static
  type checking.
- [pre-commit](https://pre-commit.com/){:target="_blank"} for running checks
  before committing code.

The `pyproject.toml` contains a useable configuration for all of these tools,
but you can modify it to suit your needs.

It also contains several tasks for running the tests, linting, formatting and
more. These use the [Poe The
Poet](https://poethepoet.natn.io/){:target="_blank"} Poetry extension see [Task
Runner](../tasks.md) for more information.
