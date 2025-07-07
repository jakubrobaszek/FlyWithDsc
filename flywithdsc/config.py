import os
from pathlib import Path
from dotenv import load_dotenv

# Path to the '.env' file
DOTENV_PATH = Path(__file__).resolve().parent.parent / '.env'

# Checking if path exists
if DOTENV_PATH.exists():
	# (override - overrides the .env k-v pairs even if they exist)
	load_dotenv(dotenv_path=DOTENV_PATH, override=True)
	print(f"INFO: Loaded .env file from: {DOTENV_PATH}")
else:
	print(f"WARNING: Create .env file in {DOTENV_PATH} using '.env_example' template")

DISCORD_BOT_TOKEN: str = os.getenv("DISCORD_BOT_TOKEN")
DATABASE_URL: str = os.getenv("DATABASE_URL", "flights_data.sqlite3")

# Checking if discord bot token was loaded
if not DISCORD_BOT_TOKEN:
	print(f"WARNING: Set up the 'DISCORD_BOT_TOKEN' in your .env file in: {DOTENV_PATH}")
