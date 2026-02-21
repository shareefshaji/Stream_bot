# Telegram Streaming Bot

A Telegram bot that converts video files into streaming links for VLC, MX Player, etc.

## Deploy on Render

1. Fork this repository
2. Create new Web Service on Render
3. Set environment variables:
   - `API_ID`: Your API ID from my.telegram.org
   - `API_HASH`: Your API hash from my.telegram.org
   - `BOT_TOKEN`: Your bot token from @BotFather
   - `BIN_CHANNEL`: Your private channel ID
4. Deploy!

## Commands
- `/start` - Welcome message
- Send any video file to get streaming link
