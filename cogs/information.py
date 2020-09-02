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
        em.add_field(name='Anime' ,value= 'Animeyi Sevmeyen bu gruptan siktirolup gidebilir')
        em.add_field(name='Dil Kanalı', value='Japonca,İngilizce Bi şeyler Ekleyin Şu AmınaKoyduğumunun SUB\'LARINA ALOOOO ')
        em.add_field(name='Kaynak',value='Şuraya da bi şeyler ekleyin amınakoyim hevesiniz osuruk kadar değilmiş pu amını sikim')
        em.set_footer(text='YENİ ÖZELLİKLER DÜŞÜNÜRSENİZ HEMEN BENLE İLETİŞİME GEÇİN ZATEN ÖNERİ OLUŞTURMA ÖZELLİĞİ DE GETİRİCEM',icon_url='https://i.ytimg.com/vi/t4x1AxYdusc/hqdefault.jpg')
  
        await ctx.send(embed=em)   

## aliases koy commandlere böylece değişik yazsalar bile yazılabilir olsun##
def setup(bot):
    bot.add_cog(information(bot))