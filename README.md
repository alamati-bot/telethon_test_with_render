# Telegram Auto Forwarder

هذا مشروع بسيط باستخدام Telethon لتحويل أي رسالة واردة إلى مستخدم أو قناة أخرى تلقائيًا.

## طريقة التشغيل

1. أنشئ ملف `.env` أو أضف متغيرات البيئة مباشرة إلى Render:
   - `API_ID`: من my.telegram.org
   - `API_HASH`: من my.telegram.org
   - `TARGET`: معرف الشخص أو القناة (مثلاً `@targetusername` أو رقم ID بدون @)

2. ثبت المتطلبات:

pip install -r requirements.txt


3. شغل السكربت:

python main.py



## تشغيل دائم على Render
ارفع المشروع إلى GitHub، ثم اربطه بـ Render وحدد ملف التشغيل: `python main.py`
