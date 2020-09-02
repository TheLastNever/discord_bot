import os 

configFile = os.path.join('.','config','config.py')

if os.path.isfile(configFile):
    try:
        from config.config import __token__
    except ImportError:
        raise Exception('__token__ has to be setted')
    try:
        from config.config import __prefix__
    except ImportError:
        __prefix__ = '.'
    try:
        from config.config import __botserverid__
    except  ImportError:
        __botserverid__ = 0
    try:
        from config.config import __greetmsg__
    except ImportError:
        __greetmsg__ = 'Naber'

        

from config.games import __games__,__gamesTimer__
from config.cogs import __cogs__
from config.sayings import __SayingE__,__keyWordsE__
