import os

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "flights_data.sqlite3")

# Checking if discord bot token was loaded
if not DISCORD_BOT_TOKEN:
	print("WARNING: Set up the 'DISCORD_BOT_TOKEN' in your .env file")
