
from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", "15584001"))
    API_HASH = getenv("API_HASH", "e12f1473abbeaaf8302bf2692efd98f6")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
 
    ADMIN = list(map(int, getenv("ADMIN", "7425490417 1509123054").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002276401285"))
    
    # database configs
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/Juf.mp4")
    
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4 https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4 https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4 https://telegra.ph/file/293cc10710e57530404f8.mp4 https://telegra.ph/file/506898de518534ff68ba0.mp4 https://telegra.ph/file/dae0156e5f48573f016da.mp4 https://telegra.ph/file/3e2871e714f435d173b9e.mp4 https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4 https://telegra.ph/file/876edfcec678b64eac480.mp4 https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4 https://telegra.ph/file/b4834b434888de522fa49.mp4").split()
    LOGO = """MCU BOTS"""
rkn1 = Config()

