# Python Project Generation Tool

This is a command line tool to help you create new Python projects.  It will
create a new directory for your project, initialise a git repository, create a
virtual environment, and install some basic dependencies.

Latest Version : {{ latest-git-tag }}

## Testing

The generated project includes
[pytest](https://docs.pytest.org/en/latest/){:target="_blank"} and some related
plugins to allow you to set up testing straight away.

Write your tests in the `tests` directory and run them with `pytest`.

## Linting

The generated project includes
[flake8](https://flake8.pycqa.org/en/latest/){:target="_blank"} (with several
plugins) for linting and
[Black](https://black.readthedocs.io/en/stable/){:target="_blank"} for
formatting. [Mypy](http://mypy-lang.org/){:target="_blank"} is installed for
type checking. [isort](https://pycqa.github.io/isort/){:target="_blank"},
[Pylint](https://pylint.org/) and
[tyrceratops](https://github.com/guilatrova/tryceratops){:target="_blank"} are
also installed as standard.

## Pre-commit

The generated project uses [pre-commit](https://pre-commit.com/) to run some
checks on the code before it is committed.  This is a great tool to help keep
your code clean.

To install pre-commit, run the following command from inside your venv:

```console
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```
