from os import getenv

SESSION_NAME = getenv("SESSION_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

STREAM_URL = getenv("STREAM_URL")

CHAT_ID = int(getenv("CHAT_ID"))
JOIN_AS = int(getenv("JOIN_AS")) if getenv("JOIN_AS") is not None else None

OUTPUT = getenv("OUTPUT")
