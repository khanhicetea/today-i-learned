- Date : 2018-03-14
- Tags : #ios #security #ssl

## Install CA root certificate on iOS device

**Disclaimer** : You can do it, but it's at your own risk !

Sometimes you want to accept a SSL firewall proxy or self-MITM proxy, the important step is installing its CA root certificate to your device. Because iOS apps almost use all https connections (that's new rule).

This is the way to install and enable custom CA Root cert :

- Step 1 : encode your certificate to binary-PEM (only need when you try `cat [ca-cert]` and see ASCII base64 characters)

```bash
openssl x509 -outform der -in [ca-cert] -out [new-ca-cert].crt
```

- Step 2 : Transfer the root certificate to your device (can use 1 of 2 methods : uploading cert to public webserver and open link in Safari app; or share certificate file through AirDrop - between 2 Apple devices). Tips : use `ngrok` as a simple tunnel webserver if you don't have AirDrop supported PC.

- Step 3 : Click Install on install profile screen

- Step 4 : Enable installed certificate, go to `Settings > General > About > Certificate Trust Settings > then switch On your certificate item. (You could disable it when you don't need it)

;) Check the web connection !

