- Date : 2019-11-23
- Tags : #javascript #json #web #performance

## JSON Parse is faster than Javascript Object declaration

**TLDR;**

Use `JSON.parse("[your data in json string]")` if your data is big (>10KB for instance)

**Short Explaination :**

`JSON.parse` parses a string to object, so it has many strict requirements than Javascript parses the source code (more syntax, more context)

**Long Explaination :**

https://www.youtube.com/watch?v=ff4fgQxPaO0

{% youtube ff4fgQxPaO0 %}

