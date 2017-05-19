- Date : 2017-05-19
- Tags : #devops #testing #bash #automated

## Checking forced push conflicts on source code in auto testing

Using automated CI solution likes Travis, Jenkins, DroneCI, ... is good solution to ensure quality of software and no breaks in deployment.

Sometimes, developers force push conflicts part to production branch of source code. If the CI tests only backend (python, ruby, php, go, ..) and forget about frontend code, then your application will be exploded !

So checking the conflicts code is required step before testing backend and deployment.

I used `grep` tool to checking conflicts code in current dir

Create a file name `conflict_detector.sh` in root dir of source code

```bash
#!/bin/bash

grep -rli --exclude=conflict_detector.sh --exclude-dir={.git,vendor,venv,node_modules} "<<<<<<< HEAD" .
```

Then mini tool print list of conflicted files. If exit code not equal 0 then testing will be failed !
