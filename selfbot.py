from telethon import TelegramClient, events  

# اطلاعات ورود به تلگرام
api_id = 23619220  # عدد بدون ""
api_hash = "fa95f7a7ce715b76c27ddcd71e8fc77e"  

# اتصال به تلگرام
client = TelegramClient("haseeb_session", api_id, api_hash)

# تنظیم پیام خودکار وقتی آنلاین نیستی
offline_message = "🔴 حسیب آفلاین است. لطفاً بعداً پیام دهید."

@client.on(events.NewMessage(incoming=True))  
async def auto_reply(event):
    sender = await event.get_sender()
    
    # بررسی اینکه پیام از طرف خودت نیست
    if not sender.bot and event.is_private:  
        await event.reply(offline_message)

print("🤖 سلف‌بات فعال شد...")
client.start()
client.run_until_disconnected()
