import os
import asyncio
from pyrogram import idle
from pytgcalls import GroupCallFactory
from .client import client
from .env import CHAT_ID, OUTPUT, JOIN_AS

try:
    os.mkfifo(OUTPUT)
except FileExistsError:
    pass


async def main():
    await client.start()
    group_call = GroupCallFactory(client).get_file_group_call(
        OUTPUT, play_on_repeat=True
    )
    await group_call.start(CHAT_ID, join_as=JOIN_AS)
    await idle()


asyncio.get_event_loop().run_until_complete(main())
