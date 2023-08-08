# Replacing the Default Template

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
