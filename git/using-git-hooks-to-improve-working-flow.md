- Date : 2017-11-22
- Tags : #git #automation #workflow

## using git hooks to improve working flow

We can improve our team workflow by defining some git hooks that trigger on specified events.
You can read all events and their usecases here : https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks

This is what I implemented to my [today-i-learned](https://github.com/khanhicetea/today-i-learned) repo. I used pre-commit to update Table of Contents in the README.md file, so every content in my repo will be updated on Github repo page.

```bash
$ ln pre-commit .git/hooks/pre-commit
```

**pre-commit** file :

```bash
#!/bin/sh

echo 'Running pre-commit hook' 

python til_update_readme.py
git add README.md
```

So it will run a Python script that update new TOC and then add the file to git.

> Automation ! Automation ! AND .... Automation !!! 🤖 

