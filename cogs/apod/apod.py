'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-07-29 17:36:13
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-30 00:22:10
FilePath: \discord_bot_repo\cogs\apod\apod.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''

from dataclasses import dataclass
import string
from typing import Optional
import nextcord
from nextcord.ext import commands
from numpy import equal
from core.classes import Cog_Extension
import requests
from pathlib import Path
import json
import urllib
import os
from dotenv import load_dotenv
from datetime import date, datetime,timezone
import time

# load setting.json file and enviroment variables
with open ('setting.json', 'r', encoding='utf8') as json_file:
    json_data = json.load(json_file)
load_dotenv()

class Apod(Cog_Extension):
    COG_EMOJI = '🪐'

    @commands.command()
    async def apod(self, ctx: commands.Context, arg:Optional[str] = None): # pic_num # hd
        if arg and arg != '-r':
            await ctx.send('something went wrong...')
            return

        arg = f"&count=1" if arg else ''
        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={os.getenv('NASA_KEY')}{arg}")
        context = response.json()[0] if arg else response.json()

        site_link = 'https://apod.nasa.gov/apod/astropix.html' if not arg else f"https://apod.nasa.gov/apod/ap{context['date'][2:4]}{context['date'][5:7]}{context['date'][8:10]}.html"
        now_time = datetime.now(tz=timezone.utc)
        embed = nextcord.Embed(title=f"**{self.COG_EMOJI} Astronomy Picture of the Day**", url=site_link, description=f"Date: {context['date']}", color=0x00FF7F, timestamp=now_time)
        
        explanation = ""
        for word in context['explanation'].split():
            if len(explanation) > 128:
                break
            explanation += f" {word}"
        
        embed.add_field(name=f"**{context['title']}**", value=f"{explanation} ...... [Read More]({site_link})")   
        file = nextcord.File(Path(json_data['nasa_thumbnail']))
        embed.set_thumbnail(url=f"attachment://{file.filename}")

        if context['media_type'] == 'image':
            embed.set_image(context['url'])
        else:
            embed.add_field(name=f"😢Unsupported Media Type:{context['media_type']}", value=f"[Link]({context['url']})")
        try:
            embed.set_footer(text=f"©️ {context['date'][0:4]}~{now_time.date().strftime('%Y')} {context['copyright']}. All rights reserved.")
        except KeyError:
            # print(context)
            embed.set_footer(text=f"Author Not Found. Click [Read More] for more details.")
        await ctx.reply(embed=embed, file=file, mention_author=False)

    @commands.command()
    async def testing(self, ctx):
        embed=nextcord.Embed(description='https://www.youtube.com/watch?v=1IlTeOMCNJU')
        embed.add_field(name='123', value='https://www.youtube.com/watch?v=1IlTeOMCNJU')
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Apod(bot))