from pyrogram import Client, filters
from flask import Flask
from threading import Thread
import os

# --- إعدادات البوت (تم وضع بياناتك الحقيقية) ---
api_id = 36078475
api_hash = "1f2795d538fdb50a715889e1bf859319"
bot_token = os.environ.get("BOT_TOKEN") # التوكن يوضع في إعدادات موقع Render فقط

app = Client("BufferBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# --- نظام البقاء أونلاين (لـ Render) ---
server = Flask(__name__)
@server.route('/')
def home():
    return "بوفر يعمل بكامل طاقته!"

def run():
    server.run(host='0.0.0.0', port=10000)

# --- أوامر البوت ---
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("أهلاً يا خطاب! 'بوفر' جاهز للخدمة. 🚀")

# --- تشغيل البوت والخادم ---
if __name__ == "__main__":
    # تشغيل الخادم الوهمي في الخلفية ليظل البوت نشطاً
    Thread(target=run).start()
    # تشغيل البوت
    app.run()
