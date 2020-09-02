import os
from dotenv import load_dotenv

load_dotenv()

__token__ = os.getenv('DISCORD_TOKEN')
__botserverid__ = os.getenv('DISCORD_GUILD')
__prefix__ = '.' # Default is `.` You can change here
__greetmsg__ = os.getenv('GREETING_MESSAGE')