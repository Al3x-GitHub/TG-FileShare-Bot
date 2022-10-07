from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> 😊 Commands For BOT Users 
 ├ /start - Start Bot
 ├ /about - About This Bot
 ├ /help - This Bot Command Help
 ├ /ping - To Check Alive Bot
 └ /uptime - To View Bot Status
 
 😉️ Commands For BOT Admin
 ├ /logs - To View Bot Logs
 ├ /setvar - To Set Var With Command
 ├ /delvar - To Delete Var With Command
 ├ /getvar - To View One Of The Vars With The Command
 ├ /users - To View Bot User Statistics
 ├ /batch - To Link More Than One File
 ├ /speedtest - To Test The Speed Of The Bot Server
 └ /broadcast - To Send Broadcast Messages To Bot Users

👨‍💻 Develoved By : </b><a href='https://t.me/MaximXRobot'>I𝗓υɱi 和泉</a>
"""

    close = [
        [InlineKeyboardButton("⛔ 𝐂𝐥𝐨𝐬𝐞 ⛔", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="help"),
            InlineKeyboardButton("⛔ 𝐂𝐥𝐨𝐬𝐞 ⛔", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("𝐀𝐛𝐨𝐮𝐭 𝐌𝐞", callback_data="about"),
            InlineKeyboardButton("⛔ 𝐂𝐥𝐨𝐬𝐞 ⛔", callback_data="close")
        ],
    ]

    ABOUT = """
<b>🤖 About This Bot :

@{} Is A Telegram Bot To Store Posts Or Files That Can Be Accessed Via Special Links Work 24×7.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://t.me/+vBu5aXlocTkwNGM1'>TG-FileShare-Bot</a>

👨‍💻 Develoved By :</b><a href='https://t.me/MaximXRobot'>I𝗓υɱi 和泉</a>
"""
