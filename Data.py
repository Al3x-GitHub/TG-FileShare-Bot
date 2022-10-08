from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❍ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐅𝐨𝐫 𝐁𝐨𝐭 𝐔𝐬𝐞𝐫𝐬
 ├ /start - Start Bot.
 ├ /about - About This Bot.
 ├ /help - This Bot Command Help.
 ├ /ping - To Check Alive Bot.
 └ /uptime - To View Bot Status.
 
 ❏️ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐅𝐨𝐫 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧
 ├ /logs - To View Bot Logs.
 ├ /setvar - To Set Var With Command.
 ├ /delvar - To Delete Var With Command.
 ├ /getvar - To View One Of The Var.
 ├ /users - To View Bot User Statistics.
 ├ /batch - To Link More Than One File.
 ├ /speedtest - Test The Speed Of The Bot.
 └ /broadcast - Broadcast Messages To Users.

👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐯𝐞𝐝 𝐁𝐲 </b><a href='https://t.me/MaximXRobot/101'>@MaximXRobot</a>"""

    close = [
        [InlineKeyboardButton("𝐂𝐥𝐨𝐬𝐞", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="help"),
            InlineKeyboardButton("𝐂𝐥𝐨𝐬𝐞", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("𝐀𝐛𝐨𝐮𝐭 𝐌𝐞", callback_data="about"),
            InlineKeyboardButton("𝐂𝐥𝐨𝐬𝐞", callback_data="close")
        ],
    ]

    ABOUT = """
<b>🤖 ❝ 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 ❞

@{} Is A Telegram Bot To Store Posts Or Files That Can Be Accessed Via Special Links Work 24×7.

 ➲ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : @{}
 ➲ 𝐅𝐫𝐚𝐦𝐞𝐰𝐨𝐫𝐤 : <a href='https://docs.pyrogram.org'>Pyrogram</a>
 ➲ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 : <a href='https://t.me/+vBu5aXlocTkwNGM1'>TG-FileShare-Bot</a>

👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐯𝐞𝐝 𝐁𝐲 </b><a href='https://t.me/MaximXRobot/101'>@MaximXRobot</a>
"""
