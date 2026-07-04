import os
import asyncio
from pyrogram import Client

# جلب التوكن من المتغيرات البيئية التي ضبطناها
bot_token = os.environ.get("BOT_TOKEN")

# إعدادات البوت (تأكد أن api_id و api_hash صحيحتان)
api_id = 36078475
api_hash = "1f2795d538fdb50a715889e1bf859319"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# هذا الجزء يضمن تشغيل البوت بشكل سليم
async def start_bot():
    await app.start()
    print("البوت يعمل الآن بنجاح! 🚀")
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        # إنشاء حلقة أحداث جديدة وتشغيل البوت بداخلها
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(start_bot())
    except Exception as e:
        print(f"حدث خطأ: {e}")
