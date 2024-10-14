- Date : 2024-10-14
- Tags : #crypto #electronjs #security

## Storing master key inside MacOS keychain

Today, I read the source of Chromium, then see it implement the encryption data is so easy to understand.

Because all of encryption needs "THE KEY", so each security layer, it has to have the master key. Chromium has one to, all its encrypted data using the same master key, store inside the OS "keychain" (macOS keychain, Windows DAPI, ...). The first boot time, the app generate its master key, then next boot, it loads the key from Keychain and store in process memory, and use this key to encrypt and decrypt all the data it wants.

Then I checked the source and a bit suprise about the master key is only 128bits. I thought nowaday, at least 256 bits needed because computation powers. But I'm wrong, 128bits is safe enough this century (read this : https://hackernoon.com/is-128-bit-encryption-enough-cp2i3aoy )

