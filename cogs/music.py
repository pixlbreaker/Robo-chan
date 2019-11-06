import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Music Cog ...')
    
    @commands.command(pass_context=True)
    async def join(self, ctx):
        '''Joins the users channel'''
        channel = ctx.message.author.voice.voice_channel
        await ctx.join_voice_channel(channel)

def setup(bot):
    bot.add_cog(Music(bot))