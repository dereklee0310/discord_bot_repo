'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-20 17:50:33
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-11 19:05:20
FilePath: \discord_bot_repo\cmds\task.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        async def time_task():
            await self.bot.wait_until_ready()
            with open ('setting.json', 'r', encoding='utf8') as jfile:
                jdata = json.load(jfile)
            self.channel = self.bot.get_channel(int(jdata['bg_channel']))
            while not self.bot.is_closed():
                # await self.channel.send("running rn!")
                # await asyncio.sleep(5)
                now_time = datetime.datetime.now().strftime('%H%M')
                if now_time == jdata['time'] and self.counter == 0:
                    await self.channel.send('task is working')
                    self.counter = 1
                    await asyncio.sleep(1) # lend bot some time to get ready
                else:
                    await asyncio.sleep(1)
                    pass
 
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'set channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0 #reset counter
        with open ('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open ('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)

def setup(bot):
    bot.add_cog(Task(bot)) # execute this line first to set up