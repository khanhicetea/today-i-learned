- Date : 2017-09-27
- Tags : #linux #keyboard

## Send ENTER key to kernel

When you try to send an Enter keyboard to linux kernel, it looks like nothing happens.

This is because you only send a key press (KEY DOWN) but don't send an key release (KEY UP) event after that.

