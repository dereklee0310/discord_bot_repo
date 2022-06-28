'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-20 15:40:41
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-06-25 02:35:15
FilePath: \discord_bot_repo\cmds\event.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import discord
from discord.ext import commands
from core.classes import Cog_Extension # let this cog class know who its parenet is
import random
import json

with open ('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension): # inheritance
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['welcome_channel'])) # use int() to convert string into integer
        await channel.send(f'{member} has joind!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['leave_channel'])) # use int() to convert string into integer
        await channel.send(f'{member} has leaved!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('endswith?') and msg.author != self.bot.user:
            await msg.channel.send('is endswith!')
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('is keyword!')
    
def setup(bot):
    bot.add_cog(Event(bot))