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

from config.games import __games__,__gamesTimer__
from config.cogs import __cogs__
