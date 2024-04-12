- Date : 2024-04-12
- Tags : #devops #monitoring #telegram #bash

## Cronjob monitoring web endpoint and alert to Telegram

This is shell script using `curl` and `grep` to send request then check if the keyword (FIND) include in the response text body. If failed, try to alert

```bash
URL="https://news.ycombinator.com/"
FIND="Hacker News"

response=$(curl -m 10 -s "$URL")
content=$(echo $response | grep "$FIND")

if [ $? -eq 0 ]; then
	echo "OK!"
	exit 0
fi

# Do watever you want to alert
CHAT_ID="telegram_chat_id"
TEXT="The web is down !"
BASIC_AUTH_BOT_PARAM="bot*****:*********"

curl -s -m 10 --get --data-urlencode "chat_id=$CHAT_ID" --data-urlencode "text=$TEXT" "https://api.telegram.org/$BASIC_AUTH_BOT_PARAM/sendMessage"
exit 1
```
