# Quick Start

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

When it asks "Package Name?" you can choose two variants :

1. **If you are creating a standard Python package** that can optionally be
   uploaded to **PyPI**, enter a package name here. Note that underscores ("_")
   must be used as opposed to dashes ("-") to comply with Python package naming
   rules. Default is the project folder name with underscores replacing dashes.
2. **For a stand-alone tool** that will not ne uploaded to PyPI, or is not a
   library, enter '-' for the package name. In this case the `main.py` will just
   be placed in the project root and no package folder will be created or
   referenced.

You should now change into the new directory, install dependencies and activate
the virtual environment:

```console
$ cd <project-folder>
$ poetry install
$ poetry shell
```

Now, you can start developing :smile:

Example run :

```console
$ pymaker new test-project
PyMaker - Generate a Python project skeleton.

Creating a new project at /home/bathroom/test-project

Name of the Application? (Test Project):
Package Name? (Use '-' for standalone script) (test_project):
Description of the Application?: An amazing Bigly test project. better than you've ever seen before!
Author Name? (Orange Tango):
Author Email? (bigly@spraytan.org):
Application License? [None/Apache2/BSD3/BSD2/GPL2/GPL3/LGPL/MIT/MPL2/CDDL/EPL2] (MIT):

Creating a New Python app with the below settings :

    Description : An amazing Bigly test project. better than you've ever seen before!
   Package Name : test_project
         Author : Orange Tango
          Email : bigly@spraytan.org
        License : MIT
    Project Dir : /home/bathroom/test-project
           Name : Test Project

Is this correct? [y/n] (y): y

--> Creating project folder ... Done
--> Creating Git repository ... Done

--> Project created successfully.

Next steps:

    1) Change to the project directory:
    2) Install the dependencies (creates a virtual environment):
        'poetry install'
    3) Activate the virtual environment:
        'poetry shell'
    4) Run the application:
        'test-project'
    5) Code!

See the README.md file for more information.
```
