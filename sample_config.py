import os
import time

class Config(object):

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", "27401020")


    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "3729fc432d01623f477178c4646df7c4")
    
    
    # Znachenie taimera
    Znachenie_taimera = os.environ.get("Znachenie_taimera", "60")


    # To record start time of bot
    BOT_START_TIME = time.time()
