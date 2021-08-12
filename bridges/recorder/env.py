from os import getenv

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME")
CHAT_ID = int(getenv("CHAT_ID"))
JOIN_AS = int(getenv("JOIN_AS")) if getenv("JOIN_AS") is not None else None
OUTPUT = getenv("OUTPUT")
