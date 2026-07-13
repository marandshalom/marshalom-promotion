import asyncio
import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from telethon import TelegramClient, events

# ===== የእርስዎ መረጃ =====
API_ID = 35977988
API_HASH = 'e8c0fa83d550cb5ecc48d34b87ea0f59'
BOT_TOKEN = '8600447897:AAExtZkgGO15u4tX81aHMiNRdlHSnunKi_M'
TARGET_CHANNEL_ID = -1002844148426

# ===== 2 ምንጭ ሰርጦች =====
SOURCE_CHANNELS = [
    'https://t.me/SebrisatElectronics',
    'https://t.me/HIKVISION0',
]

# ===== የእርስዎ ማስተዋወቂያ =====
PROMOTION = """

✨ እንኳን ደህና መጡ ወደ ማርሻሎም (Marshalom)! ✨
እኛ በኤሌክትሮኒክስ እና በደህንነት ካሜራዎች ላይ ጥራት ያለው አገልግሎት የምንሰጥ ታማኝ የቴክኖሎጂ አጋርዎ ነን። ✅
🚀 ዘመናዊ የደህንነት ካሜራዎች (CCTV) 📷 ጥራት ያላቸው ኤሌክትሮኒክስ እቃዎች 📺 ፈጣን እና አስተማማኝ አገልግሎት ⚡️
📢 ለወቅታዊ መረጃዎች እና ምርጥ ቅናሾች ቻናላችንን ይቀላቀሉ!
🌐 www.marshalom.com 🤖 @marshalom_bot 📞 0931556590
"""

# ===== የWeb ሰርቨር =====
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_health_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

# ===== ዋናው የቦት ኮድ =====
async def main():
    # ቦት ቶከን ይጠቀም!
    client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    await client
    print("✅ ቦቱ ተገናኝቷል! እየሰራ ነው...")

    @client.on(events.NewMessage(chats=SOURCE_CHANNELS))
    async def handler(event):
        try:
            msg = event.message
            if msg.photo:
                await client.send_message(TARGET_CHANNEL_ID, PROMOTION, file=msg.photo)
                print(f"✅ አዲስ ፎቶ ተልኳል!")
        except Exception as e:
            print(f"❌ ስህተት: {e}")

    await client.run_until_disconnected()

if __name__ == "__main__":
    Thread(target=run_health_server, daemon=True).start()
    asyncio.run(main())
