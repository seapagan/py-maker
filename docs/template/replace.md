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
the default template. If you answer yes, then the default template will be
disabled, and ONLY the exported template will be used instead. Otherwise, both
will still be used with the exported template taking precedence.

## Use another Template completely

!!! note
    This feature is not yet implemented.

## Choose to use the Default Template or not

Running the `dump` command will give you the option to disable the default
template completely and ONLY use the exported template. You can also do this (or
revert back to the default template) by running the following command:

```console
$ pymaker template default <enable|disable>
```

`enable` will enable the default template, and `disable` will disable it. Please
note that any custom templates you have created will still be used, and will
overwrite the default template if they have the same file name.
