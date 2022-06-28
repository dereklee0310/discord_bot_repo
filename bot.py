'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-18 22:07:14
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-06-28 17:31:45
FilePath: \discord_bot_repo\bot.py
'''
from distutils import extension
from msilib.schema import File
import discord
from discord.ext import commands # https://discordpy.readthedocs.io/en/stable/ext/commands/index.html
import json
import random
import os

with open ('setting.json', 'r', encoding='utf8') as jfile: # open setting.json, and use jfile as the instance
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents) # instance of bot

@bot.event
async def on_ready():
    print("bot is online") # start message

# load all extension in cmds directory
cog_table = {}
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        cog_table[filename[:-3]] = True
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def load(ctx, *args): # ctx: context that include all information
    if len(args) == 0: # default: load all cogs
        await ctx.send('Loading all unloaded cogs...')
        for key, value in cog_table.items(): # for filename in os.listdir('./cmds'):
            if value == False:
                bot.load_extension(f'cmds.{key}')
                value = True
                await ctx.send(f'{key} was loaded successfully.')
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
        await ctx.send('no cog will be unloaded, use `!unload [cog name]` to unload any loaded cog')
    else:
        for arg in args:
            if arg not in cog_table:
                await ctx.send(f'The cog {arg} doesn\'t exist!')
                continue
            if cog_table[arg] == False:
                await ctx.send(f'The cog {arg} is already unloaded!')
                continue

            # when the cog name is valid and it hasn't been unloaded
            cog_table[arg] = False
            bot.unload_extension(f'cmds.{arg}')
            await ctx.send(f'{arg} was unloaded successfully.')

@bot.command()
async def reload(ctx, *args):
    if len(args) == 0: # send warning
        await ctx.send('no cog will be reloaded, usage: `!reload [cog name]`')
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
    bot.run(jdata['TOKEN']) # start the bot