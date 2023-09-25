
# Installation

It is best to install this package globally, rather than in a virtual
environment, as it is intended to be used to create new projects. Since we are
using [Poetry](https://python-poetry.org/){:target="_blank"} to manage the
dependencies, a virtual environment will be created for you anyway specific to
each project you are creating.

## Release Version

Install the package globally using pip:

```console
$ pip install pyproject-maker
```

If you cannot install globally due to permissions, you can install it to your
user install directory:

```console
$ pip install --user pyproject-maker
```

or use [pipx](https://pypa.github.io/pipx/){:target="_blank"} (recommended method)

```console
$ pipx install pyproject-maker
```

## Bleeding Edge Version

It is possible to install the latest development version of the package directly
from the repository. In most cases this should be safe to do, but it is possible
that the development version may not be stable or have bugs. If you are having
issues with the development version, please open an
[issue](https://github.com/seapagan/py-maker/issues){:target="_blank"} on the
repository.

Use pipx (recommended method):

```console
$ pipx install git+https://github.com/seapagan/py-maker
```

Using pip:

```console
$ pip install git+https://github.com/seapagan/py-maker
```

You can also use the `--user` flag for `pip` if you do not have permissions to
install globally. This is NOT needed for `pipx`.

Lastly, you can clone the repository and install from the local copy:

```console
$ git clone https://github.com/seapagan/py-maker
$ cd py-maker
$ pip install .
```
