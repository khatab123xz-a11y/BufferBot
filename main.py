from pyrogram import Client
from flask import Flask
from threading import Thread
import os
import asyncio

# إعدادات البوت
api_id = 36078475
api_hash = "1f2795d538fdb50a715889e1bf859319"
bot_token = os.environ.get("BOT_TOKEN")

app = Client("BufferBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# خادم Flask لإبقاء البوت أونلاين
server = Flask(__name__)
@server.route('/')
def home():
    return "بوفر يعمل بكامل طاقته!"

def run_server():
    server.run(host='0.0.0.0', port=10000)

# تشغيل البوت و Flask معاً بطريقة صحيحة
async def main():
    await app.start()
    print("البوت يعمل الآن!")
    await asyncio.Event().wait() # إبقاء البوت يعمل

if __name__ == "__main__":
    Thread(target=run_server).start()
    asyncio.run(main())
