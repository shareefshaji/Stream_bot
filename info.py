import os
from os import environ

# Required Variables
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
BIN_CHANNEL = int(os.environ.get("BIN_CHANNEL", "0"))

# Optional Variables
PORT = int(os.environ.get("PORT", "8080"))
STREAM_URL = os.environ.get("STREAM_URL", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

# Don't change these
temp = dict()
