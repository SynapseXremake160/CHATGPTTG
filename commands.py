from telethon import events
from utils import rastgele_iltifat
import random

def register_commands(client):

    @client.on(events.NewMessage(pattern=r'\.ping'))
    async def ping(event):
        await event.reply("Pong! Bot aktif.")

    @client.on(events.NewMessage(pattern=r'\.id'))
    async def get_id(event):
        if event.reply_to_msg_id:
            msg = await event.get_reply_message()
            await event.reply(f"Yanıtlanan kişinin ID'si: `{msg.sender_id}`")
        else:
            await event.reply(f"Senin ID'n: `{event.sender_id}`")

    @client.on(events.NewMessage(pattern=r'\.iltifat'))
    async def iltifat(event):
        if event.reply_to_msg_id:
            iltifat = rastgele_iltifat()
            await event.reply(iltifat)
        else:
            await event.reply("Birine yanıt vererek kullanmalısın.")

    @client.on(events.NewMessage(pattern=r'\.ask'))
    async def ask(event):
        if event.reply_to_msg_id:
            oran = random.randint(1, 100)
            await event.reply(f"Aşk uyum oranınız: %{oran}!")
        else:
            await event.reply("Birine yanıt vererek kullanmalısın.")

    @client.on(events.NewMessage(pattern=r'\.gaytest'))
    async def gaytest(event):
        if event.reply_to_msg_id:
            oran = random.randint(0, 100)
            await event.reply(f"Gaylik oranı: %{oran}")
        else:
            await event.reply("Bir mesaja yanıtla ve tekrar dene.")

    @client.on(events.NewMessage(pattern=r'\.iqtest'))
    async def iqtest(event):
        if event.reply_to_msg_id:
            iq = random.randint(60, 160)
            await event.reply(f"Zekâ seviyesi: IQ {iq}")
        else:
            await event.reply("Yanıtla ki kimin IQ'su ölçülecek bilelim.")

    @client.on(events.NewMessage(pattern=r'\.bilgi'))
    async def bilgi(event):
        panel = """
╭─[ 🤖 BOT BİLGİ PANELİ ]─╮

    👤 Kurucu: @SyroxKurucu
    ⚙️ Altyapı: Python - Telethon  
    🧠 Bot Türü: Kişisel User-Bot  
    🔐 Sahip: Sadece komut sahibi kontrol edebilir.

    ╭─[ Kişisel Komutlar ]─╮
    ├ .ping → Botun gecikmesini ölçer
    ├ .id → Kullanıcının ID bilgisini verir
    ├ .iltifat → Yanıtlanan kişiye güzel söz söyler
    ├ .ask → Aşk uyumu testi yapar
    ├ .gaytest → Gaylik oranını gösterir
    ├ .iqtest → IQ testini yapar
    ├ .bilgi → Bu paneli gösterir
╰────────────────────────╯
        """
        await event.reply(panel)
