import json
from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "12596720"))
    API_HASH = getenv("API_HASH", "6af95397236b2f4f0da1f29bc6cd858b")
    BOT_TOKEN = getenv("BOT_TOKEN", "8113380638:AAEaxturSbm2oGXQMMJCDnDzwj25uGW4Pvk")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    BASE_URL = getenv("BASE_URL", "https://cloud02.cskinglk.xyz/").rstrip('/') if getenv("BASE_URL") else ""
    DATABASE_URL = getenv("MONGODB_URI", "mongodb+srv://csclouddrive01:csclouddrive01@cluster0.x5ynaqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    TMDB_API = getenv("TMDB_API", "")
    TMDB_LANGUAGE = getenv("TMDB_LANGUAGE", "en")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "").split(",") if channel.strip()]
    STATIC_AUTH_CHANNEL = [channel.strip() for channel in getenv("STATIC_AUTH_CHANNEL", "-1002794637424").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERS = json.loads(getenv("USERS", '{"admin": "admin"}'))
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))
