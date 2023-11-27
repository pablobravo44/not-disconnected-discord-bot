# Not disconnected Discord Bot

A discord bot that does not allow any user to send messages or be in a voice channel if they are offline. The user will receive a notification when one of his message is deleteed or when disconnected from a voice chat.

The text channel where the bot will send the notifications related to voice channel discconection is defined by the "CHANNEL_ID" variable

## Prequisitos

-   [Python](https://www.python.org)

## Variables

-   [TOKEN] - You can get a bot Token in the Discord Developer Portal
-   [CHANNEL_ID] - You can get it through Discord by right clicking on the Discord channel and copying it ( you may need to active Discord Developer Mode )

## Running on local

If you want to run the bot on local:

```
python main.py
```

## Running on server

You can follow this tutorial to use it on your own server ( using this repository code ):

```
https://www.youtube.com/watch?v=J7Fm7MdZn_E
```