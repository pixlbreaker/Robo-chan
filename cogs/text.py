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
        """Says Hello!"""
        await ctx.send("Hello", tts=self.tts)
    
    @commands.command()
    async def ping(self, ctx):
        """Ping! Pong! Ping! Pong!"""
        await ctx.send('Pong!', tts=self.tts)

    @commands.command()
    async def uwu(self, ctx):
        """UWU XD"""
        await ctx.send("Stop it Oni-chan ;)", tts=self.tts)
    
    @commands.command()
    async def date(self, ctx):
        """Gives the current date and time"""
        today = dt.datetime.today()
        await ctx.send(today.ctime())
    
    @commands.command()
    async def tts_on(self, ctx):
        """Turns on tts"""
        self.tts = True
        await ctx.send("Your wish is my command", tts=self.tts)
    
    @commands.command()
    async def tts_off(self, ctx):
        """Turns off tts"""
        self.tts = False
        await ctx.send("Aww!! Okay goodbye!!", tts=self.tts)
    
    @commands.command()
    async def fact(self, ctx):
        """Gets a random fact from the fact database"""
        #From the program's perspective you are at bot.py
        os.chdir("data")
        f = open("facts.txt")
        lines = f.readlines()
        num = random.randint(0, len(lines))
        # Changes back to the root directory
        os.chdir("..")
        await ctx.send(lines[num])

def setup(bot):
    bot.add_cog(Text(bot))