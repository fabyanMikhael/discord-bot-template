from discord.ext import commands

class admin(commands.Cog):
    '''General Commands'''
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def testadmin(self, ctx: commands.Context):
        await ctx.send("Admin command ran successfully!")

def setup(bot):
    bot.add_cog(admin(bot))