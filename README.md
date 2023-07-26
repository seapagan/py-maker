# Py-Maker <!-- omit in toc -->

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7c86940f816b455ab171dc8126476849)](https://app.codacy.com/gh/seapagan/py-maker/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

This is a command line tool to help you create new Python projects.  It will
create a new directory for your project, initialise a git repository, create a
virtual environment, and install some basic dependencies.

More functionality will be added very shortly and the code will be refactored
and cleaned up.

- [Installation](#installation)
- [Usage](#usage)
  - [Task Runner](#task-runner)
  - [Customise](#customise)
  - [Linting](#linting)
  - [Pre-commit](#pre-commit)
- [License](#license)

## Installation

It is probably better to install this package globally, rather than in a virtual
environment, as it is intended to be used to create new projects.

Currently the package is NOT on pypi so you need to install directly from this
repository:

Install the package globally using pip:

```console
$ pip install git+https://github.com/seapagan/py-maker.git
```

If you cannot install globally due to permissions, you can install it to your
user install directory:

```console
$ pip install --user git+https://github.com/seapagan/py-maker.git
```

or use [pipx](https://pypa.github.io/pipx/)

```console
$ pipx install git+https://github.com/seapagan/py-maker.git
```

## Usage

To create a new project, run the following command:

```console
$ pymaker new <project-folder>
```

This will create a new directory with the name you provide, and run the steps
needed to get you started quickly:

1) Copy the template files into the new directory
2) Initialise a git repository
3) Commit the boilerplate to Git

You will be asked a series of questions to customise the new project.

When it asks "Package Name?" you can choose two variants :

1) If you wish for a standard Python package that can optionally be uploaded to
   <http://pypi.org>, enter a package name here. Note that underscores ("_")
   must be used as opposed to dashes ("-") to comply with Python package naming
   rules.
2) Enter '-' to instruct the tool that you are not creating any package, just a
   standalone app, and then the `main.py` will just be placed in the project
   root.

You should now change into the new directory, install dependencies and activate
the virtual environment:

```console
$ cd <project-folder>
$ poetry install
$ poetry shell
```

Now, you can start developing :)

### Task Runner

The task-runner [Poe the Poet](https://github.com/nat-n/poethepoet) is installed
as a development dependency which allows us to run simple tasks (similar to npm
`scripts`).

These are run (from within the virtual environment) using the `poe` command and
then the script name, for example:

```console
$ poe pre
```

You can define your own, but there are 5 specific ones provided with the script.

- `pre` : Run `pre-commit run --all-files`
- `pylint`: Run Pylint on all Python files in the project.
- `mypy` = Run MyPy type-checker on all Python files in the project.
- `flake8` = Run Flake8 linter on all Python files in the project.
- `black` = Run Black code formatter on all Python files in the project.
- `try` = Run Tryceratops linter on all Python files in the project.

- `lint` = Runs pylint, mypy, flake8 and black in sequence

These are defined in the `pyproject.toml` file in the `[tool.poe.tasks]`
section. Take a look at this file if you want to add or remove tasks.

### Customise

The `pyproject.toml` file is set up to use `app` as the main source directory,
which is the default for this template, you can change this to whatever you
require, just remember to update the `pyproject.toml` file to match.

### Linting

The generated project includes [flake8](https://flake8.pycqa.org/en/latest/)
(with several plugins) for linting and
[Black](https://black.readthedocs.io/en/stable/) for formatting.
[Mypy](http://mypy-lang.org/) is installed for type checking.
[isort](https://pycqa.github.io/isort/),[Pylint](https://pylint.org/) and
[tyrceratops](https://github.com/guilatrova/tryceratops) are also installed as
standard.

### Pre-commit

The generated project uses [pre-commit](https://pre-commit.com/) to run some
checks on the code before it is committed.  This is a great tool to help keep
your code clean.

To install pre-commit, run the following command from inside your venv:

```console
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

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
