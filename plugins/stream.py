import os
from pyrogram import Client, filters
from info import BIN_CHANNEL

@Client.on_message(filters.private & filters.video)
async def stream_handler(client, message):
    try:
        # Forward to bin channel
        forwarded = await message.forward(BIN_CHANNEL)
        
        # Generate streaming link
        stream_link = f"https://t.me/c/{str(BIN_CHANNEL).replace('-100', '')}/{forwarded.id}"
        
        # Send link to user
        await message.reply_text(
            f"✅ **Streaming Link Generated!**\n\n"
            f"📁 **File:** {message.video.file_name}\n"
            f"📊 **Size:** {message.video.file_size / (1024*1024):.2f} MB\n\n"
            f"🔗 **Link:** `{stream_link}`\n\n"
            f"📱 Copy this link and open in VLC or MX Player"
        )
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
