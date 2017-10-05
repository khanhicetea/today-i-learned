- Date : 2017-10-05
- Tags : #bash #python

## Simple HTTP server function helper

I use python3 (3.4+) to create a bash function to help me start quickly a simple http server on specified port

```bash
function server() {
  local port="${1:-8000}" # Getting port number
  google-chrome "http://127.0.0.1:$port" # Open URL in browser, could change to firefox --new-tab "http://127.0.0.1:$port"
  python3 -m http.server $port --bind 127.0.0.1
}
```

