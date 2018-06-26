- Date : 2018-06-26
- Tags : #git #github

## Running git command using another ssh key

Sometimes you want to use another private key to authorize to remote repository.

Just add an environment variable before the command you wanna run : `GIT_SSH_COMMAND='ssh -i [your-private-key]`

Example :

```bash
$ GIT_SSH_COMMAND='ssh -i ~/keys/key1' git pull
```

