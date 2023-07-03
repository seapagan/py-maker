# Py-Maker <!-- omit in toc -->

This is a command line tool to help you create new Python projects.  It will
create a new directory for your project, initialise a git repository, create a
virtual environment, and install some basic dependencies.

More functionality will be added very shortly and the code will be refactored
and cleaned up.

- [Installation](#installation)
- [Usage](#usage)
  - [Customise](#customise)
  - [Linting](#linting)
  - [Pre-commit](#pre-commit)
- [License](#license)

## Installation

It is probably better to install this package globally, rather than in a virtual
environment, as it is intended to be used to create new projects.

Install the package globally using pip:

```console
$ pip install py-maker
```

If you cannot install globally due to permissions, you can install it to your
user install directory:

```console
$ pip install --user py-maker
```

or use [pipx](https://pypa.github.io/pipx/)

```console
$ pipx install py-maker
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

You should now change into the new directory, install dependencies and activate
the virtual environment:

```console
$ cd <project-folder>
$ poetry install
$ poetry shell
```

### Customise

The `pyproject.toml` file is set up to use `App` as the main source directory,
which is the default for this template, you can change this to whatever you
require, just remember to update the `pyproject.toml` file to match.

### Linting

The generated project includes [flake8](https://flake8.pycqa.org/en/latest/) for
linting and [Black](https://black.readthedocs.io/en/stable/) for formatting.
[Mypy](http://mypy-lang.org/) is installed for type checking.
[isort](https://pycqa.github.io/isort/) and [Pylint](https://pylint.org/) are
also installed as standard.

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
