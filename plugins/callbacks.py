from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data
    
    if data == "help":
        await callback_query.message.edit_text(
            "**How to use:**\n"
            "1. Send any video file\n"
            "2. Get streaming link\n"
            "3. Open in VLC/MX Player"
        )
