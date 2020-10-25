#JaaduBot Exclusive
#And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

#Usage .avdp Im Not Responsible For Any Ban caused By This

import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd

import asyncio

from time import sleep

COLLECTION_STRING = [
  
  "avengers-iphone-wallpaper"
]

async def animepp():

    os.system("rm -rf rangerop.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"rangerop.jpg")

@borg.on(admin_cmd(pattern="avdp ?(.*)"))

async def main(event):

    await event.edit("**Starting Avengers Profile Pic...\n\nDone !!! Check Your DP in 5 seconds. By [JaaduBot](https://github.com/Amberyt/JaaduBot)**")

    while True:

        await animepp()

        file = await event.client.upload_file("rangerop.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf rangerop.jpg")

        await asyncio.sleep(300) #Edit this to your required needs
