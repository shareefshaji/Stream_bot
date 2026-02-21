from pyrogram import Client, filters
from info import temp

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        "Send me any video file and I'll give you a streaming link.\n"
        "You can play it in VLC, MX Player, etc."
    )
