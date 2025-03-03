from telethon.sync import TelegramClient  

# اطلاعات خودت رو اینجا جایگزین کن
api_id = 23619220  # بدون ""
api_hash = "fa95f7a7ce715b76c27ddcd71e8fc77e"  # درست بدون خط جدید

# ساخت یک کلاینت برای ورود
client = TelegramClient("haseeb_session", api_id, api_hash)

async def main():
    await client.send_message("me", "✅ سلف‌بات با موفقیت لاگین شد!")

with client:
    client.loop.run_until_complete(main())
