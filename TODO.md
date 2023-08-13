# TODO List

## General

- Add testing with [Pytest](https://pytest.org) (`IN PROGRESS`)
- Add option to generate a skeleton MkDocs website for the new project
- Ask for more settings ie homepage, repo, etc. and add them to the generated
  `pyproject.toml` file (if the new project is likely to be uploaded to PyPI)
- check manually entered package name to ensure no dashes.
- add a flag to overwrite existing files if the directory exists. Make this
  require confirmation. Alternately allow overwrite with confirmation if an
  existing/populated directory is found. Add a force flag to skip confirmation.
  I think DO NOT allow this when '.' is specified as this could be disastrous.
- when creating a package project, quickly check PyPI to see if the package name
  is already taken. If it is, either abort or ask the user if they want to
  continue (making clear they will need to rename the package before it can be
  uploaded).
- add some form of 'extra packages' command line option and config setting to
  automatically add extra packages to the generated `pyproject.toml` file.
- add cmd line options to specify the project name, author, etc. so the user
  doesn't have to enter them manually.
- add a command line option to specify the project type so the user doesn't have
  to enter it manually. ie `--standalone` or `--package`(latter is default and
  wouldn't need to be specified).
- add a command to the CLI template command to show the template files as a
  tree, marking whether each file/folder is from the internal templates or the
  user's templates.
- add some sort of 'plugin' functionality where we can specify modified/extra
  files to be added to the generated project. This would also add a command line
  flag (ie `--django`, `--pydantic` or `--fastapi` or whatever) to use that
  plugin, and a config setting to specify using this plugin always.
- add config  and CLI options to enable/disable creating a `git` repo, disable
  adding `test` or `linting` packages etc (expand for any future options).

## Documentation

- Add usage examples and perhaps a walk-through to the documentation. Maybe
  with a YouTube video?
