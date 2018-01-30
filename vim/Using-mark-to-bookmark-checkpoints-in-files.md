- Date : 2018-01-30
- Tags : #vim #editor

## Using mark to bookmark checkpoints in files

Bookmarking a checkpoint will help you get back to it intermidately. Ex: your have to find some text to replace something but want to return back current position. 

**Set a mark**
- [NORMAL MODE] , type `m` then follow by a letter from a-z (lowercase is filescope, uppercase for global scope - vim scope)

**Go to a mark**
- [NORMAL MODE] , type backstick ` then follow by the letter your marked above.

**List all current marks**
- [NORMAL MODE], `:marks`

**TIPS** : Can use it as a motion with `c`hange, `d`elete or `y`ank