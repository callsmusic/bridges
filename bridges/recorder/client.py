from pyrogram import Client
from .env import SESSION_NAME, API_ID, API_HASH

client = Client(SESSION_NAME, API_ID, API_HASH)
