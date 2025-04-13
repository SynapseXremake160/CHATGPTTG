import os
from dotenv import load_dotenv
from telethon import TelegramClient
from commands import register_commands

load_dotenv()

api_id = int(os.getenv("29599643"))
api_hash = os.getenv("5f1be22bccb797b2a23a9b2fb7ad6029")

client = TelegramClient("userbot", api_id, api_hash)

register_commands(client)

print("Bot çalışıyor...")
client.start()
client.run_until_disconnected()
