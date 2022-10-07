import os

import speedtest
import wget
from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import ADMINS


@Bot.on_message(filters.command("speedtest") & filters.user(ADMINS))
async def run_speedtest(client: Bot, message: Message):
    m = await message.reply_text("⚡ 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐒𝐞𝐫𝐯𝐞𝐫 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭...")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("📥 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐩𝐞𝐞𝐝...")
        test.download()
        m = await m.edit("📤 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐔𝐩𝐥𝐨𝐚𝐝 𝐒𝐩𝐞𝐞𝐝...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await m.edit(e)
        return
    m = await m.edit("🔄 𝐒𝐡𝐚𝐫𝐢𝐧𝐠 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐬")
    path = wget.download(result["share"])

    output = f"""💡 <b>𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐬</b>
    
<u><b>𝐂𝐥𝐢𝐞𝐧𝐭:<b></u>
<b>𝐈𝐒𝐏:</b> {result['client']['isp']}
<b>𝐂𝐨𝐮𝐧𝐭𝐫𝐲:</b> {result['client']['country']}
  
<u><b>𝐒𝐞𝐫𝐯𝐞𝐫:</b></u>
<b>𝐍𝐚𝐦𝐞:</b> {result['server']['name']}
<b>𝐂𝐨𝐮𝐧𝐭𝐫𝐲:</b> {result['server']['country']}, {result['server']['cc']}
<b>𝐒𝐩𝐨𝐧𝐬𝐨𝐫:</b> {result['server']['sponsor']}
⚡️ <b>𝐏𝐢𝐧𝐠:</b> {result['ping']}"""
    msg = await client.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
