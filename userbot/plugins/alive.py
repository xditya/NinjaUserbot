"""Check if userbot alive."""

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://telegra.ph/file/19161731ca00f82fd6e7d.jpg"
ALIVE_caption = "**Ninja Userbot is Alive!**\n\n\n"
ALIVE_caption += "**🧿 Bot Tier:** `Pro Like {DEFAULTUSER}`\n\n"
ALIVE_caption += "**🧬 Telethon version:** `1.16.2`\n\n"
ALIVE_caption += "**🧿 Python:** `3.7.4`\n\n"
ALIVE_caption += "**🧬 Database Status:** : `All Set and are Working Flawlessly!`\n\n"
ALIVE_caption += "**🧿 Ninja Userbot Version:** `1.2`\n\n"
ALIVE_caption += "**🧿 My Pro Owner:** `{DEFAULTUSER}` \n\n\n"
ALIVE_caption += "[🛡Deploy Ninja Userbot🛡](https://github.com/ninjanaveen/NinjaUserbot)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_caption)
