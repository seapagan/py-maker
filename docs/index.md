# Python Project Generation Tool

[![Codacy
Badge](https://app.codacy.com/project/badge/Grade/7c86940f816b455ab171dc8126476849)](https://app.codacy.com/gh/seapagan/py-maker/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)&nbsp;
[![CodeQL](https://github.com/seapagan/py-maker/actions/workflows/codeql.yml/badge.svg)](https://github.com/seapagan/py-maker/actions/workflows/codeql.yml)&nbsp;
![PyPI - License](https://img.shields.io/pypi/l/pyproject-maker)&nbsp;
[![Downloads](https://static.pepy.tech/personalized-badge/pyproject-maker?period=week&units=international_system&left_color=black&right_color=green&left_text=Weekly%20Downloads)](https://pepy.tech/project/pyproject-maker)&nbsp;
[![Downloads](https://static.pepy.tech/personalized-badge/pyproject-maker?period=total&units=international_system&left_color=black&right_color=green&left_text=Total%20Downloads)](https://pepy.tech/project/pyproject-maker)

A fully customizable Python application to bootstrap
[Poetry](https://python-poetry.org/){:target="_blank"}-based boilerplate for you
to start developing your Python applications quicker! Includes linting and
Pytest libraries.

It will create a new directory for your project (or use the current directory),
initialise a git repository, create a virtual environment, and install some
basic dependencies for Testing, Linting and more.

Latest Version : [{{ latest-git-tag
}}](https://pypi.org/project/pyproject-maker/){:target="_blank"}

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

## Customize the generated project

You can add extra or edited files to the generated project by adding them to the
`~/.pymaker/template` directory.  The files in this directory will be copied
into the generated project, overwriting any existing files with the same name.

It is also possible to dump the whole template into this folder or the current
folder so full customization and even removal of files is possible.

## Pre-commit

The generated project uses
[pre-commit](https://pre-commit.com/){:target="_blank"} to run some checks on
the code before it is committed.  This is a great tool to help keep your code
clean.

To install pre-commit, run the following command from inside your venv:

```console
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## GitHub Actions and Configuration

By default the generated project includes a GitHub Actions workflow to run
[Dependabot](https://dependabot.com/){:target="_blank"} to keep your
dependencies up to date. There are also standard templates for Pull Request and
Issues.

The plan is to add more workflows in the future, for example running tests and
more.

## Community related files

To aid in community building, the generated project includes a
`CODE_OF_CONDUCT.md` file.  This is based on the [Contributor
Covenant](https://www.contributor-covenant.org/){:target="_blank"} standard.

Future releases will include other Community related files (for example an
`AUTHORS` and `CONTRIBUTING` file.).

## Contributing to this Project

For information on how to contribute to the project, see the `CONTRIBUTING.md`
file in the root of the repository or [on this website](contributing.md)
