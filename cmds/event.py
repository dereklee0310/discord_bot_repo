'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-20 15:40:41
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-11 16:56:08
FilePath: \discord_bot_repo\cmds\event.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from distutils.log import error
import discord
from discord.ext import commands
from core.classes import Cog_Extension # let this cog class know who its parenet is
import random
import json
import sys
import os
import datetime
from pathlib import Path

with open ('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

sys.path.append(jdata['func_lib']) 
# # from func import is_text_channel
import func
class Event(Cog_Extension): # inheritance
    @commands.Cog.listener() # @bot.event
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['welcome_channel'])) # use int() to convert string into integer
        await channel.send(f'{member} has joind!')
 
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['leave_channel'])) # use int() to convert string into integer
        await channel.send(f'{member} has leaved!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if not func.is_text_channel(msg.channel.type):
            return #? is simply return a good idea?

        if msg.author == self.bot.user:
            return

        # keyword handler
        if "好笑嗎" in msg.content:
              await msg.channel.send("https://i.imgur.com/o5BdVBk.jpg")
        elif 'apex' in msg.content:
            await msg.channel.send('狗才打apex')
        elif "屁眼派對" in msg.content:
            await msg.channel.send('https://imgur.com/gallery/qWFV4zE')
        elif "屁眼" in msg.content:
            # await msg.channel.send("https://imgur.com/gallery/qWFV4zE")
            dir = os.listdir(Path(jdata['piyan_meme_dir']))
            random.seed(datetime.datetime.now())
            file = random.choice(dir)

            # handle specific gif file due to slow image loading
            if(file == "TseBKI5.gif"):
                await msg.channel.send('https://imgur.com/a/E8dQVzt')
                return

            await msg.channel.send(file=discord.File(Path(jdata['piyan_meme_dir']) / file))

        if msg.content.startswith('! ') and msg.author != self.bot.user: # if there is at least one space between '!' and [command]
            await msg.channel.send('Usage: `![command]`, no space or tab needed.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if(isinstance(error, commands.CommandNotFound)):
            await ctx.send('The command you type is invalid, use `!help to show the available commands`')
            return
        raise error
    
def setup(bot):
    bot.add_cog(Event(bot))