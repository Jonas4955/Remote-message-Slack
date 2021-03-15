# Remote-message-Slack
The simple way to send external messages to Slack using the App "Incoming WebHooks".

This solution for sending messages to Slack consists of creating a BOT on the Slack platform itself, which can be linked to a specific channel.

We use Incoming WebHooks, which is an application created by Slack itself to facilitate external messaging.

As the WebHooks description indicates, it uses normal HTTP requests with a JSON payload, which includes the message and some other optional details.

We have created a BOT from WebHooks, learn more at (https://api.slack.com/legacy/custom-integrations#incoming-webhooks). WebHooks has generated a URL with a specific TOKEN for the BOT created, it is through the URL that the JSON with the message and usually some style attributes to display the message in Slack channels will be sent.

Using this URL allows any program to be used in a simple way to send messages to Slack just through a POST request.

The code for sending messages via Incoming WebHooks is extremely simple. You can make it more robust by using the message formatting parameters, or even create interactive messages.

Learn more about message structures at: (https://api.slack.com/messaging/composing/layouts#attachments).
