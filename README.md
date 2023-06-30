# Basic Python project shell <!-- omit in toc -->

This repository is a template for a basic Python project using
[Poetry](https://python-poetry.org/), with assorted Linting and Testing
libraries installed as standard. It also uses
[pre-commit](https://pre-commit.com/)

I will tweak and update this as I see the need in my own coding use, and also
welcome suggestions and pull requests.

Shortly this will be converted into an installable package with a command line
that can be used to create a new project from the template at will.

- [Installation](#installation)
  - [Dependencies](#dependencies)
  - [Customise](#customise)
  - [Pre-commit](#pre-commit)
- [License](#license)

## Installation

You can clone this repo (or click the `Use this Template` button to
automatically create a new GitHub repository based on this) and use it as a
template for your own projects.

> In the former case, remember to delete the `.git` directory and re-initialise
> as a new repository. You don't need to do this if you use the `Use this
> Template` button.

### Dependencies

Install the dependencies using Poetry:

```console
$ poetry install
```

Then, activate the virtual environment:

```console
$ poetry shell
```

### Customise

You should now customise the project to your own needs.  At the very least,
you'll want to change the name of the project in `pyproject.toml` and the
`README.md` file, your name and email address in the `LICENSE` file, and in the
`pyproject.toml` file. Please do not remove the license file, or my header from
the `pyproject.toml` file.

Also if you don't like `App` as the main source directory, you can change that.
Just remember to update the `pyproject.toml` file to match.

### Pre-commit

This repo uses [pre-commit](https://pre-commit.com/) to run some checks on the
code before it is committed.  This is a great tool to help keep your code
clean.

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
