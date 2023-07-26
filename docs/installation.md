
# Installation

It is probably better to install this package globally, rather than in a virtual
environment, as it is intended to be used to create new projects. Since we are
using [Poetry](https://python-poetry.org/){:target="_blank"} to manage the
dependencies, a virtual environment will be created for you anyway specific to
each project you are creating.

Install the package globally using pip:

```console
$ pip install py-maker
```

If you cannot install globally due to permissions, you can install it to your
user install directory:

```console
$ pip install --user py-maker
```

or use [pipx](https://pypa.github.io/pipx/){:target="_blank"}

```console
$ pipx install py-maker
```
