import os
from dotenv import load_dotenv

ABSOLUTE_PATH_TO_CONFIG_FILE = os.path.abspath(__file__)
CONFIG_DIR = os.path.dirname(ABSOLUTE_PATH_TO_CONFIG_FILE)
BASE_DIR = os.path.dirname(CONFIG_DIR)
DOTENV_PATH = os.path.join(BASE_DIR, '.env')

# Checking if path exists
if os.path.exists(DOTENV_PATH):
	load_dotenv(dotenv_path=DOTENV_PATH, verbose=True, override=True)
	print(f"INFO: Loaded .env file from: {DOTENV_PATH}")
else:
	print(f"WARNING: Create .env file in {DOTENV_PATH} using template")

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "flights_data.sqlite3")

# Checking if discord bot token was loaded
if not DISCORD_BOT_TOKEN:
	print(f"WARNING: Set up the 'DISCORD_BOT_TOKEN' in your .env file in: {DOTENV_PATH}")
