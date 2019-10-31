import discord
import json

# Token and the bot
f = open("info.json")
data = json.load(f)
TOKEN = data['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print("Welcome! we have logged on")

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return
    
    if ctx.content.startswith("$hello"):
        await ctx.channel.send('Hello!')

# Run the bot
client.run(TOKEN)