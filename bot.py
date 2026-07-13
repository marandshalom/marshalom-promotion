import asyncio
import re
from telethon import TelegramClient, events

API_ID = 35977988
API_HASH = 'e8c0fa83d550cb5ecc48d34b87ea0f59'
PHONE = '+251721386958'
TARGET_CHANNEL_ID = -1002844148426

SOURCE_CHANNELS = [
    -1002250223737,
    -1002065550405,
    -1002155573697,
    -1001670686737,
]

blocked_words = [
    "Sebrisat", "SEBRISAT", "sebrisat", "ሴብሪሳት",
    "@SebrisatBuy", "@SebrisatSecurity", "@SebrisatElectronics",
    "Seniya", "SENIYA", "seniya", "EHSAN", "Ehsan", "ehsan",
    "TREKPLC", "trekplc", "Trekplc", "Mr Shemsu", "mrshemsu",
    "HIKVISION", "Hikvision", "hikvision",
    "@trekplc", "@mrshemsu",
    "መርካቶ", "መገናኛ", "ቦሌ", "ሲኤምሲ", "ካዛንቺስ",
    "መክሲኮ", "ሳሪስ", "ፒያሳ", "ቃሊቲ", "አራዳ",
    "ጉለሌ", "ልደታ", "ሱፐርሳሌ", "ጉርድሾላ",
    "ጀሞ", "ላፍቶ", "አዲስ አበባ", "ኮልፌ", "አጠናተራ",
    "Addis Ababa", "Addis", "addis",
    "📍", "📞", "💰", "Inbox", "Contact us",
    "PDF", "pdf", "Word", "word", "Excel", "excel",
]

def clean_text(text):
    text = re.sub(r'(?:\+251|0)?\s*[789]\d{2}\s*\d{3}\s*\d{4}', '', text)
    text = re.sub(r'#ይደውሉ\s*', '', text)
    for word in blocked_words:
        text = text.replace(word, "")
    text = re.sub(r'\d{1,3}(?:,\d{3})*\s*ብር', '', text)
    text = re.sub(r'\d{1,3}(?:,\d{3})*\s*Birr', '', text)
    text = re.sub(r'\d{1,3}(?:,\d{3})*\s*ETB', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return '\n'.join(lines).strip()

PROMOTION = """

✨ እንኳን ደህና መጡ ወደ ማርሻሎም (Marshalom)! ✨
እኛ በኤሌክትሮኒክስ እና በደህንነት ካሜራዎች ላይ ጥራት ያለው አገልግሎት የምንሰጥ ታማኝ የቴክኖሎጂ አጋርዎ ነን። ✅
🚀 ዘመናዊ የደህንነት ካሜራዎች (CCTV) 📷 ጥራት ያላቸው ኤሌክትሮኒክስ እቃዎች 📺 ፈጣን እና አስተማማኝ አገልግሎት ⚡️
📢 ለወቅታዊ መረጃዎች እና ምርጥ ቅናሾች ቻናላችንን ይቀላቀሉ!
🌐 www.marshalom.com 🤖 @marshalom_bot 📞 0931556590
"""

async def main():
    client = TelegramClient('marshalom_bot', API_ID, API_HASH)
    await client.start(phone=PHONE)
    print("✅ ተገናኝቷል! ለዘላለም እየሰራ ነው...")

    @client.on(events.NewMessage(chats=SOURCE_CHANNELS))
    async def handler(event):
        try:
            msg = event.message
            if msg.file:
                return
            text = msg.text if msg.text else ""
            cleaned = clean_text(text)
            final = cleaned + "\n\n" + PROMOTION
            await client.send_message(TARGET_CHANNEL_ID, final, file=msg.media if msg.media else None)
            print("✅ ፖስት ተልኳል!")
        except Exception as e:
            print(f"❌ ስህተት: {e}")

    await client.run_until_disconnected()

asyncio.run(main())
