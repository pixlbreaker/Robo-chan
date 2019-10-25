import discord
import asyncio
import json
import time
import os
from urllib.request import Request, urlopen
from discord.ext import commands
from random import randint

# Token and the bot
f = open("info.json")
data = json.load(f)
TOKEN = data['TOKEN']
bot = commands.Bot(command_prefix = ".")

# Ready Event
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.online, game=discord.Game(name="All those Beats"))

@bot.command(pass_context=True)
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    
    # Send it to the user
    await ctx.send(latency)

@bot.command(pass_context=True)
async def join(ctx):
    '''
    Joins the users channel
    '''
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)

@bot.command(pass_context = True)
async def leave(ctx):
    '''
    Leaves the user channel
    '''
    #server = ctx.message.server
    voice_client = bot.get_guild(id)
    await voice_client.leave()


# Run the bot
bot.run(TOKEN)