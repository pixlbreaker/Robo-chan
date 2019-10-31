from discord.ext import commands

###############
# Text Cogs
################
class TextCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.command
    async def acommand(self, ctx, argument):
       await self.bot.say("Stuff")
    
    @commands.command
    async def hello(self, ctx):
        await ctx.send("Hello!")

    async def on_message(self, message):
        print(message.content)

def setup(bot):
    bot.add_cog(TextCog(bot))