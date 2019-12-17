import os
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
        self.tts = False
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Text Cog ...')
    
    @commands.command()
    async def logout(self, ctx):
        await self.bot.logout()
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello", tts=self.tts)
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!', tts=self.tts)

    @commands.command()
    async def uwu(self, ctx):
        await ctx.send("Stop it Oni-chan ;)", tts=self.tts)
    
    @commands.command()
    async def date(self, ctx):
        today = dt.datetime.today()
        await ctx.send(today.ctime())
    
    @commands.command()
    async def tts_on(self, ctx):
        self.tts = True
        await ctx.send("Your wish is my command", tts=self.tts)
    
    @commands.command()
    async def tts_off(self, ctx):
        self.tts = False
        await ctx.send("Your wish is my command", tts=self.tts)
    
    @commands.command()
    async def fact(self, ctx):
        #From the program's perspective you are at bot.py
        os.chdir("data")
        f = open("facts.txt")
        lines = f.readlines()
        num = random.randint(0, len(lines))
        await ctx.send(lines[num])



def setup(bot):
    bot.add_cog(Text(bot))