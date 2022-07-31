'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-07-25 16:41:13
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-28 16:45:33
FilePath: \discord_bot_repo\cogs\weather\weather.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension
import requests
from pathlib import Path
import json
import urllib
from .error import InvalidCountyError
import os
from dotenv import load_dotenv
from datetime import datetime,timezone
import time

# load setting.json file and enviroment variables
with open ('setting.json', 'r', encoding='utf8') as json_file:
    json_data = json.load(json_file)
load_dotenv()

class Weather(Cog_Extension):
    COG_EMOJI = '🌦️'

    # https://docs.python.org/zh-tw/3/library/datetime.html#strftime-and-strptime-behavior
    def format_time(self, str: str)-> str:
        struct_time = time.strptime(str, "%Y-%m-%d %H:%M:%S")
        tmp = time.strftime("%m %d %I%p", struct_time)
        # 0123456789012345
        # 07 09 06PM
        r_str = list(tmp)
        if int(tmp[6:8]) < 10:
            r_str[6:8] = f"{int(tmp[6:8])}"
        r_str[2] = '/'

        return ''.join(r_str)

    def validate_county(self, county: str) -> str:
        """fix typo of '台' and '臺', then validate it"""
        county = county.replace('台', '臺') # convert '台' to '臺' if any
        if county not in json_data['county']:
            raise InvalidCountyError
        return urllib.parse.quote(county) # https://blog.csdn.net/u014663232/article/details/103501574

    async def send_error_embed(self, ctx: commands.Context, error: str):
        """send error embed according to the error"""
        # embed=nextcord.Embed(title=f"**\U0000274C | Usage: `{json_data['usage'][str(ctx.command)]}`**", color=0XDC143C) # ❌= '\U0000274C'
        embed=nextcord.Embed(title=f"**\U0000274C | Usage: `{ctx.prefix}{ctx.command.qualified_name} {ctx.command.signature}`**", color=0XDC143C) # ❌= '\U0000274C'
        embed.set_footer(text=f"An error has occured: {json_data['error_table'][error]}")
        await ctx.reply(embed=embed, mention_author=False)
        # await ctx.send_help(ctx.command)
        # print(ctx.command.usage)
        # print(ctx.command.signature)
        #todo log the error

    @commands.command()
    async def orgtime_forecast(self, ctx: commands.Context, county: str)-> None:
        """origin time format of data (used for test)"""
        from datetime import datetime,timezone
        time = datetime.now(tz=timezone.utc)
        embed=nextcord.Embed(title=f"**Weather Forecast**", url='https://www.cwb.gov.tw/V8/C/W/County/index.html', color=0x80FFEC, timestamp=time)

        key = os.getenv('OPENDATA_KEY')
        response = requests.get(f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={key}")
        data = response.json()['records']['location']
        # report = f"Now Showing: future 36 hours weather forecast of {county}"
        for i in data:
            if i['locationName'] != county:
                continue
            for j in i['weatherElement']:
                if j['elementName'] == 'Wx':
                    for k in j['time']:
                        embed.add_field(name=f"{k['startTime']} ~ {k['endTime']}\n", value=f"```{k['parameter']['parameterName']}\n```", inline=False)
        embed.set_footer(text=f"{time.date().strftime('%Y')} Derek Lee. All rights reserved.")
        await ctx.send(embed=embed)

    @commands.command()
    async def forecast(self, ctx: commands.Context, county: str)-> None:
        """
        Next 36h weather forecast in Taiwan
        
        Example:
        ```
        $forecast 高雄市
        ```
        """
        try:
            county_utf8 = self.validate_county(county)
        except InvalidCountyError:
            #todo log the error
            await self.send_error_embed(ctx, InvalidCountyError.__name__)
            return
        
        # open weather data: https://opendata.cwb.gov.tw/dataset/forecast/F-C0032-001
        # forecast element: https://opendata.cwb.gov.tw/opendatadoc/MFC/ForecastElement.pdf
        key = os.getenv('OPENDATA_KEY')
        response = requests.get(f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={key}&locationName={county_utf8}") #todo add key to Heroku
        data = response.json()['records']['location']
        
        # another approach: https://rnnnnn.medium.com/python3-%E5%8F%96%E5%BE%97%E7%8F%BE%E5%9C%A8%E6%99%82%E9%96%93-%E8%A8%AD%E5%AE%9A%E6%99%82%E5%8D%80-8b29380f9dbb
        # from datetime import datetime,timezone,timedelta
        # dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        # dt2 = dt1.astimezone(tz=timezone(timedelta(hours=8)))
        now_time = datetime.now(tz=timezone.utc)
        embed = nextcord.Embed(title=f"**Taiwan Weather Forecast**", url='https://www.cwb.gov.tw/V8/C/W/County/index.html', color=0x00FF7F, timestamp=now_time)
        filename = county_utf8.replace('%', '') + ".png"
        # path reference: https://www.gushiciku.cn/pl/2SvB/zh-tw    
        file = nextcord.File(Path(json_data['county_icon_dir']) / filename)
        embed.set_thumbnail(url=f"attachment://{file.filename}")
        empty = "\u200b"
        embed.add_field(name=f'Next 36h Weather Forecast of **{county}**', value=empty, inline=False)
        
        time = ['']*3
        entry = data[0]['weatherElement'][0]['time']
        for i in range(len(time)):
            start = self.format_time(entry[i]['startTime'])
            end_year = f"{entry[i]['endTime'][0:4]} " if int(entry[i]['startTime'][0:4]) != int(entry[i]['endTime'][0:4]) else ''
            end_time = self.format_time(entry[i]['endTime'])
            time[i] = f"{start} ~ {end_year}{end_time}"
            
        # 3 time blocks in each weather element block
        info = ['']*3
        for i in range(len(info)):
            min = int(data[0]['weatherElement'][2]['time'][i]['parameter']['parameterName'])
            max = int(data[0]['weatherElement'][4]['time'][i]['parameter']['parameterName'])
            # reference: http://163.28.10.78/content/junior/earth/tp_tm/new/item0402/knowledge/w3.htm
            if (min + max) / 2 > 29:
                icon = '\U0001F975' # 🥵
            elif (min + max) / 2 > 18:
                icon = '\U0001F642' # 🙂
            else:
                icon = '\U0001F976' # 🥶
            temperature = f"{icon}{min}~{max}°C" # °: chr(0xb0)

            tmp = int(data[0]['weatherElement'][0]['time'][i]['parameter']['parameterValue'])
            if tmp == 1:
                icon = '\U00002600' # ☀
            elif 2 <= tmp <= 3:
                icon = '\U0001F324' # 🌤
            elif 4 <= tmp <= 7:
                icon = '\U00002601' # ☁
            elif 8 <= tmp <= 22:
                icon = '\U0001F327' # 🌧
            elif tmp == 23:
                icon = '\U0001F328' # 🌨
            elif 24 <= tmp <= 28:
                icon = '\U0001F32B' # 🌫
            elif 29 <= tmp <= 41:
                icon = '\U0001F327' # 🌧
            else:
                icon = '\U00002744' # ❄
            wx = data[0]['weatherElement'][0]['time'][i]['parameter']['parameterName']
            weather = f" {icon}{wx} " if len(wx) <= 6 else f"{icon}{wx}" 

            prob = int(data[0]['weatherElement'][1]['time'][i]['parameter']['parameterName'])
            icon = '\U00002600' if prob <= 50 else '\U0001F327' # ☀ or 🌧
            precipitation = f"{icon}降雨機率{prob}%"
            info[i] = f"```{temperature}{weather}{precipitation}```" # example: # []28 ~ 32°C []晴時多雲 []降雨機率20%

        for i, j in zip(time, info):
            embed.add_field(name=i, value=j, inline=False)

        #* format test
        # import time
        # # entry = data[0]['weatherElement'][0]['time'][0]
        # tmp = entry['startTime']
        # # https://docs.python.org/zh-tw/3/library/datetime.html#strftime-and-strptime-behavior
        # struct_time = time.strptime(tmp, "%Y-%m-%d %H:%M:%S")
        # # new_tmp = time.strftime("%Y %b %d %I:%M %p", struct_time) # 2022 Jul 09 06:00 PM
        # new_tmp = time.strftime("%Y %m %d %a %I:%M %p", struct_time)
        # print(new_tmp)
        
        copyright = '©' # ©: chr(0xa9)
        embed.set_footer(text=f"{copyright}{now_time.date().strftime('%Y')} Derek Lee. All rights reserved.")
        await ctx.reply(embed=embed, file=file, mention_author=False)

    @commands.command()
    async def t(self, ctx):
        """
        quick reload weather cog and run &forecast 高雄市
        
        this is for testing :)
        """
        self.bot.reload_extension(f'cogs.weather.weather') #! just for test
        # await ctx.invoke(self.bot.get_command('forecast'), county="高雄市")
        await ctx.invoke(self.bot.get_command('forecast'), "高雄市")

    @forecast.error
    async def forecast_error_handler(self, ctx:commands.Context, error: commands.errors)-> None:
        '''error handler of forecast command'''
        if isinstance(error, commands.MissingRequiredArgument):
            #todo send_help?
            #todo log the error
            await self.send_error_embed(ctx, commands.MissingRequiredArgument.__name__)
        else:
            raise error
        
def setup(bot: commands.Bot)-> None:
    bot.add_cog(Weather(bot)) # execute this line first to set up