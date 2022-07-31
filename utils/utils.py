'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-06-30 23:16:17
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-27 18:11:06
FilePath: \\discord_bot_repo\\utils\\utils.py
Description: 

Copyright (c) 2022 by dereklee0310 dereklee0310.gmail.com, All Rights Reserved. 
'''
import nextcord

def is_text_channel(channel_type):
    if channel_type == nextcord.ChannelType.text:
        return True
    return False

# def is_valid_command(command_name, cog_table):
#     if command_name in cog_table:
#         return True
#     return False