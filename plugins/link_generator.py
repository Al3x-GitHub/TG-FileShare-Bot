from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command("batch"))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(
                text="<b>𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐡𝐞 𝐅𝐢𝐫𝐬𝐭 𝐌𝐞𝐬𝐬𝐚𝐠𝐞/𝐅𝐢𝐥𝐞 𝐅𝐫𝐨𝐦 𝐓𝐡𝐞 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</b>\n\n<b>or 𝐒𝐞𝐧𝐝 𝐏𝐨𝐬𝐭 𝐋𝐢𝐧𝐤 𝐅𝐫𝐨𝐦 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        await first_message.reply(
            "❌ <b>𝐄𝐫𝐫𝐨𝐫𝟒𝟎𝟒</b>\n\n<b>𝐓𝐡𝐢𝐬 𝐅𝐨𝐫𝐰𝐚𝐫𝐝𝐞𝐝 𝐏𝐨𝐬𝐭 𝐈𝐬 𝐍𝐨𝐭 𝐅𝐫𝐨𝐦 𝐌𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞</b>",
            quote=True,
        )
        continue

    while True:
        try:
            second_message = await client.ask(
                text="<b>𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐡𝐞 𝐅𝐢𝐫𝐬𝐭 𝐌𝐞𝐬𝐬𝐚𝐠𝐞/𝐅𝐢𝐥𝐞 𝐅𝐨𝐫𝐦 𝐓𝐡𝐞 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</b>\n\n<b>or 𝐒𝐞𝐧𝐝 𝐏𝐨𝐬𝐭 𝐋𝐢𝐧𝐤 𝐅𝐨𝐫𝐦 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        await second_message.reply(
            "❌ <b>𝐄𝐫𝐫𝐨𝐫𝟒𝟎𝟒</b>\n\n<b>𝐓𝐡𝐢𝐬 𝐅𝐨𝐫𝐰𝐚𝐫𝐝𝐞𝐝 𝐏𝐨𝐬𝐭 𝐈𝐬 𝐍𝐨𝐭 𝐅𝐨𝐫𝐦 𝐌𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞</b>",
            quote=True,
        )
        continue

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔁 𝐒𝐡𝐚𝐫𝐞 𝐋𝐢𝐧𝐤", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    await second_message.reply_text(
        f"<b>𝐅𝐢𝐥𝐞 𝐒𝐡𝐚𝐫𝐢𝐧𝐠 𝐋𝐢𝐧𝐤 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐂𝐫𝐞𝐚𝐭𝐞𝐝:</b>\n\n{link}",
        quote=True,
        reply_markup=reply_markup,
    )


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command("genlink"))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(
                text="<b>𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐅𝐫𝐨𝐦 𝐓𝐡𝐞 𝐃𝐚𝐭𝐚𝐛𝐚𝐝𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</b>\n\n<b>𝐎𝐫 𝐒𝐞𝐧𝐝 𝐏𝐨𝐬𝐭 𝐋𝐢𝐧𝐤 𝐅𝐫𝐨𝐦 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        await channel_message.reply(
            "❌ <b>𝐄𝐫𝐫𝐨𝐫𝟒𝟎𝟒</b>\n\n<b>𝐓𝐡𝐢𝐬 𝐅𝐨𝐫𝐰𝐚𝐫𝐝𝐞𝐝 𝐏𝐨𝐬𝐭 𝐈𝐬 𝐍𝐨𝐭 𝐅𝐫𝐨𝐦 𝐌𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</b>",
            quote=True,
        )
        continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔁 𝐒𝐡𝐚𝐫𝐞 𝐋𝐢𝐧𝐤", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    await channel_message.reply_text(
        f"<b>𝐅𝐢𝐥𝐞 𝐒𝐡𝐚𝐫𝐢𝐧𝐠 𝐋𝐢𝐧𝐤 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲:</b>\n\n{link}",
        quote=True,
        reply_markup=reply_markup,
    )
