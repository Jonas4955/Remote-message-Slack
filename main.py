import requests
import json

# Stores the url made available by creating the BOT with Incoming WebHooks.
URL_TOKEN = "https://hooks.slack.com/services/TOKEN_GENERATE_WEBHOOKS"

# Stores a dictionary with parameters interpreted by WebHooks for message display,
# styling, message structure, etc.
MESSAGE = {
    "attachments": [
        {
            "color": "warning",
            "fields": [
                {
                    "title": ":warning: Warning!!!",
                    "value": "Alert message!",
                }
            ]
        }
    ]
}


def main():
    requests.post(url=URL_TOKEN, data=json.dumps(MESSAGE))


if __name__ == "__main__":
    main()
