import asyncio
import random
import discord
from discord.ext import commands
class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    

    # ROLL A DICE
    @commands.command(name='Roll', aliases =['roll','r'],help='Zar atar: zar sayısı ve zar yüzü belirlenmeli')
    async def roll(self,ctx, number_of_dice: int, number_of_sides: int):
        if number_of_dice > 20 :
            await ctx.send("Daha küçük sayılar seç ")
        else:
            dice = [
                str(random.choice(range(1, number_of_sides + 1)))
                for _ in range(number_of_dice)
            ]
            await ctx.send(', '.join(dice))


    # Yazı tura
    @commands.command(name='Yazi_tura' , aliases =['yt','cf','coinflip'] , help = 'Yazı Tura atar : kaç adet para atılacağı yazılmalı')
    async def yaziTura(self,ctx, number_of_change:int):
        tura = ['YAZI', 'TURA']
        if number_of_change > 20 :
            await ctx.send("20'den fazla bozukluğu ne yapacan ?")
        else:
            yazi = [
                str(random.choice(tura))
                for _ in range(number_of_change)
            ]
            channel = self.bot.get_channel(746686244368678912)
            
            print(channel)
            await channel.send("naber")
            await ctx.send(' :: '.join(yazi))
           


def setup(bot):
    bot.add_cog(fun(bot))