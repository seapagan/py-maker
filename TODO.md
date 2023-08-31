# Future Plans

The below is a list of things I'd like to add to the project in the future, and
is kinda a 'work list' for me.

Everything below will be implemented and are in no particular order or
importance.

## General

- Ask for more settings ie homepage, repo, etc. and add them to the generated
  `pyproject.toml` file (if the new project is not standalone).
- add a flag to overwrite existing files if the directory exists. Make this
  require confirmation. Alternately allow overwrite with confirmation if an
  existing/populated directory is found. Add a force flag to skip confirmation.
  `I think DO NOT allow this when '.' is specified as this could be disastrous`.
- add some form of 'extra packages' command line option and config setting to
  automatically add extra packages to the generated `pyproject.toml` file.
- add cmd line options to specify the project name, author, etc. so the user
  doesn't have to enter them manually. `Not sure if this is needed once we add
  the CLI parameters to the config file. May be useful for automation though`.
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
- modify boolean settings in the config to have the values 'yes', 'no' or 'ask'?
  This will be a bit lower priority and not sure if it's worth it.
- include an optional `vscode` settings file in the generated project, optimized
  for python projects. This could include recommended extensions.

## Code Quality

- refactor the `PyMaker` class as its getting a bit messy. Maybe split it into
  multiple classes with specific responsibilities.
- sort out the nested `if/else` statements in
  `PyMaker.get_sanitized_package_name`.

## Documentation

- Add usage examples and perhaps a walk-through to the documentation. Maybe
  with a YouTube video?

## Testing

- Add testing with [Pytest](https://pytest.org) (`IN PROGRESS`)
