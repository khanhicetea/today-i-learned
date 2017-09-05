- Date : 2017-09-05
- Tags : #sysadmin #grep

## Grep : find a string in folder

Grep is a greate tool for searching a string in files.

**Syntax**

```bash
$ grep -nr '[string]' [folder]
```

If you want to show surrounding lines the result, add flag `-C [number]` to the command

```bash
$ grep -nr -C 3 'hello' src
```

