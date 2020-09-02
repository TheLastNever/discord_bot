import discord
from discord.ext import commands
class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command(name = 'Create', help = 'Yeni Kanal Oluşturur')
    @commands.has_role('admin')
    async def create_channel(self,ctx,channel_name : str):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name= channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)
            await ctx.send("Yeni Kanal Kuruldu!")
# ROLL A DICE





    
def setup(bot):
    bot.add_cog(admin(bot))