#all plugins are imported from bothub,x-tra-telegram by @heyworld
#Don't edit or you gay
#credits: spechide,ravana69,mkaraniya & me
from telethon import events

import asyncio

from userbot.events import register 
from userbot import  CMD_HELP, bot, ALIVE_NAME
from collections import deque
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from random import choice, getrandbits, randint
from re import sub
from random import randint
import random


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "bheart":

        await event.edit(input_str)

        animation_chars = [

            "🖤",

            "❤️",

            "🖤",

            "❤️"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "fnl":

        await event.edit(input_str)

        animation_chars = [

            "😁🏿",

            "😁🏾",

            "😁🏽",

            "😁🏼",

            "‎😁",

            "**Fair & Lovely GeNg Is BeHiNd You....**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])
