- Date : 2018-05-17
- Tags : #crypto #encrypt #decrypt

## Encrypt and decrypt file using openssl command line

You can encrypt and decrypt the file using openssl command line. Somehow you will need to encrypt your important file with a secret key.

**Encrypt**

```bash
openssl enc -aes-256-cbc -in [input_file] -out [output_file]
```

Then Enter 2 times your secret key (this should be hard to guess and don't loose it)

**Decrypt**

```bash
openssl enc -aes-256-cbc -d -in [input_file] > [output_file]
```

Then enter your secret key to decrypt the content !

*Notice : should use a 10-char length secret with alpha nums and special characters*

