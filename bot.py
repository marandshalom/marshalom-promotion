import asyncio
import os
import re
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from telethon import TelegramClient, events

# ===== የእርስዎ መረጃ =====
API_ID = 35977988
API_HASH = 'e8c0fa83d550cb5ecc48d34b87ea0f59'
YOUR_PHONE = '+251721386958'
TARGET_CHANNEL_ID = -1002844148426  # የእርስዎ ቻናል

# ===== 2 ምንጭ ሰርጦች (Sebrisat እና HIKVISION) =====
SOURCE_CHANNELS = [
    'https://t.me/SebrisatElectronics',
    'https://t.me/HIKVISION0',  # ወይም ትክክለኛውን ሊንክ አስገባ
]

# ===== ሊወገዱ የሚገቡ ቃላት (ሁሉም ጽሁፍ ይወገዳል) =====
def remove_all_text(text):
    # ሁሉንም ጽሁፍ አስወግድ - ባዶ መስመር ብቻ ይቀርሃል
    return ""

# ===== የእርስዎ ማስተዋወቂያ =====
PROMOTION = """

✨ እንኳን ደህና መጡ ወደ ማርሻሎም (Marshalom)! ✨
እኛ በኤሌክትሮኒክስ እና በደህንነት ካሜራዎች ላይ ጥራት ያለው አገልግሎት የምንሰጥ ታማኝ የቴክኖሎጂ አጋርዎ ነን። ✅
🚀 ዘመናዊ የደህንነት ካሜራዎች (CCTV) 📷 ጥራት ያላቸው ኤሌክትሮኒክስ እቃዎች 📺 ፈጣን እና አስተማማኝ አገልግሎት ⚡️
📢 ለወቅታዊ መረጃዎች እና ምርጥ ቅናሾች ቻናላችንን ይቀላቀሉ!
🌐 ድር ጣቢያችንን ይጎብኙ፡ www.marshalom.com
🤖 ጥያቄ ካለዎት የኛን አውቶማቲክ ረዳት ያናግሩ፡ @marshalom_bot
📞 ለበለጠ መረጃ ይደውሉልን፡ 0931556590

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ስለ ምርቱ የበለጠ ለማወቅ እና ዋጋ ለማግኘት፦
👉 @ethiopiansecuritycamera ላይ ይጻፉልን
👉 ወይም ይህን ሊንክ ይጫኑ፦
🔗 https://t.me/ethiopiansecuritycamera
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔹 For product details and price:
👉 Contact us on @ethiopiansecuritycamera
👉 Or click this link: https://t.me/ethiopiansecuritycamera
"""

# ===== የWeb ሰርቨር (ለRender ፖርት) =====
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
    client = TelegramClient('marshalom_render_bot', API_ID, API_HASH)
    await client.start(phone=YOUR_PHONE)
    print("✅ ተገናኝቷል! እየሰራ ነው...")

    @client.on(events.NewMessage(chats=SOURCE_CHANNELS))
    async def handler(event):
        try:
            msg = event.message
            # ፎቶ (photo) ብቻ ያስተላልፍ
            if msg.photo:
                # ሁሉንም ጽሁፍ አስወግድ - ፎቶ ብቻ!
                final_text = PROMOTION
                await client.send_message(TARGET_CHANNEL_ID, final_text, file=msg.photo)
                print(f"✅ አዲስ ፎቶ ተልኳል!")
        except Exception as e:
            print(f"❌ ስህተት: {e}")

    await client.run_until_disconnected()

# ===== ሁለቱንም አብሮ አስኬድ =====
if __name__ == "__main__":
    Thread(target=run_health_server, daemon=True).start()
    asyncio.run(main())
