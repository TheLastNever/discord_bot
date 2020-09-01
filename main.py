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
print(description)

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
    bot.commands_used = Counter()
    bot.startTime = time.time()
   # bot.gamesLoop = asyncio.ensure_future(_randomGame())

def _currenttime():
    return datetime.datetime.now(timezone('Asia/Istanbul')).strftime('%H:%M%S')



if __name__ == '__main__':
    bot.run(loadconfig.__token__)