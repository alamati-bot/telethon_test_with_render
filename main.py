from dotenv import load_dotenv
from telethon import TelegramClient, events
import os, base64

load_dotenv()  # تحميل متغيرات البيئة من ملف .env

# session_b64 = os.getenv("SESSION_B64")
session_b64 = os.getenv(os.getenv("SESSION_PART1", "") +
    os.getenv("SESSION_PART2", "") )
if session_b64:
    with open("anon.session", "wb") as f:
        f.write(base64.b64decode(session_b64))


# إعداد المتغيرات من بيئة التشغيل
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
TARGET = os.getenv('TARGET')  # يمكن أن يكون ID رقمي أو username (بدون @)

client = TelegramClient("forwarder_session", API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True))
async def forward_message(event):
    try:
        await event.forward_to(TARGET)
        print(f"تم تحويل رسالة من {event.sender_id} إلى {TARGET}")
    except Exception as e:
        print(f"فشل التحويل: {e}")

client.start()
print("✅ البوت يعمل...")
client.run_until_disconnected()
