import random
import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import UserStatusOnline

# Telegram credentials
api_id = 23619220  
api_hash = "fa95f7a7ce715b76c27ddcd71e8fc77e"

client = TelegramClient("haseeb_session", api_id, api_hash)
bot_enabled = True  # Controls bot activity based on user status

# Track replied messages to avoid duplicate responses
replied_messages = set()

@client.on(events.UserUpdate)
async def handle_status_update(event):
    global bot_enabled
    me = await client.get_me()
    
    if event.user.id == me.id:
        # Disable bot when user comes online
        if isinstance(event.user.status, UserStatusOnline):
            bot_enabled = False
        else:
            bot_enabled = True

@client.on(events.NewMessage(incoming=True))
async def auto_responder(event):
    global replied_messages
    
    if not bot_enabled:
        return

    sender = await event.get_sender()
    if event.is_private and not sender.bot:
        msg_id = event.id  # Unique ID of the incoming message
        
        # Check if we've already replied to this message
        if msg_id in replied_messages:
            return
        
        msg = event.raw_text.strip()
        
        # Custom response for 'سلام'
        if msg == "سلام":
            response = "علیک جور استی"
        else:
            response = "سلام شازادع اقای حسیب فعلا در صنف درسی است  به زود ترین فرصت پاسخگو شما است  صبور باشید"
        
        # Add natural response delay
        await asyncio.sleep(random.uniform(1, 3))
        
        # Send response and mark this message as replied to
        await event.reply(response)
        replied_messages.add(msg_id)
        
        # Clean up old message IDs to avoid memory bloat
        if len(replied_messages) > 100:  # Keep only the last 100 message IDs
            replied_messages = set(list(replied_messages)[-100:])

print("🤖 Selfbot is now running...")
client.start()
client.run_until_disconnected()