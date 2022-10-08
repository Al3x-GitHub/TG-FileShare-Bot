import asyncio
from datetime import datetime
from time import time

from bot import Bot
from config import (
    ADMINS,
    CUSTOM_CAPTION,
    DISABLE_CHANNEL_BUTTON,
    FORCE_MSG,
    PROTECT_CONTENT,
    START_MSG,
)
from database.sql import add_user, full_userbase, query_msg
from pyrogram import filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked
from pyrogram.types import InlineKeyboardMarkup, Message

from helper_func import decode, get_messages, subsall, subsch, subsgc

from .button import fsub_button, start_button

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60**2 * 24),
    ("hour", 60**2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)


@Bot.on_message(filters.command("start") & filters.private & subsall & subsch & subsgc)
async def start_command(client: Bot, message: Message):
    id = message.from_user.id
    user_name = (
        f"@{message.from_user.username}"
        if message.from_user.username
        else None
    )

    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except BaseException:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except BaseException:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except BaseException:
                return
        temp_msg = await message.reply("<code>𝐖𝐚𝐢𝐭 𝐀 𝐌𝐨𝐦𝐞𝐧𝐭...</code>")
        try:
            messages = await get_messages(client, ids)
        except BaseException:
            await message.reply_text("<b>𝐀𝐧 𝐄𝐫𝐫𝐨𝐫 𝐇𝐚𝐬 𝐎𝐜𝐜𝐮𝐫𝐝 </b>🥺")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(
                    previouscaption=msg.caption.html if msg.caption else "",
                    filename=msg.document.file_name,
                )

            else:
                caption = msg.caption.html if msg.caption else ""

            reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None
            try:
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode="html",
                    protect_content=PROTECT_CONTENT,
                    reply_markup=reply_markup,
                )
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode="html",
                    protect_content=PROTECT_CONTENT,
                    reply_markup=reply_markup,
                )
            except BaseException:
                pass
    else:
        out = start_button(client)
        await message.reply_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=f"@{message.from_user.username}"
                if message.from_user.username
                else None,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(out),
            disable_web_page_preview=True,
            quote=True,
        )


    return


@Bot.on_message(filters.command("start") & filters.private)
async def not_joined(client: Bot, message: Message):
    buttons = fsub_button(client, message)
    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=f"@{message.from_user.username}"
            if message.from_user.username
            else None,
            mention=message.from_user.mention,
            id=message.from_user.id,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True,
    )


@Bot.on_message(filters.command(["users", "stats"]) & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(
        chat_id=message.chat.id, text="<code> 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠...</code>"
    )
    users = await full_userbase()
    await msg.edit(f"{len(users)} <b>𝐔𝐬𝐞𝐫𝐬 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭</b>")


@Bot.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0

        pls_wait = await message.reply(
            "<code>📡 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐢𝐧𝐠 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐖𝐚𝐢𝐭 𝐀 𝐌𝐨𝐦𝐦𝐞𝐧𝐭...</code>"
        )
        for row in query:
            chat_id = int(row[0])
            if chat_id not in ADMINS:
                try:
                    await broadcast_msg.copy(chat_id, protect_content=PROTECT_CONTENT)
                    successful += 1
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await broadcast_msg.copy(chat_id, protect_content=PROTECT_CONTENT)
                    successful += 1
                except UserIsBlocked:
                    blocked += 1
                except InputUserDeactivated:
                    deleted += 1
                except BaseException:
                    unsuccessful += 1
                total += 1
        status = f"""<b><u>𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭</u>
➲ 𝐍𝐚𝐦𝐞 𝐎𝐟 𝐔𝐬𝐞𝐫𝐬: <code>{total}</code>
➲ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬: <code>{successful}</code>
➲ 𝐅𝐚𝐢𝐥𝐞𝐝: <code>{unsuccessful}</code>
➲ 𝐔𝐬𝐞𝐫 𝐁𝐥𝐨𝐜𝐤𝐞𝐝: <code>{blocked}</code>
➲ 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐀𝐜𝐜𝐨𝐮𝐧𝐭: <code>{deleted}</code></b>"""
        return await pls_wait.edit(status)
    else:
        msg = await message.reply(
            "<code>𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐌𝐮𝐬𝐭 𝐖𝐡𝐢𝐥𝐞 𝐑𝐞𝐥𝐲 𝐓𝐨 𝐓𝐡𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐌𝐮𝐬𝐭 𝐖𝐡𝐢𝐥𝐞 𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐓𝐡𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭.</code>"
        )
        await asyncio.sleep(8)
        await msg.delete()


@Bot.on_message(filters.command("ping"))
async def ping_pong(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    m_reply = await m.reply_text("🇵 🇮 🇳 🇬 ")
    delta_ping = time() - start
    await m_reply.edit_text(
        "<b>𝐏𝐎𝐍𝐆!!</b> 🏓 \n"
        f"<b>◍ 𝐏𝐢𝐧𝐠 -</b> <code>{delta_ping * 1000:.3f}ms</code>\n"
        f"<b>◍ 𝐔𝐩𝐭𝐢𝐦𝐞 -</b> <code>{uptime}</code>\n"
    )


@Bot.on_message(filters.command("uptime"))
async def get_uptime(client, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "🤖 <b> 𝐁𝐨𝐬𝐭 𝐒𝐭𝐚𝐭𝐮𝐬:</b>\n"
        f"• <b>⚡ 𝐔𝐩𝐭𝐢𝐦𝐞 :</b> <code>{uptime}</code>\n"
        f"• <b>⏰ 𝐒𝐭𝐚𝐫𝐭 𝐓𝐢𝐦𝐞 :</b> <code>{START_TIME_ISO}</code>"
    )
