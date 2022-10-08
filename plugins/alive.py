import time
from datetime import datetime as dt
from platform import python_version as pyver

from git import Repo
from pyUltroid.version import __version__ as UltVer
from telethon import __version__, events
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

from . import *

(pattern="alive")
async def live(ult):
    pic = udB.get("ALIVE_PIC")
    uptime = time_formatter((time.time() - start_time) * 1000)
    header = udB.get("ALIVE_TEXT") if udB.get("ALIVE_TEXT") else "Hey, I'm Alive."
    als=str(f'''╭┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
┃‣ Master -{OWNER_NAME}
┃‣️ Telethon - {__version__}
┃‣ Python - {pyver()}
┃‣ Py-Ultroid -{UltVer}
┃‣ Ultroid Version -  {ultroid_version}
┃‣ Uptime - {uptime}
┃‣ Branch - [main](https://github.com/AL3X-Github/TG-FileShare-Bot/tree/main)
╰┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄''')
    if pic is None:
        return await eor(ult, als)
    elif pic is not None and "telegra" in pic:
        try:
            await ult.reply(als, file=pic, link_preview=False)
            await ult.delete()
        except ChatSendMediaForbiddenError:
            await eor(ult, als, link_preview=False)
    else:
        try:
            await ult.reply(file=pic)
            await ult.reply(als, link_preview=False)
            await ult.delete()
        except ChatSendMediaForbiddenError:
            await eor(ult, als, link_preview=False)


