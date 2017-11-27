- Date : 2017-11-27
- Tags : #git #ci #automation

## Fastly conflict detector script

Last month, I built a CI solution for our project and adding a conflict detector to our build commands. This script runned so slow because it will check all application files (and our application codebase has many of css, js files).

This was the script

```bash
#!/bin/bash

grep -rli --exclude=conflict_detector.sh --exclude-dir={.git,vendor,node_modules} "<<<<<<< HEAD" .

if [ $? -eq 0 ]; then
    exit 1
else
    exit 0
fi
```

Today, I think why don't we just check recently updated files (in the latest commit) ??? Then I have this new script

```bash
#!/bin/bash

# New way :D
CHANGED_FILES=$(git log --pretty=format: --name-only HEAD^..HEAD | sort | uniq)

for f in $CHANGED_FILES
do
    if grep --exclude=conflict_detector.sh -q "<<<<<<< HEAD" $f
    then
        exit 1
    fi
done

exit 0
```

`conflict_detector.sh` is the filename of script, we exclude it from check to make sure changing this file doesn't make it failed.

**Result** :

- Old script : 12 seconds
- New script : ~ 50ms (200 times faster)

> be Automated, be Fast, but be Careful !

