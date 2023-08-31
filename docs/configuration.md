# Configuration

## Configuration file

This app needs minimal configuration, currently just storing defaults for the
`author_name`, `author_email` and `default_license`. This is stored in a
configuration file in a sub-folder of the user's home directory. By default (and
currently the only option) this file is stored in `~/.pymaker/config.toml`. An
example of this file is:

```toml
[pymaker]
author_email = "user@server.com"
author_name = "Python User"
default_license = "MIT"
include_linters = true
include_mkdocs = false
include_testing = true
schema_version = "1.0" # for internal use, generally don't change this
template_folder = "/home/user/.pymaker/template"
use_default_template = true
use_git = true
```

If this file does not exist, it will be created on first run. The app will ask
for the values of `author_name`, `author_email` and `default_license`. For
`author_name` and `author_email` it will try to use the current git user name
and email if they are set as defaults, though the user can override these.

## View configuration

You can list the current configuration with the command:

```ini
$ pymaker config show
```

## Set configuration

The configuration is set the first time you run the app, but you can change
these defaults at any time using the command:

```console
$ pymaker config change
```

The latter command will prompt you for the values of Author name, email and
default License, and then update the configuration file.
