import asyncio
import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from telethon import TelegramClient, events

# ===== የእርስዎ መረጃ =====
API_ID = 35977988
API_HASH = 'e8c0fa83d550cb5ecc48d34b87ea0f59'
BOT_TOKEN = '8600447897:AAExtZkgGO15u4tX81aHMiNRdlHSnunKi_M'
YOUR_USER_ID = 1577576513

# ===== የእርስዎ የእውቂያ መረጃ =====
YOUR_PHONE = '+251931556590'
YOUR_CONTACT = '@ethiopiansecuritycamera'

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
    bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    await bot
    print("✅ ቦቱ ተገናኝቷል! እየሰራ ነው...")

    @bot.on(events.NewMessage)
    async def handler(event):
        try:
            customer_message = event.message.text
            customer_name = event.sender.username if event.sender else "Unknown"
            customer_id = event.sender_id
            
            # 1. መልእክቱን ወደ አንተ ላክ
            await bot.send_message(
                YOUR_USER_ID,
                f"📩 **አዲስ መልእክት ከደንበኛ!**\n\n"
                f"👤 ደንበኛ: @{customer_name}\n"
                f"🆔 መታወቂያ: `{customer_id}`\n"
                f"💬 መልእክት: {customer_message}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"📌 ምርቱን ለማየት:\n"
                f"👉 https://t.me/MarshalomTech\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"📞 መልስ ለመስጠት ደንበኛውን ያግኙ"
            )
            
            # 2. ደንበኛው አንተን እንዲያገኝ መልስ ስጥ
            await event.reply(
                f"✅ መልእክትዎ ተደርሷል!\n\n"
                f"📞 እባክዎ በዚህ ቁጥር ይደውሉ ወይም ይጻፉልን:\n"
                f"📱 {YOUR_PHONE}\n"
                f"🔗 {YOUR_CONTACT}\n\n"
                f"📌 ስለ ምርቱ የበለጠ ለማወቅ:\n"
                f"👉 https://t.me/MarshalomTech\n\n"
                f"✅ Your message has been received!\n"
                f"📞 Please contact us at:\n"
                f"📱 {YOUR_PHONE}\n"
                f"🔗 {YOUR_CONTACT}"
            )
            
            print(f"✅ መልእክት ከ @{customer_name} ተቀብሏል!")
        except Exception as e:
            print(f"❌ ስህተት: {e}")

    await bot.run_until_disconnected()

# ===== ሁለቱንም አብሮ አስኬድ =====
if __name__ == "__main__":
    Thread(target=run_health_server, daemon=True).start()
    asyncio.run(main())
