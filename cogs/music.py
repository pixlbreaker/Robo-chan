import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Music Cog ...')
    
    @commands.command(pass_context=True)
    async def join(self, ctx):
        '''Joins the users channel'''
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegPCMAudio('1.m4a')
        player = voice.play(source)

def setup(bot):
    bot.add_cog(Music(bot))