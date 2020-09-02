import logging
from logging.handlers import RotatingFileHandler
import random
import sqlite3
import traceback
import time
import datetime #
import sys
import os
import hashlib
import asyncio
import aiohttp
from collections import Counter
from pytz import timezone #
import discord #
from discord.ext import commands #
import loadconfig #

description = '''Expat's feature rich discord bot, developed with discord.py \n
                 All the command are available at https://github.com/TheLastNever/discord_bot/blob/master/README.md: '''
bot = commands.Bot(command_prefix=loadconfig.__prefix__,description=description)


def _currenttime():
    return datetime.datetime.now(timezone('Asia/Istanbul')).strftime('%H:%M%S')

async def _randomGame():
    while True:
        guildCount = len(bot.guilds)
        memberCount = len(list(bot.get_all_members()))
        randomGame = random.choice(loadconfig.__games__)
        await bot.change_presence(activity=discord.Activity(type=randomGame[0],name = randomGame[1].format(guilds = guildCount , members= memberCount)))
        await asyncio.sleep(loadconfig.__gamesTimer__) 
@bot.event
async def on_ready():
    ''' To see the starting of the bot '''
    if bot.user.id == 745768346938769508 :
        bot.dev = True
    else:
        bot.dev = False
    print('Logged in as')
    print(f'Bot-Name: {bot.user.name}')
    print(f'Bot-ID: {bot.user.id}')
    print(f'Dev MODE: {bot.dev} ')
    bot.AppInfo = await bot.application_info()
    print(f'Owner: {bot.AppInfo.owner}')
    print('--------')
    for cog in loadconfig.__cogs__:
        try:
            bot.load_extension(cog)
        except Exception:
            print(f'This cog couldn\'t be loaded {cog}')

    bot.startTime = time.time()
    bot.gamesLoop = asyncio.ensure_future(_randomGame())
   
@bot.event
async def on_message(message):
    ErdoSoz = ["Ezanımızı türkçe okuttular yeğenim","akp\'ye laf yokkkkk","Çalıyo Ama Yapıyo","Diğerleri Gelse Nabacak Kardeşim","Kılıçdaroğlunda liderlik vasfı yok bi kere","Almanycıyım keşke türkiyede yaşasam","Bazılarının Gözünde Silivri hasreti görüyorum!!","Eskiden Buzdolabı Yoktu","Ekmeği Karneyle alıyoduk","Bu Millet 15 Temmuzda tankları durdurdu kardeşim","senin telefon kullanman lüks","Burası ÇOKOMELLİ"]
    keyWords =[ 'akp' , 'erdoğan'  , 'ak parti' , 'hükümet' , 'tayyip' , 'tayip' , 'hükümet','çomar']
    a = str(message.content.lower())
    res = [ele for ele in keyWords if(ele in a)] 
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        await message.author.send('Üzgünüm ama özel mesajdan komut almıyorum! :/ Server içinden dene lütfen')
    if 'cahil' in message.clean_content.lower():
        await message.channel.send('Ne hakla cahil diyorsun kardeşim sen?!!')
 
    # Make it clearer with clean_content method
    if bool(res):
        response = random.choice(ErdoSoz) 
        await message.channel.send(f'{message.author.name} öhöm öhöm ')
        await message.channel.send(response)





if __name__ == '__main__':
    bot.run(loadconfig.__token__)