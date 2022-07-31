'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-20 14:44:52
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-21 21:59:28
FilePath: \discord_bot_repo\core\classes.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''
import nextcord
from nextcord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot