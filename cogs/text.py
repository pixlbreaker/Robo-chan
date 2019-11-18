import random
import discord
import datetime as dt
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
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def uwu(self, ctx):
        await ctx.send("Stop it Oni-chan ;)", tts="True")
    
    @commands.command()
    async def date(self, ctx):
        today = dt.datetime.today()
        await ctx.send(today.ctime())
    
    # Trying to add reactions to a post
    # @commands.command()
    # async def love(self, ctx):
    #     await self.bot.add_reaction('❤️')

def setup(bot):
    bot.add_cog(Text(bot))