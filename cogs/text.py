import random
import discord
from discord.ext import commands

###############
# Text Cogs
################
class Text(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Text Cog ...')
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello")

    @commands.command()
    async def uwu(self, ctx):
        await ctx.send("Stop it Oni-chan ;)")

    async def on_message(self, message):
        print(message.content)

def setup(bot):
    bot.add_cog(Text(bot))