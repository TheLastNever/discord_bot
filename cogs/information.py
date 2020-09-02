import discord
from discord.ext import commands
class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    

## aliases koy commandlere böylece değişik yazsalar bile yazılabilir olsun##




    
def setup(bot):
    bot.add_cog(information(bot))