- Date : 2017-08-06
- Tags : #sysadmin #linux #kernel

## Cleaning up old linux kernels

Last day, I try to reboot a production server which has out-of-space /boot (I upgraded many kernels without rebooting, so system doesn't clean up old ones). And in the end, doom day had come ! It installed new kernel failed and booting to that kernel. My system crashed !

So, I learned from it :

- Never ever upgrade kernel without cleaning up old ones (just reboot)
- Never ever reboot a production without backup
- MORE IMPORTANT, NEVER do 2 above things at same time in the weekend !!!

**Solution** :

- Check current kernel : `uname -r`
- List all kernels : `dpkg --list | grep linux-image `
- Remove a kernel : `sudo apt-get purge linux-image-x.x.x-x-generic`
- Finally, update grub after removing all old kernels : `sudo update-grub2`

- YOLO command for DEBIAN distros (to remove all of old kernels in 1 line), from [AskUbuntu](https://askubuntu.com/a/254585)

```bash
dpkg --list | grep linux-image | awk '{ print $2 }' | sort -V | sed -n '/'`uname -r`'/q;p' | xargs sudo apt-get -y purge
```

THEN, `sudo reboot`
