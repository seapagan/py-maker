# Configuration

## Configuration file

This app needs minimal configuration, most options default to `True`. The
configuration is stored in a `TOML` file in a sub-folder of the user's
home directory. By default (and currently the only option) this file is stored
in `~/.pymaker/config.toml`. An example of this file is:

```toml
[pymaker]
author_email = "user@server.com"
author_name = "Python User"
default_license = "MIT"
github_username = "githubuser" # optional
github_token = "ghp_1234567890abcdefghij" # optional
github_protocol = "ssh"
include_linters = true
include_mkdocs = true
include_testing = true
install_pre_commit = true
schema_version = "1.0" # for internal use, generally don't change this
template_folder = "/home/user/.pymaker/template"
use_default_template = true
use_git = true
create_remote = true
```

If this file does not exist, it will be created on first run. The app will ask
for the values of `author_name`, `author_email`, `default_license` and
`github_username`. For `author_name` and `author_email` it will try to use the
current global git user name and email if they are set as defaults, though the
user can override these.

## Configuration options

The following options are available for configuring Py-Maker:

- `author_email`: The email address of the author.
- `author_name`: The name of the author.
- `default_license`: The default license to use for the project.
- `github_username`: The GitHub username of the author [optional].
- `github_token`: The GitHub Personal Access Token of the author [optional]. See
  [below](#add-a-github-personal-access-token) for more information.
- `github_protocol`: The protocol to use for GitHub, either `ssh` or `https`,
  defaults to **`ssh`** which means that the user will need to have set up an
  SSH key with GitHub and added it to their account. If you wish to use HTTPS,
  you will be asked for your GitHub password every time you push to the remote
  repository.
- `include_linters`: Whether to include linters in the project, defaults to
  **`true`**
- `include_mkdocs`: Whether to include MkDocs in the project, defaults to
  **`true`**
- `include_testing`: Whether to include testing in the project, defaults to
  **`true`**
- `install_pre_commit`: Whether to install pre-commit hooks, defaults to
  **`true`**
- `schema_version`: The version of the configuration schema. **This should not
  be modified by hand**. Currently, and until version 1.0 is released, this is
  set to "none" to indicate that the schema is not yet stable.
- `template_folder`: The path to the template folder.
- `use_default_template`: Whether to use the default template, defaults to
  **`true`**
- `use_git`: Whether to use Git for version control, defaults to
  **`true`**
- `create_remote`: Whether to create a remote repository on GitHub, defaults to
  **`true`**

All of the boolean options are set to **`true`** by default. The
`template_folder` is set to the default template folder, which is
`~/.pymaker/template`. The `schema_version` is for internal use, and should not
be changed by the user.

## View configuration

You can list the current configuration with the command:

```console
$ pymaker config show
```

## Edit the configuration file

You can edit the configuration file with the command:

```console
$ pymaker config edit
```

This will open the configuration file in your default editor. Under linux it
will try to use `xdg-open` to open the file, and if that fails, it will try to
use a few different editors until it finds one that works. Under Windows and Mac
it will try to use the default editor.

You may also edit the configuration file manually, by default it is stored in
`~/.pymaker/config.toml`.

## Set configuration

The configuration is set the first time you run the app, but you can change
these defaults at any time using the command:

```console
$ pymaker config change
```

The latter command will prompt you for the values of `Author name`, `Author
Email`, `Default License` and `GitHub Username`, then update the configuration
file.

## Add a GitHub Personal Access Token

This app is able to create a new GitHub repository for you. To do this, it will
need a GitHub Personal Access Token. You can create a new token by going to
[GitHub Personal Access
Tokens](<https://github.com/settings/tokens>){:target="_blank"} and clicking on
the "Generate new token" button. Use the 'Classic' token option unless you
really need more control. **Unless you want to use the token on Private
repositories, you should check the `public_repo` option and leave all the other
permissions unchecked** (this tool does not yet have the option to create a
private repository). Give it a name (for your reference only) and chose an
expiry date. You can choose never to expire, but this is not recommended. Once
you have created the token, copy it (it will only be shown once, so make sure
you copy it now). Then run the command:

```console
$ pymaker config token
```

This will accept the token and store it in the configuration file. You can
change the token at any time by running the same command again.

!!! danger "NEVER PUSH THE CONFIG FILE TO A REPOSITORY!!!"

    This shouldnt ever happen since the file is stored in the user's home
    directory, but it is worth mentioning. If you didn't choose any extra
    permissions, then the worst that can happen is that someone can use your
    token to create a new repository. This token is READ-ONLY, so it can't be
    used to do anything malicious, but it is still a good idea to keep it secret.

## Manually editing the configuration file

The configuration file is stored in TOML format, and can be edited manually if
you wish. The file is stored in `~/.pymaker/config.toml` by default. The
configuration file is created on first run, so if you have not run the app yet,
you will need to create the file manually.
