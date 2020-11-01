#JaaduBot Exclusive
#Give Credits if you copy

from telethon import events
import random, re
from uniborg.util import admin_cmd

RUNSREACTS = ["`Want to make a userbot for yourself But Fed up of writing Long Command So here is a new way to get string session without termux.
"`Firstly, Go to my.telegram.org and create an app of your choice. Then you will get app id and api`"
"`Second Go to @Botfather and make a bot of ur choice.`"
"`You will get a token copy that.`"
"`Then click on /mybots then go to Bot Settings  and turn on inline mode on.`"
"`After that go to this link`"
"`http://generatestringsession.rangerop.repl.run`"
"`Go to this link and after that follow the onscreen prompts.`"
"`After doing all the process go and check your saved message for the string session.`"
"`Create a heroku.com and github.com account`"
"`After that go to github.com and search JaaduBot or just click [HERE](github.com/Amberyt/JaaduBot) Then Open that in Desktop site.`"
"`Click on the Fork option in the top right corner`"
"`Then you will see a deploy to heroku button just click on that and fill the info. Done your bot is done😍☺️Join @jaadubotofficial for any help.`"
"`Note-: I (@ranger_op) will not be responsible for any kind of bans.`"
]

@borg.on(admin_cmd(pattern="tut"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)
