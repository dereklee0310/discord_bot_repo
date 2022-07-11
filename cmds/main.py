'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-20 14:27:58
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-11 19:07:39
FilePath: \discord_bot_repo\cmds\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE   
'''
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests
from pathlib import Path
import json

with open ('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class Main(Cog_Extension):

    # return the latency of bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')

    @commands.command()
    async def hey(self, ctx):
        await ctx.send('hello its me :)')

    @commands.command()
    async def aquatrail(self, ctx):
        await ctx.send('那你很棒欸 老弟<:test:993523987520950352>') #todo move this to setting.json

    @commands.command()
    # keyword-only argument: https://segmentfault.com/a/1190000005173136
    async def sayitforme(self, ctx, *, msg): # use * to get all arguments
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def purge(self, ctx, num: int):
        await ctx.channel.purge(limit=num + 1) # + 1 for the command message itself

    ################################################################### DIVIDING LINE ##################################################################################
    
    @commands.command()
    async def profile(self, ctx): #todo create a chinese version profile !! let user set his language using another command and send the message according his setting.
        from datetime import datetime,timezone,timedelta
        time = datetime.now(tz=timezone.utc)
        file = discord.File(Path(jdata['bot_icon']))
        embed=discord.Embed(title="***Hi, I am Not a Bot, designed to best serve your needs***", color=0x80FFEC, timestamp=time)
        embed.set_author(name="Not a Bot", url=jdata['rick_roll'], icon_url=f"attachment://{file.filename}")

        empty = "\u200b"
        embed.add_field(name="Type `!help` to get started \U0001F913", value='**Main Features:**', inline=False)
        embed.add_field(name="\U0001F324 Taiwan Weather Forecast", value="```!forecast [county name]```", inline=True)
        embed.add_field(name="TBD", value="```![TBD]```", inline=True)

        slight_smile = "\U0001f642"
        # embed.add_field(name=f"If you encounter problems enjoying my service or have any cool idea about my new feature, please contact the developer. {slight_smile}", value=empty, inline=False)
        embed.add_field(name=empty, value=f"**If you encounter problems enjoying my service or have any cool\n idea about my new feature, please contact the developer. {slight_smile}**", inline=False)
        embed.add_field(name="\U0001F914 Discord", value="```DEREK#5958```", inline=True)
        embed.add_field(name="\U00002709 Gmail", value="```dereklee0310@gmail.com```", inline=True)
        embed.set_footer(text=f"{time.date().strftime('%Y')} Derek Lee. All rights reserved.")
        # await ctx.send(":slight_smile:")
        # await ctx.send(str("""```bash\nThis is some colored Text```"""))
        await ctx.send(embed=embed, file=file)

    @commands.command()
    async def weather(self, ctx, county):
        response = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC")
        data = response.json()['records']['location']
        report = f"Now Showing: future 36 hours weather forecast of {county}"
        for i in data:
            if i['locationName'] != county:
                continue
            # report += (f"                 {i['locationName']}\n")
            # report += '-----------------------------------------\n'
            report += '```'
            for j in i['weatherElement']:
                if j['elementName'] == 'Wx':
                    for k in j['time']:
                        report += f"{k['startTime']} ~ {k['endTime']}\n"
                        report += f"{k['parameter']['parameterName']}\n"
            # report += '-----------------------------------------'
            report += '```'
        await ctx.send(report)

    @commands.command()
    async def orgtime_forecast(self, ctx, county):
        from datetime import datetime,timezone,timedelta
        time = datetime.now(tz=timezone.utc)
        embed=discord.Embed(title=f"**Weather Forecast**", url='https://www.cwb.gov.tw/V8/C/W/County/index.html', color=0x80FFEC, timestamp=time)

        response = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC")
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
    async def forecast(self, ctx, org_county): #todo use reply!
        import json
        with open ('setting.json', 'r', encoding='utf8') as jfile: # open setting.json, and use jfile as the instance
            jdata = json.load(jfile)

        county = org_county.replace('台', '臺') # convert '台' to '臺' if any
        if county not in jdata['county']:
            await ctx.reply(f"County {county} doesn't exists!", mention_author=False)
            return

        # https://blog.csdn.net/u014663232/article/details/103501574
        import urllib
        county_utf8 = urllib.parse.quote(county)
        # open weather data: https://opendata.cwb.gov.tw/dataset/forecast/F-C0032-001
        # forecast element: https://opendata.cwb.gov.tw/opendatadoc/MFC/ForecastElement.pdf
        response = requests.get(f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1F4F2B0A-81C7-4A39-858B-7A8DACED51AC&locationName={county_utf8}")
        data = response.json()['records']['location']
        
        #* another approach: https://rnnnnn.medium.com/python3-%E5%8F%96%E5%BE%97%E7%8F%BE%E5%9C%A8%E6%99%82%E9%96%93-%E8%A8%AD%E5%AE%9A%E6%99%82%E5%8D%80-8b29380f9dbb
        # from datetime import datetime,timezone,timedelta
        # dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        # dt2 = dt1.astimezone(tz=timezone(timedelta(hours=8)))
        # now_time = datetime.now(tz=timezone.utc)
        from datetime import datetime,timezone,timedelta
        now_time = datetime.now(tz=timezone.utc)
        embed = discord.Embed(title=f"**Taiwan Weather Forecast**", url='https://www.cwb.gov.tw/V8/C/W/County/index.html', color=0x80FFEC, timestamp=now_time)
        filename = county_utf8.replace('%', '') + ".png"
        # path reference: https://www.gushiciku.cn/pl/2SvB/zh-tw
        from pathlib import Path
        
        file = discord.File(Path(jdata['county_icon_dir']) / filename)
        embed.set_thumbnail(url=f"attachment://{file.filename}")

        empty = "\u200b"
        embed.add_field(name=f'Next 36h Weather Forecast of **{county}**', value=empty, inline=False)
        
        from func import format_time

        #? compute time (name entry)
        time = ['', '', '']
        for i in range(len(time)):
            entry = data[0]['weatherElement'][0]['time']
            time[i] += format_time(entry[i]['startTime']) + ' ~ '
            # end_year = '' if int(entry[i]['startTime'][0:4]) == int(entry[i]['endTime'][0:4]) else f"{entry[i]['endTime'][0:4]} " # use original time format to compare year entry, assign '' or '20XX '
            end_year = f"{entry[i]['endTime'][0:4]} "
            end_time = format_time(entry[i]['endTime'])
            time[i] += end_year + end_time

        # 3 time block in each weather element block
        info = ['', '', '']
        for i in range(3):
            #? add emoji or not?
            # reference: http://163.28.10.78/content/junior/earth/tp_tm/new/item0402/knowledge/w3.htm
            if (int(data[0]['weatherElement'][2]['time'][i]['parameter']['parameterName']) + int(data[0]['weatherElement'][4]['time'][i]['parameter']['parameterName'])) / 2 > 29:
                icon = '\U0001F975'
            elif (int(data[0]['weatherElement'][2]['time'][i]['parameter']['parameterName']) + int(data[0]['weatherElement'][4]['time'][i]['parameter']['parameterName'])) / 2 < 19:
                icon = '\U0001F976'
            else:
                icon = '\U0001F642'

            # example: # []28 ~ 32°C []晴時多雲 []降雨機率20%
            info[i] += icon
            info[i] += data[0]['weatherElement'][2]['time'][i]['parameter']['parameterName']
            info[i] += '~'
            info[i] += data[0]['weatherElement'][4]['time'][i]['parameter']['parameterName']
            info[i] += chr(0xb0) + 'C'
            info[i] += ' '
            tmp = int(data[0]['weatherElement'][0]['time'][i]['parameter']['parameterValue'])
            if tmp == 1:
                icon = '\U00002600'
            elif tmp == 2:
                icon = '\U0001F324'
            elif tmp == 3:
                icon = '\U0001F324' # '\U000026C5'
            elif tmp >= 4 and tmp <= 7:
                icon = '\U00002601'
            elif tmp >= 8 and tmp <= 22:
                icon = '\U0001F327'
            elif tmp == 23:
                icon = '\U0001F328'
            elif tmp >= 24 and tmp <= 28:
                icon = '\U0001F32B'
            elif tmp >= 29 and tmp <= 41:
                icon = '\U0001F327'
            else:
                icon = '\U00002744'
            info[i] += icon
                 
            info[i] += data[0]['weatherElement'][0]['time'][i]['parameter']['parameterName']
            info[i] += ' '
            info[i] += '\U00002600' if int(data[0]['weatherElement'][1]['time'][i]['parameter']['parameterName']) <= 50 else '\U0001F327'
            info[i] += '降雨機率'
            info[i] += data[0]['weatherElement'][1]['time'][i]['parameter']['parameterName']
            info[i] += '%'

        for i, j in zip(time, info):
            #todo convert ```[something]``` to a macro
            embed.add_field(name=i, value=f'```{j}```', inline=False)

        #* format test
        # import time
        # # entry = data[0]['weatherElement'][0]['time'][0]
        # tmp = entry['startTime']
        # # https://docs.python.org/zh-tw/3/library/datetime.html#strftime-and-strptime-behavior
        # struct_time = time.strptime(tmp, "%Y-%m-%d %H:%M:%S")
        # # new_tmp = time.strftime("%Y %b %d %I:%M %p", struct_time) # 2022 Jul 09 06:00 PM
        # new_tmp = time.strftime("%Y %m %d %a %I:%M %p", struct_time)
        # print(new_tmp)
        
        copyright = '\U000000A9'
        embed.set_footer(text=f"{copyright}{now_time.date().strftime('%Y')} Derek Lee. All rights reserved.")
        await ctx.reply(embed=embed, file=file, mention_author=False)

    # @forecast.error
    # async def forecast_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send('somthing wrong...')
    #         return

    # @commands.Cog.cog_command_error()
    # async def checker(self, ctx, error):
    #     if ctx.command.has_error_handler():
    #         return
    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, command_exception):
    #     if isinstance(command_exception, commands.MissingRequiredArgument):
    #         await ctx.send('somthing wrong...')
    #         return

    @commands.command()
    async def t(self, ctx):
        self.bot.reload_extension(f'cmds.main') #! just for test
        await ctx.invoke(self.bot.get_command('forecast'), org_county="高雄市")
    @commands.command()
    async def t1(self, ctx):
        await ctx.reply('123')

def setup(bot):
    bot.add_cog(Main(bot)) # execute this line first to set up