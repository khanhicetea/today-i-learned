- Date : 2017-09-25
- Tags : #tools #zip #compress

## Zip compressing list of files

To specify a list of compressed files when using **zip** cli tool, you could use `-@ [file_list]` flag. And `file_list` is a file contains list of compressed file (new line separated)

Example

```bash
$ zip changed.zip -@ changed_files.txt
```

Or use stdin pipe

```bash
$ find . -mmin -60 -print | zip changed_1_hour_ago -@
```

This will zip all changed files 1 hour ago

