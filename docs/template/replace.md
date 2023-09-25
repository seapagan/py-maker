# Replacing the Default Template

## Dump the Default Template

Should you wish to heavily modify the default template, or even replace it
completely, you can do so by dumping the default template to the
`~/.pymaker/template` folder. This will copy all files from the default template
to the global template folder, where you can modify or delete them as you see
fit.

To do this, run the following command:

```console
$ pymaker template dump
```

This will copy the default template to the global template folder
(`~/.pymaker/template`). You can then modify or delete files as you see fit.

Running this command will ask you if you wish to set this exported template as
the default template. It will then ask you if you want to disable the internal
template. If you answer yes, then the internal template will be
disabled, and ONLY the exported template will be used instead. Otherwise, both
will still be used with the exported template taking precedence.

## Change the location of the Template folder

If you wish to change the location of the template folder, you can do so in 2
ways:

1. By adding the `--local` flag to the above command (e.g. `pymaker template
   dump --local`). This will dump the default template to the current folder,
    giving you the option to disable the default template if needed. Note that
    any files in the folder will be overwritten.
2. By changing to the folder containing your template and running `pymaker
   template set`. This will set the current folder as the template folder and
   give you the same option to disable the default template.

You can reset the template location back to the default `~/.pymaker/template`
folder by running the following command:

```console
$ pymaker template reset
```

## Choose to use the Default Template or not

Running the `dump` command will give you the option to disable the default
template completely and ONLY use the exported (or custom) template. You can also
do this (or revert back to the default template) by running the following
command:

```console
$ pymaker template default <enable|disable>
```

`enable` will enable the default template, and `disable` will disable it. Please
note that any custom templates you have created will be used regardless, and
will overwrite the default template (if enabled) if they have the same file
name.
