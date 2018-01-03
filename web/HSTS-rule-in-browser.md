- Date : 2018-01-03
- Tags : #web #security

## HSTS rule in browser

HTTP Strict Transport Security (HSTS) is a web security policy mechanism which helps to protect websites against protocol downgrade attacks and cookie hijacking.

Enabling HSTS on your web will make your browser validate every SSL issues more strictly :

- User can not visit http version on browser
- User can not add SSL exception for the domain to ignore the warning. (when SSL cert expire or invalid common name)

Note : You can manually remove a domain from HSTS in Chrome by accessing this page URL `chrome://net-internals/#hsts`

> So remember to add HSTS to your website !

