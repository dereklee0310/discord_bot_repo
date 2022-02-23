from sqlite3 import Timestamp
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')

    @commands.command()
    async def say_something(self, ctx):
        await ctx.send('hello its me :)')
    
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="test title(links of generator)", url="https://cog-creators.github.io/discord-embed-sandbox/", description="this is a descrpition", color=0x007180, timestamp=datetime.datetime.now())
        embed.set_author(name="derek", url="https://wallhere.com/zh/wallpaper/2002393", icon_url="https://c.wallhere.com/photos/3e/65/anime_anime_girls_Null_Makima_Chainsaw_Man_Chainsaw_Man-2002393.jpg!d")
        embed.set_thumbnail(url="https://previews.123rf.com/images/dustin999/dustin9992008/dustin999200800099/153515139-mountain-icon-vector-mountain-icon-black-on-white-background-mountain-hills-icon-simple-and-modern-d.jpg")
        embed.add_field(name="test field1", value="field value", inline=False)
        embed.set_footer(text="this is a footer text")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

def setup(bot):
    bot.add_cog(Main(bot))