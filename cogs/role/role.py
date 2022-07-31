from nextcord.ext import commands
from core.classes import Cog_Extension
from .role_view import RoleView

class Role(Cog_Extension, name='Role'):#todo name?
    @commands.Cog.listener()
    async def on_ready(self):
        '''add view decorator'''
        self.bot.add_view(RoleView())
    
    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx):
        await ctx.send('click a button!', view=RoleView())

def setup(bot):
    bot.add_cog(Role(bot)) # execute this line first to set up
