# Adding or Modifying files in the template

If you wish to add or change specific files in the template, you can do so by
adding them to the `~/.pymaker/template` folder. The files (and folders) in this
folder will be copied to the root of the project when the template is generated.

Files in this global template folder will override any files in the default
template, so you can for example change the `README.md` file, add to the
`.gitignore` or even add a complete extra folder structure.

If you want to do a major change to the template, you can actually dump the
default template to this folder and modify or delete files as you see fit. See
the next section for more information on how to do this.
