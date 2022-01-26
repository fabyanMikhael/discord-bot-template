from discord.ext import commands

class general(commands.Cog):
    '''General Commands'''
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong.")

def setup(bot):
    bot.add_cog(general(bot))