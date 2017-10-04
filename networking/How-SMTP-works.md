- Date : 2017-10-04
- Tags : #networking #smtp #mail

## How SMTP works

When a email send through an SMTP (with authentication), every SMTP server is a hop in mail routing. So it will transfer to localmail or forward the email to next hop (shortest distance via DNS MX record).

And standard port of SMTP is 25 (unsecured, but can upgrade to TLS via STARTTLS command).

```bash
$ nslookup -type=mx gmail.com 8.8.8.8
Server:         8.8.8.8       
Address:        8.8.8.8#53    

Non-authoritative answer:     
gmail.com       mail exchanger = 20 alt2.gmail-smtp-in.l.google.com.                                                    
gmail.com       mail exchanger = 5 gmail-smtp-in.l.google.com.                                                          
gmail.com       mail exchanger = 30 alt3.gmail-smtp-in.l.google.com.                                                    
gmail.com       mail exchanger = 10 alt1.gmail-smtp-in.l.google.com.                                                    
gmail.com       mail exchanger = 40 alt4.gmail-smtp-in.l.google.com.                                                    

Authoritative answers can be found from:
```

So shortest SMTP of gmail.com domain is `gmail-smtp-in.l.google.com`

```bash
$ telnet gmail-smtp-in.l.google.com 25
```

