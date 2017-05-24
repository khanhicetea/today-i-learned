- Date : 2017-05-24
- Tags : #docker #sysadmin

## Changing channel from alpha to stable will remove ALL DATA

On MacOS, changing Docker channel will remove all data (includes volumes, images, networks and ... everything).

Because Docker on Mac using a minimal Linux machine to host docker engine, so changing machine means discarding all old data. So BECAREFUL !

