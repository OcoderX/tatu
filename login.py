from config import API_IDd, API_HASHd
from telethon import TelegramClient

api_id = API_IDd
api_hash = API_HASHd

client = TelegramClient('OcoderX', api_id, api_hash)

async def main():
    await client.start()

    # Getting information about yourself
    me = await client.get_me()

    # "me" is a User object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you're done, disconnect and/or run other async code...
    await client.disconnect()

# We have to manually call "loop.run_until_complete" here because
# "__main__" must be a synchronous function, and asyncio refuses
# to run the event loop in the same thread more than once.
with client:
    client.loop.run_until_complete(main())
