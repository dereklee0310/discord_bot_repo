'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-06-30 23:16:17
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-08 23:05:05
FilePath: \discord_bot_repo\lib\func.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''
import time
import discord
from discord.ext import commands

def is_text_channel(channel_type):
    if channel_type == discord.ChannelType.text:
        return True
    return False

# def is_valid_command(command_name, cog_table):
#     if command_name in cog_table:
#         return True
#     return False


# https://docs.python.org/zh-tw/3/library/datetime.html#strftime-and-strptime-behavior
def format_time(str):
    # print(type(str))
    struct_time = time.strptime(str, "%Y-%m-%d %H:%M:%S")
    tmp = time.strftime("%m %d %I%p", struct_time)
    # 0123456789012345
    # 07 09 06PM
    r_str = list(tmp)
    if int(tmp[6:8]) < 10:
        r_str[6:8] = f"{int(tmp[6:8])}"
    r_str[2] = '/'

    return ''.join(r_str)