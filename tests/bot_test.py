'''
Author: dereklee0310 dereklee0310.gmail.com
Date: 2022-02-14 22:27:13
LastEditors: dereklee0310 dereklee0310.gmail.com
LastEditTime: 2022-06-25 02:32:47
FilePath: \discord_bot_repo\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import discord
import time
import asyncio
import os
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print('user:', client.user)
    game = discord.Game('testing')
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'ping':
        await message.channel.send('pong')
    if message.content.startswith('say'):
        tmp = message.content.split(" ", 2)
        if len(tmp) == 1:
            await message.content.split('I have nothing to say')
        else:
            await message.channel.send(tmp[1])
    if message.content.startswith('change_status'):
        tmp = message.content.split(" ", 2)
        if len(tmp) == 1:
            await message.channel.send("can't change the status")
        else:
            game = discord.Game(tmp[1])
            await client.change_presence(status=discord.Status.idle, activity=game)
    if message.content.startswith('hello'):
        channel = message.channel
        await channel.send('hello')

        def checkmessage(m):
            return m.content == 'i say hello!' and m.channel == channel 
        msg = await client.wait_for('message', check=checkmessage) #reaction_add
        await channel.send('hello, {.author}!'.format(msg))
    if message.content == 'hehe':
        await message.delete()
        tmpmsg = await message.channel.send('lmao')
        await asyncio.sleep(3)
        await tmpmsg.delete()
    if message.content == 'group?':
        guilds = await client.fetch_guilds(limit=150).flatten()
        for i in guilds:
            await message.channel.send(i.name)


# client.run('OTQyNjQ0NTkwMTIzNTY1MDY3.YgngLw.6g-BrYo1_Bqa9EiPEyLPZpFegtM')
load_dotenv()
client.run(os.getenv('TOKEN'))