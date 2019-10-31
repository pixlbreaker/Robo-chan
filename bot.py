import discord
import json

from discord.ext import commands

# Token and the bot
f = open("info.json")
data = json.load(f)
TOKEN = data['TOKEN']

bot = commands.Bot(command_prefix="!")

# Adds the Cogs
bot.load_extension("rnd")
# Run the bot
bot.run(TOKEN)