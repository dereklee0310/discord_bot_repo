'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-18 22:07:14
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-07-12 02:07:30
FilePath: \discord_bot_repo\bot.py
'''
import discord
from discord.ext import commands # https://discordpy.readthedocs.io/en/stable/ext/commands/index.html
import json
import os
from dotenv import load_dotenv
from pathlib import Path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#todo handle the default help command that can't be used in text channel in voice channel

#todo handle exception: discord.ext.commands.errors.CommandNotFound: Command "piyan" is not found

with open (Path('./setting.json'), 'r', encoding='utf8') as jfile: # open setting.json, and use jfile as the instance
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents) # instance of bot

@bot.event
async def on_ready():
    print("bot is online") # start message

cog_table = {}
# load all extension in cmds directory
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        cog_table[filename[:-3]] = True
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def load(ctx, *args): # ctx: context that include all information
    if len(args) == 0: # default: load all cogs
        await ctx.send('Loading all unloaded cogs...')
        is_any_loaded = False
        for key, value in cog_table.items(): # for filename in os.listdir('./cmds'):
            if value == False:
                bot.load_extension(f'cmds.{key}')
                cog_table[key] = True
                await ctx.send(f'{key} was loaded successfully.')
                is_any_loaded = True
        if is_any_loaded == False:
            await ctx.send('All cogs up-to-date')

    else: # load specific cogs
        for arg in args:
            if arg not in cog_table:
                await ctx.send(f'The cog {arg} doesn\'t exist!')
                continue
            if cog_table[arg] == True:
                await ctx.send(f'The cog {arg} is already loaded!')
                continue

            # when the cog name is valid and it hasn't been loaded
            bot.load_extension(f'cmds.{arg}')
            cog_table[arg] = True
            await ctx.send(f'{arg} was loaded successfully.')

@bot.command()
async def unload(ctx, *args):
    if len(args) == 0: # send warning
        await ctx.send('No cog will be unloaded, use `!unload [cog name]` to unload any loaded cog')
    else:
        for arg in args:
            if arg not in cog_table:
                await ctx.send(f'The cog {arg} doesn\'t exist!')
                continue
            if cog_table[arg] == False: 
                await ctx.send(f'The cog {arg} is already unloaded!')
                continue

            # when the cog name is valid and it hasn't been unloaded
            bot.unload_extension(f'cmds.{arg}')
            cog_table[arg] = False
            await ctx.send(f'{arg} was unloaded successfully.')

@bot.command()
async def reload(ctx, *args):
    if len(args) == 0: # send warning
        await ctx.send('No cog will be reloaded, usage: `!reload [cog name]`')
    else:
        for arg in args:
            if arg not in cog_table:
                await ctx.send(f'The cog {arg} doesn\'t exist!')
                continue
            if cog_table[arg] == False:
                await ctx.send(f'The cog {arg} hasn\'t been loaded, use `!load {arg}` to load it first')
                continue

            bot.reload_extension(f'cmds.{arg}')
            await ctx.send(f'{arg} was reloaded successfully.')

if __name__ == "__main__":
    # bot.run(jdata['TOKEN']) # start the bot
    load_dotenv()
    bot.run(os.getenv("DISCORD_TOKEN"))