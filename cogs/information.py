import asyncio
import discord
from discord.ext import commands
from pytz import timezone
import datetime
class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name = 'Hakkinda', aliases= ['hakkinda','about'], help = "Klasik Hakkinda Sayfası")
    async def about(self,ctx):
        em = discord.Embed(color=discord.Color.green())
        em.title = 'Bot Bilgisi'
        em.set_thumbnail(url='https://i.ytimg.com/vi/38CLxTx4898/maxresdefault.jpg')
        em.set_author(name='Yüce Kralımız Ahmey Bey Hazretleri',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRqCGRys6rLHWqRrkA2_zirxRHR6SBewN1lcw&usqp=CAU')
        em.description = "Çok Olanaklı Yapımcımın İsteklerine Göre Şekillenecek Bir Uygulama"
        em.set_image(url='https://c12.incisozluk.com.tr/res/incisozluk//11505/4/834364_o67cd.png')
        em.add_field(name='Anime' ,value= 'Animeyi Sevmeyen bu gruptan  gidebilir')
        em.add_field(name='Dil Kanalı', value='Japonca,İngilizce Bi şeyler Ekleyin Şu  SUB\'LARINA ALOOOO ')
        em.add_field(name='Kaynak',value='Şuraya da bi şeyler ekleyin ')
        em.set_footer(text='YENİ ÖZELLİKLER DÜŞÜNÜRSENİZ -Öneri komutunu kullanın',icon_url='https://i.ytimg.com/vi/t4x1AxYdusc/hqdefault.jpg')
  
        await ctx.send(embed=em)   


    @commands.command(name = 'suggest', help = 'Öneri Kanalına Bot Hakkında Önerilerinizi Gönderir')
    async def suggestion(self,ctx,*args):
        channel = bot.get_channel(746686244368678912)
        #em = discord.Embed(color = discord.Color.red())
        #em.title = 'DEĞERLİ ÖNERİ'
        #em.set_author(name=ctx.author.name, icon_url="https://previews.123rf.com/images/bankrx/bankrx1703/bankrx170300012/73008857-grunge-red-suggestion-with-star-icon-round-rubber-seal-stamp.jpg")
        #em.description = " ".join(args[:])
        #print(em.title)
        #await ctx.send(embed= em)
        await channel.send("Naber")


def setup(bot):
    bot.add_cog(information(bot))