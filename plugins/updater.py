import os
import sys
from os import environ, execle, system

from bot import Bot
from git import Repo
from git.exc import InvalidGitRepositoryError
from pyrogram import Client, filters
from pyrogram.types import Message

from config import ADMINS, LOGGER

UPSTREAM_REPO = "https://github.com/AL3X-Github/TG-FileShare-Bot"


def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = ""
    tldr_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)



@Bot.on_message(filters.command("update") & filters.user(ADMINS))
async def update_bot(_, message: Message):
    message.chat.id
    msg = await message.reply_text("𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐔𝐩𝐃𝐚𝐭𝐞𝐬...")
    update_avail = updater()
    if update_avail:
        await msg.edit("✅ 𝐔𝐩𝐝𝐚𝐭𝐞 𝐅𝐢𝐧𝐢𝐬𝐡𝐞𝐝!")
        system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
        execle(sys.executable, sys.executable, "main.py", environ)
        return
    await msg.edit(
        f"𝐁𝐨𝐬𝐭 𝐈𝐬 𝐔𝐩 𝐓𝐨 𝐃𝐚𝐭𝐞 𝐕𝟏 𝐖𝐢𝐭𝐡 𝐁𝐫𝐚𝐧𝐚𝐜𝐡 [main]({UPSTREAM_REPO}/tree/main)",
        disable_web_page_preview=True,
    )


@Bot.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("`𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐁𝐨𝐭...`")
        LOGGER(__name__).info("𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝!!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("🤖 𝐁𝐨𝐭 𝐇𝐚𝐬 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝!!\n\n")
    os.system(f"kill -9 {os.getpid()} && bash start")
