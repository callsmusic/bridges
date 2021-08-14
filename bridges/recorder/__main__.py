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

fifo = None


def write_data(_, data: bytes, length: int):
    global fifo

    if not fifo:
        fifo = open(OUTPUT, "wb")

    fifo.write(data)


async def main():
    await client.start()
    raw = GroupCallFactory(client).get_raw_group_call(on_recorded_data=write_data)
    await raw.start(CHAT_ID, join_as=JOIN_AS)
    await idle()


asyncio.get_event_loop().run_until_complete(main())
