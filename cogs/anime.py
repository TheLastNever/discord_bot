import discord
from discord.ext import commands
class anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    





    
def setup(bot):
    bot.add_cog(anime(bot))