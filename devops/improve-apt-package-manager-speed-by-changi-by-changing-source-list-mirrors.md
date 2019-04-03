- Date : 2019-04-03
- Tags : #devops #apt #packagemanager

## Improve apt package manager speed by changi by changing source list mirrors

Sometimes, you ran into issues that apt update package list so slow or even can not connect to the destination server.

You can change the default list into new one near your country. Get example : if you live in ASIA, choose the Singapore or Japan mirror instead of main mirror. you just change the "archive.ubuntu.com" and "security.ubuntu.com" to "[country_code].archive.ubuntu.com" in file list `/etc/apt/sources.list`

Then run `sudo apt update` to test your new mirror :)

