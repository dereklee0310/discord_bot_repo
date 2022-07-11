'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-20 14:28:11
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-06-25 02:32:28
FilePath: \discord_bot_repo\cmds\react.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from pathlib import Path

with open ('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    
    @commands.command()
    async def pic(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(Path(random_pic)) # convert it into a file first
        await ctx.send(file=pic)

    @commands.command()
    async def web_pic(self, ctx):
        random_pic = random.choice(jdata['web_pic']) # just send the address of picture
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot)) # execute this line first to set up