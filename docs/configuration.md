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
github_username = "githubuser"
include_linters = true
include_mkdocs = true
include_testing = true
install_pre_commit = true
schema_version = "1.0" # for internal use, generally don't change this
template_folder = "/home/user/.pymaker/template"
use_default_template = true
use_git = true
```

If this file does not exist, it will be created on first run. The app will ask
for the values of `author_name`, `author_email` and `default_license`. For
`author_name` and `author_email` it will try to use the current git user name
and email if they are set as defaults, though the user can override these.

## Configuration options

The following options are available for configuring Py-Maker:

- `author_email`: The email address of the author.
- `author_name`: The name of the author.
- `default_license`: The default license to use for the project.
- `github_username`: The GitHub username of the author [optional].
- `include_linters`: Whether to include linters in the project.
- `include_mkdocs`: Whether to include MkDocs in the project.
- `include_testing`: Whether to include testing in the project.
- `install_pre_commit`: Whether to install pre-commit hooks.
- `schema_version`: The version of the configuration schema.
- `template_folder`: The path to the template folder.
- `use_default_template`: Whether to use the default template.
- `use_git`: Whether to use Git for version control.

All of the boolean options are set to `true` by default. The `template_folder`
is set to the default template folder, which is `~/.pymaker/template`. The
`schema_version` is for internal use, and should not be changed by the user.

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

## Add a GitHub Personal Access Token

In future versions, this app will be able to create a new GitHub repository for
you, and generate a CHANGELOG.md file. To do this, it will need a GitHub
Personal Access Token. You can create a new token by going to [GitHub Personal
Access Tokens](<https://github.com/settings/tokens>){:target="_blank"} and
clicking on the "Generate new token" button. Use the 'Classic' token option
unless you really need more control. Unless you want to use the token on Private
repositories, you can leave all the permissions unchecked. Give it a name (for
your reference only) and chose an expiry date. You can choose never to expire,
but this is not recommended. Once you have created the token, copy it (it will
only be shown once, so make sure you copy it now). Then run the command:

```console
$ pymaker config token
```

This will accept the token and store it in the configuration file. You can
change the token at any time by running the same command again.

!!! danger "NEVER PUSH THE CONFIG FILE TO A REPOSITORY!!!"

    This shouldnt ever happen since the file is stored in the user's home
    directory, but it is worth mentioning. If you didn't choose any extra
    permissions, then the worst that can happen is that someone can use your token
    to create a new repository. This token is READ-ONLY, so it can't be used to do
    anything malicious, but it is still a good idea to keep it secret.

## Manually editing the configuration file

The configuration file is stored in TOML format, and can be edited manually if
you wish. The file is stored in `~/.pymaker/config.toml` by default. The
configuration file is created on first run, so if you have not run the app yet,
you will need to create the file manually.
