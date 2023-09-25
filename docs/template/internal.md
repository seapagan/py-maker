# The Internal Template

By default, the generated application will have a basic template that you can
use to get started, this template is stored inside the package itself. It will
contain all you need to get started, including a basic `README.md` file.

The dependency management is handled by
[Poetry](<https://python-poetry.org/>){:target="_blank"}, and we include a
`pyproject.toml` file with several useful dependencies:

- [PyTest](https://docs.pytest.org/en/stable/contents.html){:target="_blank"}
  for testing, along with several useful plugins.
- The [Black](https://black.readthedocs.io/en/stable/){:target="_blank"}
  code formatter.
- The [Flake8](https://flake8.pycqa.org/en/latest/){:target="_blank"} linter,
  along with a good selection of plugins. It is also set up to use the
  `pyproject.toml` for it's configuration, and to work nicely with Black.
- [Pylint](<https://www.pylint.org/>){:target="_blank"} and
  [Pydocstyle](https://www.pydocstyle.org/en/stable/){:target="_blank"}
  linters.
- [MyPy](https://mypy.readthedocs.io/en/stable/){:target="_blank"} for static
  type checking.
- [Isort](https://pycqa.github.io/isort/){:target="_blank"} for sorting
  imports.
- [pre-commit](https://pre-commit.com/){:target="_blank"} for running checks
  before committing code.

It also contains several tasks for running the tests, linting, formatting and
more. These use the [Poe The
Poet](https://poethepoet.natn.io/){:targer="_blank"} Poetry extension see [Task
Runner](../tasks.md) for more information.
