import discord
from discord.ext import commands
class utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name = 'Öneri', help = 'Öneri Kanalına Bot Hakkında Önerilerinizi Gönderir')
    async def suggestion(self,ctx,*args):
        channel = bot.get_channel(746139662522908686)
        em = discord.Embed(color = discord.Color.red())
        em.title = 'DEĞERLİ ÖNERİ'
        em.set_author(name=ctx.author.name, icon_url="https://previews.123rf.com/images/bankrx/bankrx1703/bankrx170300012/73008857-grunge-red-suggestion-with-star-icon-round-rubber-seal-stamp.jpg")
        em.description = " ".join(args[:])
        await channel.send(embed = em) 


    
def setup(bot):
    bot.add_cog(utilities(bot))