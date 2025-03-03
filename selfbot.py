import random
import asyncio
from telethon import TelegramClient, events  

# اطلاعات ورود به تلگرام
api_id = 23619220  
api_hash = "fa95f7a7ce715b76c27ddcd71e8fc77e"  

# اتصال به تلگرام
client = TelegramClient("haseeb_session", api_id, api_hash)

# پیام‌های مختلف برای پاسخگویی به پیام‌های اول، دوم و سوم هر کاربر
first_responses = ["سلام! چطوری؟", "سلام عزیز، خوبی؟", "درود بر تو!"]
second_responses = ["چیزی لازم داشتی؟", "بگو جانم؟", "بفرمایید؟"]
third_responses = ["الان کار دارم، بعداً حرف می‌زنیم!", "یکم سرم شلوغه، بعداً پیام بده.", "باشه، بعداً در ارتباط باشیم."]

# پاسخ‌های مخصوص پیام‌های خاص
custom_responses = {
    "سلام": ["جان، خوبی؟", "سلام عزیز، حالت چطوره؟"],
    "چطوری": ["شکر، خودت چطوری؟", "خوبم، تو چطوری؟"],
    "😢": ["چرا ناراحتی؟ 😔", "چی شده؟"],
    "😂": ["خنده‌ات همیشه پایدار 😂", "خوش باشی همیشه!"]
}

# لیست پیام‌های ارسال‌شده برای جلوگیری از تکرار بی‌دلیل
user_messages = {}

@client.on(events.NewMessage(incoming=True))  
async def auto_reply(event):
    sender = await event.get_sender()
    user_id = sender.id

    # بررسی اینکه پیام از طرف خودت نیست
    if not sender.bot and event.is_private:
        user_messages.setdefault(user_id, 0)
        user_messages[user_id] += 1

        # ارسال پاسخ متفاوت بر اساس تعداد پیام‌ها
        if user_messages[user_id] == 1:
            reply = random.choice(first_responses)
        elif user_messages[user_id] == 2:
            reply = random.choice(second_responses)
        else:
            reply = random.choice(third_responses)

        # بررسی پاسخ‌های خاص برای پیام‌های خاص
        text = event.raw_text.lower()
        for key in custom_responses:
            if key in text:
                reply = random.choice(custom_responses[key])
                break

        # تأخیر تصادفی برای طبیعی‌تر شدن
        await asyncio.sleep(random.uniform(1, 3))
        await event.reply(reply)

print("🤖 سلف‌بات فعال شد...")
client.start()
client.run_until_disconnected()
