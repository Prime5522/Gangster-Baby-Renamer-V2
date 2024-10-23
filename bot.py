import asyncio
from pyrogram import Client, idle
import os
from plugins.cb_data import app as Client2
from pyrogram.errors import BadMsgNotification

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID", "25425840"))
API_HASH = os.environ.get("API_HASH", "e6ea2eca4aa38e965511f323e5ffa578")
STRING = os.environ.get("STRING", "")

bot = Client(
    "Renamer",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

async def start_clients():
    apps = [Client2, bot] if STRING else [bot]
    
    while True:
        try:
            for app in apps:
                await app.start()
            print("Clients started successfully!")
            await idle()  # Keeps the clients running
            
            for app in apps:
                await app.stop()
            break  # Exit loop after successful run
        except BadMsgNotification as e:
            print(f"Error occurred: {e}, retrying in 5 seconds...")
            await asyncio.sleep(5)  # Retry after 5 seconds

if __name__ == "__main__":  # Fixed here
    if STRING:
        asyncio.run(start_clients())
    else:
        bot.run()
