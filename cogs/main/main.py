'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-20 14:27:58
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-27 17:27:01
FilePath: \discord_bot_repo\cogs\main\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE   
'''
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension
import requests
from pathlib import Path
import json
import urllib

with open ('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class Main(Cog_Extension):
    COG_EMOJI = '❗'

    # return the latency of bot
    @commands.command()
    async def ping(self, ctx):
        """get server latency"""
        await ctx.send(f'{round(self.bot.latency*1000)}ms')

    @commands.command()
    async def aquatrail(self, ctx):
        """send a bloodtrail emoji but aqua edition"""
        await ctx.send('那你很棒欸 老弟<:test:993523987520950352>')

    @commands.command()
    async def sayitforme(self, ctx, *, msg): # use * to get all arguments
        """let the bot speak for u"""
        # keyword-only argument: https://segmentfault.com/a/1190000005173136
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clear(self, ctx, num: int):
        """delete specific number of message"""
        await ctx.channel.purge(limit=num + 1) # + 1 for the command message itself
    
    @commands.command()
    async def profile(self, ctx): #todo create a chinese version profile !! let user set his language using another command and send the message according his setting.
        """show the profile of the bot"""
        from datetime import datetime,timezone,timedelta
        time = datetime.now(tz=timezone.utc)
        file = nextcord.File(Path(jdata['bot_info']['bot_icon']))
        embed=nextcord.Embed(title="***Hi, I am Not a Bot, designed to best serve your needs***", color=0x80FFEC, timestamp=time)
        # embed.set_author(name="Not a Bot", url=jdata['rick_roll'], icon_url=f"attachment://{file.filename}")
        embed.set_author(name="Not a Bot", url=jdata['rick_roll'], icon_url=self.bot.user.avatar.url)

        empty = "\u200b"
        embed.add_field(name="Type `!help` to get started \U0001F913", value='**Main Features:**', inline=False)
        embed.add_field(name="\U0001F324 Taiwan 36h Weather Forecast", value="```!forecast [county name]```", inline=True)
        embed.add_field(name="<:test:993523987520950352> Aquatrail", value="```!aquatrail```", inline=True)

        slight_smile = "\U0001f642"
        # embed.add_field(name=f"If you encounter problems enjoying my service or have any cool idea about my new feature, please contact the developer. {slight_smile}", value=empty, inline=False)
        embed.add_field(name=empty, value=f"**If you encounter problems enjoying my service or have any cool\n idea about my new feature, please contact the developer. {slight_smile}**", inline=False)
        embed.add_field(name="\U0001F914 Discord", value="```DEREK#5958```", inline=True)
        embed.add_field(name="\U00002709 Gmail", value="```dereklee0310@gmail.com```", inline=True)
        # embed.add_field(name="\U00002709 test", value="[Link](https://github.com/Proladon/Proladon-DC_BaseBot)", inline=True) #! markdown link work for embed!
        embed.set_footer(text=f"{time.date().strftime('%Y')} Derek Lee. All rights reserved.")
        # await ctx.send(":slight_smile:")
        # await ctx.send(str("""```bash\nThis is some colored Text```"""))
        # await ctx.send(embed=embed, file=file)
        await ctx.send(embed=embed)


    @commands.group()
    async def test(self, ctx):
        pass
    
    @test.command()
    async def test1(self, ctx):
        await ctx.send('test1')

    @test.command()
    async def test2(self, ctx):
        await ctx.send('test2')

    @commands.command()
    async def tt(self, ctx, msg):
        print(str(ctx.command))
        await ctx.send(msg)
        
def setup(bot):
    bot.add_cog(Main(bot)) # execute this line first to set up