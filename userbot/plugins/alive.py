"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Abe Dalle Apna Kaam Kar Baap Ko Mat Dekh.\n\nBot version: 1.5\nPython: 3.8.3\n\n`"
                     f"`Mera Maalik`: {DEFAULTUSER}\n"
                     "`Telethon version: 6.9.0\nPython: 3.8.3\nMade by:` @ranger_op\n"
                     f"`Sabka Baap` : {DEFAULTUSER} \n" "`Always with my Maalik\n`"
                     "[Deploy this userbot Now](https://github.com/Amberyt/JaaduBot)")

