"""call

Available Commands:

.call

"""

from telethon import events

import asyncio
from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"call"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        
            "`Connecting To Sunny Leone's Personal Assistant...`",
            "`Call Connected.`",
            "`Sunny Leone's P.A: Hello This is Sunny Leone's Personal Assistant. Who is this?`",
            "`Me: Hello, It is Ninja Userbot User. I need Biology Practicals. Connect the Call to Sunny Leone`",
            "`Sunny Leone's P.A: Sure Sir.`",
            "`Connecting Call to Sunny Leone`",
            "`Private  Call Connected...`",
            "`Me: Hey, I want some Biology Practicals`",    
            "`Sunny Leone: May I Know Who Is This?`",
            "`Me: Yo, I'm Ninja Userbot User `",
            "`Sunny Leone: OMG!!! It's been a Long Time Since I saw You..`",
            "`Me: Yeah, I'm in Need of Biology Practicals Badly`",
            "`Sunny Leone: Sure, I'm giving you some Private Vids in your Ib`",
            "`Me: Thank You!`",
            "`Sunny Leone: I've also given you a premium access to my Website!`",
            "`Me: Whoa! Thank You!`",
            "`Sunny Leone: No Problem!\nBye!`",
            "`Private Call Disconnected.`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
