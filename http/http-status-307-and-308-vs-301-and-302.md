- Date : 2023-08-20
- Tags : #http #redirect #web

## HTTP Status Codes : 301+302 vs 307+308

- HTTP 307 : Temporary redirect, keep METHOD and BODY
- HTTP 308 : Permanent redirect, keep METHOD and BODY

vs

- HTTP 301 : Permanent redirect, fallback to GET method
- HTTP 302 : Temporary redirect, fallback to GET method
