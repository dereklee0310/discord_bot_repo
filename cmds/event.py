import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open ('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['welcome_channel']))
        await channel.send(f'{member} has joind!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['leave_channel']))
        await channel.send(f'{member} has leaved!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('endswith?') and msg.author != self.bot.user:
            await msg.channel.send('is endswith!')
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('is keyword!')
    
def setup(bot):
    bot.add_cog(Event(bot))