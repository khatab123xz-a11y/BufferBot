import os
import asyncio
from pyrogram import Client

# البيانات الأساسية
api_id = 36078475
api_hash = "1f2795d538fdb50a715889e1bf859319"
bot_token = os.environ.get("BOT_TOKEN")

# إنشاء البوت
app = Client("bover_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# أمر بسيط للتجربة
@app.on_message(lambda client, message: True)
async def handle_message(client, message):
    if message.text == "/start":
        await message.reply_text("بوفر يعمل بكامل طاقته! 🚀")

async def main():
    await app.start()
    print("البوت يعمل الآن بنجاح!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
