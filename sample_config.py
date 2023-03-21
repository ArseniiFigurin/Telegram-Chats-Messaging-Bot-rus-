import os
import time

class Config(object):

    # Get from my.telegram.org (or @UseTGXBot)
    API_ID = int(os.environ.get("API_ID", "27401020")


    # Get from my.telegram.org (or @UseTGXBot)
    API_HASH = os.environ.get("API_HASH", "3729fc432d01623f477178c4646df7c4")
    
    
    # Znachenie taimera
    Znachenie taimera = os.environ.get("Znachenie taimera", "60")


    # To record start time of bot
    BOT_START_TIME = time.time()
