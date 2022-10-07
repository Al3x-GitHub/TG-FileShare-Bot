from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="help"),
                InlineKeyboardButton(text="⛔ 𝐂𝐥𝐨𝐬𝐞 ⛔", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐆𝐫𝐨𝐮𝐩", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="help"),
                InlineKeyboardButton(text="⛔ 𝐂𝐥𝐨𝐬𝐞 ⛔", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="help"),
                InlineKeyboardButton(text="⛔ 𝐂𝐥𝐨𝐬𝐞 ⛔", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬", url=client.invitelink),
                InlineKeyboardButton(text="𝐆𝐫𝐨𝐮𝐩", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="⛔ 𝐂𝐥𝐨𝐬𝐞 ⛔", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=client.invitelink),
                InlineKeyboardButton(text="𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
