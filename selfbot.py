import random
import asyncio
from collections import deque
from telethon import TelegramClient, events
from telethon.tl.types import UserStatusOnline

# Telegram credentials (replace with yours)
api_id = 23619220
api_hash = "fa95f7a7ce715b76c27ddcd71e8fc77e"

client = TelegramClient("haseeb_session", api_id, api_hash)
bot_enabled = True  # Master switch for the bot

# Track replied messages (max 100 to prevent memory bloat)
replied_messages = deque(maxlen=100)

@client.on(events.UserUpdate)
async def handle_status(event):
    global bot_enabled
    me = await client.get_me()
    
    # Only react to YOUR account's status changes
    if event.user.id == me.id:
        bot_enabled = not isinstance(event.user.status, UserStatusOnline)
        print(f"Bot {'disabled' if not bot_enabled else 'enabled'}")

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if not bot_enabled:
        return  # Skip processing if bot is disabled

    sender = await event.get_sender()
    if event.is_private and not sender.bot:
        msg_id = event.id
        
        # Avoid duplicate replies
        if msg_id in replied_messages:
            return
        
        replied_messages.append(msg_id)  # Track message ID immediately
        
        # Custom responses
        if event.raw_text.strip() == "سلام":
            response = "علیک جور استی"
        else:
            response = "سلام شازادع اقای حسیب فعلا در صنف درسی است  به زود ترین فرصت پاسخگو شما است  صبور باشید"
        
        # Simulate human-like delay
        await asyncio.sleep(random.uniform(1, 3))
        await event.reply(response)

print("🤖 Selfbot running. Ctrl+C to stop.")
client.start()
client.run_until_disconnected()