from discord.ext import commands

###############
# Text Cogs
################
class Text():

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command
    async def hello(self, ctx):
        await self.bot.say("Hello")

    async def on_message(self, message):
        print(message.content)

def setup(bot):
    bot.add_cog(Text(bot))