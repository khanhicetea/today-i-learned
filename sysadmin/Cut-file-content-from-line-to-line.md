- Date : 2018-03-25
- Tags : #sysadmin #file #string

## Cut file content from line to line

In case you have a big file which contains a lot of content (2+ GB). And you only need a small part from the file (the part is continuous string from line X to line Y).

You have many ways to achieve that :

1. Use `vi` editor and delete from line 1 to line (X-1) by press `[X-1]dd` then go to line (Y-X+2) and delete to last line by press `dG`
2. Use `sed -n '[X][Y]p' [input_file] > [output_file]`. Example : `sed -n '15,68p' a.sql > b.sql`
3. Use `head` and `tail` trick : `head -n[Y] [input_file] | tail -n[Y-X+1] > [output_file]`

I personally recommend using the `sed` way, it's faster and simpler to remember.

