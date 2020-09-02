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
bot = commands.Bot(command_prefix='.',description=description)


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
    Sayings = loadconfig.__SayingE__
    keyWords = loadconfig.__keyWordsE__
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
        response = random.choice(Sayings) 
        await message.channel.send(f'{message.author.name} öhöm öhöm ')
        await message.channel.send(response)
@bot.event
async def on_member_join(member):
    dm = f"{member.name} , {loadconfig.__greetmsg__}"
    print(dm)
    await member.create_dm()
    await member.dm_channel.send(dm)


@bot.event
async def on_error(event, *args, **kwargs):
    if bot.dev:
        traceback.print_exc()
    else:
        embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
        embed.add_field(name='Event', value=event)
        embed.description = '```py\n%s\n```' % traceback.format_exc()
        embed.timestamp = datetime.datetime.utcnow()
        try:
            await bot.AppInfo.owner.send(embed=embed)
        except:
            pass

@bot.event
async def on_command_error(ctx,error):
    send_help = (commands.MissingRequiredArgument, commands.BadArgument, commands.TooManyArguments, commands.UserInputError)
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Nabıyon ln")
        #pass
    elif isinstance(error,send_help):
        _help = await send_cmd_help(ctx)
        await ctx.send(embed=_help)
#ERROR HAKKINDA KULLANICIYA BİLGİ VERSİN DİYE
async def send_cmd_help(ctx):
    cmd = ctx.command
    em = discord.Embed(title=f'Usage: {ctx.prefix + cmd.signature}')
    em.color = discord.Color.green()
    em.description = cmd.help
    return em


if __name__ == '__main__':
    bot.run(loadconfig.__token__)