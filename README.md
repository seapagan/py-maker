# Python Project Generation Tool <!-- omit in toc -->

[![PyPI version](https://badge.fury.io/py/pyproject-maker.svg)](https://badge.fury.io/py/pyproject-maker)
[![Codacy
Badge](https://app.codacy.com/project/badge/Grade/7c86940f816b455ab171dc8126476849)](https://app.codacy.com/gh/seapagan/py-maker/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![CodeQL](https://github.com/seapagan/py-maker/actions/workflows/codeql.yml/badge.svg)](https://github.com/seapagan/py-maker/actions/workflows/codeql.yml)
![PyPI - License](https://img.shields.io/pypi/l/pyproject-maker)
[![Weekly Downloads](https://static.pepy.tech/personalized-badge/pyproject-maker?period=week&units=international_system&left_color=black&right_color=green&left_text=Weekly%20Downloads)](https://pepy.tech/project/pyproject-maker)
[![Total Downloads](https://static.pepy.tech/personalized-badge/pyproject-maker?period=total&units=international_system&left_color=black&right_color=green&left_text=Total%20Downloads)](https://pepy.tech/project/pyproject-maker)

A fully customizable Python application to bootstrap
[Poetry](https://python-poetry.org/)-based boilerplate for you to start
developing your Python applications quicker! Includes linting and Pytest
libraries, a task runner, pre-commit hooks, and optionally create a git
repository and upload to GitHub. you can also fully customize the template used.

Full documentation for this project with usage examples is available at
<https://py-maker.seapagan.net/>

- [Installation](#installation)
- [Usage](#usage)
  - [Linting](#linting)
  - [Customise](#customise)
  - [Task Runner](#task-runner)
  - [Pre-commit](#pre-commit)
- [GitHub Actions and Configuration](#github-actions-and-configuration)
- [Contributing to Py-Maker](#contributing-to-py-maker)
- [License](#license)

## Installation

It is best to install this package globally, rather than in a virtual
environment, as it is intended to be used to create new projects.

Install the package globally using pip:

```console
$ pip install pyproject-maker
```

If you cannot install globally due to permissions, you can install it to your
user install directory:

```console
$ pip install --user pyproject-maker
```

or use [pipx](https://pypa.github.io/pipx/) (recommended)

```console
$ pipx install pyproject-maker
```

## Usage

To create a new project, run the following command:

```console
$ pymaker new <project-folder>
```

This will create a new directory with the name you provide, and run the steps
needed to get you started quickly:

1. Copy the template files into the new directory
2. Initialise a git repository
3. Commit the boilerplate to Git

You will be asked a series of questions to customise the new project.

When it asks "Package Name?" you can choose two variants :

1. If you wish for a standard Python package that can optionally be uploaded to
   <http://pypi.org>, enter a package name here. Note that underscores ("_")
   must be used as opposed to dashes ("-") to comply with Python package naming
   rules.
2. Enter '-' to instruct the tool that you are not creating any package, just a
   standalone app, and then the `main.py` will just be placed in the project
   root.

You should now change into the new directory, install dependencies and activate
the virtual environment:

```console
$ cd <project-folder>
$ poetry install
$ poetry shell
```

Now, you can start developing :smile:

### Linting

The generated project includes [Ruff](https://docs.astral.sh/ruff/) for linting
and formatting. [Mypy](http://mypy-lang.org/) is installed for type checking.

### Customise

For a 'package' project, the `pyproject.toml` file is set up to put the code in
a sub-folder with the same name as chosen for the 'Package Name'. You can change
this to whatever you require, just remember to update the `pyproject.toml` file
to match.

You can also modify the template used to generate the new project.

Check the documentation at <https://py-maker.seapagan.net/> for more details.

### Task Runner

The task-runner [Poe the Poet](https://github.com/nat-n/poethepoet) is installed
as a development dependency which allows us to run simple tasks (similar to npm
`scripts`).

These are run (from within the virtual environment) using the `poe` command and
then the script name, for example:

```console
$ poe pre
```

You can define your own, but there are 6 specific ones provided with the script.

- `pre` : Run `pre-commit run --all-files`
- `ruff`: Run Ruff linter on all Python files in the project.
- `format`: Run Ruff formatter on all Python files in the project.
- `mypy`: Run MyPy type-checker on all Python files in the project.
- `markdown`: Run pymarkdown on all markdown files in the project.

- `lint`: Runs ruff, format, mypy, and markdown in sequence

These are defined in the `pyproject.toml` file in the `[tool.poe.tasks]`
section. Take a look at this file if you want to add or remove tasks.

### Pre-commit

The generated project uses [pre-commit](https://pre-commit.com/) to run some
checks on the code before it is committed.  This is a great tool to help keep
your code clean.

To install pre-commit, run the following command from inside your venv:

```console
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## GitHub Actions and Configuration

By default the generated project includes a GitHub Actions workflow to run
[Dependabot](https://dependabot.com/) to keep your dependencies up to date.
There are also standard templates for Pull Request and Issues.

The plan is to add more workflows in the future, for example running tests and
more.

## Contributing to Py-Maker

All contributions, bug reports, bug fixes, documentation improvements,
enhancements, and ideas are welcome.

A detailed overview on how to contribute can be found in the **[contributing
guide](CONTRIBUTING.md)** and on the
[website](http://py-maker.seapagan.net/contributing/).

If you are simply looking to start working with the codebase, navigate to the
[GitHub "issues" tab](https://github.com/seapagan/py-maker/issues) and start
looking through interesting issues. There may be issues listed under
[documentation](https://github.com/seapagan/py-maker/issues?labels=documentation&sort=updated&state=open)
and [good first
issue](https://github.com/seapagan/py-maker/issues?labels=good+first+issue&sort=updated&state=open)
where you could start out.

You can also triage issues which may include reproducing bug reports, or asking
for vital information such as version numbers or reproduction instructions.

Maybe through using Py-Maker you have an idea of your own or are looking for
something in the documentation and thinking ‘this can be improved’...you can do
something about it!

As contributors and maintainers to this project, you are expected to abide by
our code of conduct. More information can be found at: [Contributor Code of
Conduct](https://github.com/seapagan/py-maker/blob/main/CODE_OF_CONDUCT.md)

## License

This project is licensed under the terms of the MIT license.

```pre
MIT License

Copyright (c) 2023 Grant Ramsay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


```
