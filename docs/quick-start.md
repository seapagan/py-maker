# Quick Start

## Create a new project

To create a new project, run the following command:

```console
$ pymaker new <project-folder>
```

This will create a new directory with the name you provide.

You can create a new project in the current directory by using `.` as the
project folder name. This must be an empty directory:

```console
$ mkdir test-project
$ cd test-project
$ pymaker new .
```

The App will then run the steps needed to get you started quickly:

1. Copy the template files into the new directory
2. Initialise a git repository
3. Commit the boilerplate to Git

You will be asked a series of questions to customise the new project.

## Choose a package name and description

When it asks "Package Name?" you can choose two variants :

1. **If you are creating a standard Python package** that can optionally be
   uploaded to **PyPI**, enter a package name here. Note that underscores ("_")
   must be used as opposed to dashes ("-") to comply with Python package naming
   rules. Default is the project folder name with underscores replacing dashes.
2. **For a stand-alone tool** that will not be uploaded to PyPI, or is not a
   library, enter '-' for the package name. In this case the `main.py` will just
   be placed in the project root and no package folder will be created or
   referenced.

## Choose to create an MkDocs site or not

If you answer "y" to the question "Use MkDocs for documentation?", then the app
will create a new MkDocs site in the `docs` folder, and will add the
`mkdocs-material` theme to the `mkdocs.yml` file along with a few other useful
plugins and markdown extensions.

## Command line options

There are a few command line options that can be used to customise the build

### `--no-git`

This will skip the step of initialising a git repository.

### `--no-test`

This will skip the step of creating a test directory, and will not add the
`pytest` dependency or any related plugins to the `pyproject.toml` file.

### `--no-lint`

This will skip adding any linting dependencies to the `pyproject.toml` file, nor
will it add any linting configuration options or related tasks.

## Run `poetry install` automatically

You will be asked if you want to run `poetry install` automatically. This will
create a virtual environment and install the dependencies, plus also create a
bare `MkDocs` site and configuration. This is the recommended option.

You will still need to run `poetry shell` to activate the virtual environment
from inside the new project folder.

## Start developing

You should now change into the new directory, install dependencies and activate
the virtual environment:

```console
$ cd <project-folder>
$ poetry install # if not done automatically already
$ poetry shell
```

Now, you can start developing :smile:

## Example run

```console
$ pymaker new secret-docs
PyMaker - Generate a Python project skeleton.

Creating a new project at /home/bathroom/secret-docs

Name of the Application? (Secret Docs):
Package Name? (Use '-' for standalone script) (secret_docs):
Description of the Application?: Store all the Bigly amount of secret documents
I have in the bathroom

Author Name? (): Orange Tango
Author Email? (): bigly@straytan.org
Application License? [None/Apache2/BSD3/BSD2/GPL2/GPL3/LGPL/MIT/MPL2/CDDL/EPL2] (MIT):
Use MkDocs for documentation? [y/n] (y):

Creating a New Python app with the below settings :

    Description : Store all the Bigly amount of secret documents I have in the
                  bathroom
   Package Name : secret_docs
         Author : Orange Tango
          Email : bigly@straytan.org
        License : MIT
     Use Mkdocs : True
    Project Dir : /home/bathroom/secret-docs
           Name : Secret Docs
     Standalone : False

Is this correct? [y/n] (y):

--> Creating project folder ... Done

Should I Run 'poetry install' now? [y/n] (y):
Creating virtualenv secret-docs in /home/bathroom/secret-docs/.venv
Updating dependencies
Resolving dependencies... (11.6s)

Package operations: 103 installs, 1 update, 0 removals

  • Installing lazy-object-proxy (1.9.0)
  • Installing six (1.16.0)

            <snippy snip>

  • Installing pytest-xdist (3.3.1)
  • Installing tryceratops (2.3.2)

Writing lock file

Installing the current project: secret-docs (0.1.0)

--> Creating MkDocs project
INFO    -  Writing config file: ./mkdocs.yml
INFO    -  Writing initial docs: ./docs/index.md

--> Creating Git repository ... Done

--> Project created successfully.

Next steps:

1. Change to the project directory:
2. Install the dependencies if not done (creates a virtual environment):
  'poetry install'
3. Activate the virtual environment:
  'poetry shell'
4. Run the application:
  'secret-docs'
5. Code!

See the README.md file for more information.
```
