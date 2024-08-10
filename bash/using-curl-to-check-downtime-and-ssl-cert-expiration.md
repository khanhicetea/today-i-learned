- Date : 2024-08-10
- Tags : bash curl devops downtime

## Using Curl to check downtime and ssl cert expiration

Before I wrote a [cron script](/til/2024-04-12-cronjob-monitoring-web-endpoint-and-alert-to-telegram/) to check website is down, but it can't check multiple endpoint and can't alert if ssl certificates is about to expired.

So, I created this bash snippet function to check multiple endpoints (and their SSL certificates)

```bash
#!/bin/bash

function checkEndpoint() {
    URL="$1"
    FIND="$2"

    RESPONSE=$(curl -m 10 -s "$URL")
    CONTENT=$(echo $RESPONSE | grep "$FIND")

    if [ $? -ne 0 ]; then
        echo "Error: $URL same down. Please check!"
        return 1
    fi

    # Check SSL certificate expiration
	HOST=$(echo "$URL" | sed -E 's|https?://([^/]+).*|\1|')
    EXPIRY_DATE=$(echo | openssl s_client -connect "$HOST:443" -servername "$HOST" 2>/dev/null | openssl x509 -noout -enddate | cut -d= -f2)
    EXPIRY_TIMESTAMP=$(date -d "$EXPIRY_DATE" +%s)
    CURRENT_TIMESTAMP=$(date +%s)
    DAYS_LEFT=$(( (EXPIRY_TIMESTAMP - CURRENT_TIMESTAMP) / 86400 ))

    if [ "$DAYS_LEFT" -le 7 ]; then
        echo "Error: $URL - SSL certificate will expire in $DAYS_LEFT days."
        return 1
    fi

    return 0
}

function checkAndAlert() {
	CHAT_ID="telegram_chat_id"
	BASIC_AUTH_BOT_PARAM="bot*****:*********"
    ALERT_MSG=$(checkEndpoint "$1" "$2")

    if [ $? -ne 0 ]; then
		curl -s -m 10 --get --data-urlencode "chat_id=$CHAT_ID" --data-urlencode "text=$ALERT_MSG" "https://api.telegram.org/$BASIC_AUTH_BOT_PARAM/sendMessage"
        return 1
    fi
}

checkAndAlert "https://google.com/" "google"
checkAndAlert "https://news.ycombinator.com" "Hacker News"
```

