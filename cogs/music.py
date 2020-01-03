import discord
import pafy
import youtube_dl
from discord.ext import tasks, commands
from discord import FFmpegPCMAudio
from discord.utils import get


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.songs = []
        #self.play_queue.start()
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Music Cog ...')
    

    @tasks.loop()
    async def play_queue(self):
        if len(self.songs) > 0:

            audio_path = self.songs.pop()
            # Plays the audio in the channel
            guild = ctx.guild
            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
            audio_source = discord.FFmpegPCMAudio(audio_path)

            #self.songs.append(audio_source)
            if not voice_client.is_playing():
                voice_client.play(audio_source, after=None)


    @commands.command(pass_context=True)
    async def join(self, ctx):
        """Joins the users channel"""
        try:
            channel = ctx.message.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
                await ctx.send("Moved channel")
            else:
                voice = await channel.connect()
                await ctx.send("Joined channel")
        except:
            await ctx.send("You are not connected to a channel")
        
    
    @commands.command()
    async def leave(self, ctx):
        """Leaves the user channel"""
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await ctx.send("Disconnecting from channel")
            await voice.disconnect()
        else:
            await ctx.send("")
    
    @commands.command()
    async def play(self, ctx, url: str):
        """Plays the given url to the channel. It will replace any song that is currently playing"""

        # Gets the video and audio stream
        video = pafy.new(url)
        #self.songs[video.title] = video
        audio = video.getbestaudio()
        audio.download(filepath="audio")
        audio_path = "audio/" + audio.title + ".webm"

        # Plays the audio in the channel
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(audio_path)

        #self.songs.append(audio_source)
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            await ctx.send("Playing song")
        else:
            voice_client.pause()
            voice_client.play(audio_source, after=None)
            await ctx.send("Replacing song")
    
    @commands.command()
    async def queue(self, ctx, url):
        # Gets the video and audio stream
        video = pafy.new(url)
        #self.songs[video.title] = video
        audio = video.getbestaudio()
        audio.download(filepath="audio")
        audio_path = "audio/" + audio.title +".webm"

        # Plays the audio in the channel
        # guild = ctx.guild
        # voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        # audio_source = discord.FFmpegPCMAudio(audio_path)

        self.songs.append(audio_path)
        
    @commands.command()
    async def skip(self, ctx):
        self.songs.pop()
        self.play_queue.start()


    @commands.command()
    async def stop(self, ctx):
        """Stops the song that is playing in the channel."""

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        if voice_client.is_playing():
            voice_client.pause()
            await ctx.send("Okay! No more music :/")
        else:
            await ctx.send("But music wasn't playing")
    
    @commands.command()
    async def execute_66(self, ctx):
        
        await ctx.send("")
    
    # @commands.command()
    # async def resume(self, ctx):
    #     guild = ctx.guild
    #     voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
    #     #audio_source = discord.FFmpegPCMAudio(audio_path)
    #     if voice_client.is_playing():
    #         voice_client.resume()

def setup(bot):
    bot.add_cog(Music(bot))