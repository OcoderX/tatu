from pyrogram import Client, filters, types
from config import API_ID, API_HASH, TEXT


if not API_HASH or API_ID == 1234:
    # config.py fayliga yozmagan bo'lsangiz
    # my.telegram.org dan olasiz
    print("my.telegram.org dan olgan ma'lumotlaringizni kiriting")
    API_ID = input("API_ID: ")
    API_HASH = input("API_HASH: ")

app = Client("userbot", API_ID, API_HASH)

@app.on_message(filters.me & filters.command("nb", prefixes=[".", "!"]))
async def nb_command(_, msg: types.Message):
    await msg.edit_text(TEXT)

app.run()
