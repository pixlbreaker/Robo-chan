import random
import discord
from discord.ext import commands

class RNG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added RNG Cog ...')

    @commands.command()
    async def roll(self, ctx, dice : str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
            if rolls > 100 or limit > 100:
                await ctx.send('Please give a number smaller than 100')
                return
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def rnd(self, ctx, num):
        """Returns a random number from 1 to the given number"""
        try:
            n_num = int(num)
            rand_num = random.randint(1, n_num)
            await ctx.send(rand_num)
        except Exception:
            await ctx.send("Please enter a valid number")

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, *choices : str):
        """Chooses between multiple choices."""
        await choices.send(random.choice(choices))


def setup(bot):
    bot.add_cog(RNG(bot))