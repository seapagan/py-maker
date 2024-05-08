# Future Plans

The below is a list of things I'd like to add to the project in the future, and
is kinda a 'work list' for me.

Everything below will be implemented and are in no particular order or
importance.

## General

- Add a flag to overwrite existing files if the directory exists. Make this
  require confirmation. Alternately allow overwrite with confirmation if an
  existing/populated directory is found. Add a force flag to skip confirmation.
  `I think DO NOT allow this when '.' is specified as this could be disastrous`.
- Add cmd line options to specify the project name, author, etc. so the user
  doesn't have to enter them manually. `Not sure if this is needed once we add
  the CLI parameters to the config file. May be useful for automation though`.
- Add a command to the CLI template command to show the template files as a
  tree, marking whether each file/folder is from the internal templates or the
  user's templates.
- Implement a 'plugin' functionality where we can specify modified/extra files
  to be added to the generated project. This would also add a command line flag
  (ie `--django`, `--pydantic` or `--fastapi` or whatever) to use that plugin,
  and a config setting to specify using this plugin always. Plugins could be
  built-in (provided with the package) or user-defined (in the users
  `/pymaker/plugins` folder or installable via pip). Have a config setting to
  specify which plugins are enabled.
- Include an optional `vscode` settings file in the generated project, optimized
  for python projects. This could include recommended extensions.
- Perhaps add AUTHORS.md skeleton.
- Add a default dockerfile? Maybe a docker-compose file as well- Both for this
  project and for the generated projects?
- Update the `config` CLI command to enable setting/flipping individual config
  settings from the command line.
- check for an existing GitHub repository when the user supplies the repo name
  and ask for an alternative if it exists.
- add option (probably using the eventual plugin functionality) to create a
  skeleton `typer` CLI app.
- if it creates a new remote GitHub repo, print the GitHub URL to the console,
  offer to open it in the browser.
- when creating a github repo, set the homepage if specified. Options to add
  tags? Offer option to create a private repo?
- add ability to add new licences to the `licenses` module. Perhaps similar to
  the way we modify the templates. This will need a bit of refactoring to the
  way we handle licences.

## Bugs

- None known at this time.

## Back Burner

These are ideas that I may or may not implement. They are here for reference.

- Modify boolean settings in the config to have the values 'yes', 'no' or 'ask'?
  This will be a bit lower priority and not sure if it's worth it.
- Add some form of 'extra packages' command line option and config setting to
  automatically add extra packages to the generated `pyproject.toml` file.
- Add template GitHub workflows for CI/CD, testing, etc. CodeQL or is that too
  much (I do use it in most of my repos)?
- Add the `actions/stale` action to the generated project.

## Refactoring / Code Cleanup

- None planned at this time.

## Documentation

- Add usage examples and perhaps a walk-through to the documentation. Maybe
  with a YouTube video?
- explain how to add more License templates to the 'licenses' module

## Testing

- Add testing with [Pytest](https://pytest.org) (`IN PROGRESS`)
