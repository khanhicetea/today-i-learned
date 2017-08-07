- Date : 2017-08-07
- Tags : #linux #keyboard

## Remap Capslock to Control key

Edit file `/etc/default/keyboard` and set 

```
XKBOPTIONS="ctrl:nocaps"
```

Then, logout and log in again to impact

