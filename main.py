def load_config():
	try:
		# Trying to import config from main package
		from flywithdsc import config
		print("INFO: Config was loaded successfuly!")
		return config
	except ImportError as e:
		print("ERROR: {e}")
		import sys
		sys.exit(1)

def run_application():
	"""Main function responsible for the entire program"""
	print("Loading FlyWithDsc...")
	config = load_config()
	print(f"The loaded discord token is: {'loaded correctly' if config.DISCORD_BOT_TOKEN else 'NO TOKEN!'}")

	# Check if the discord token is not loaded and exit
	if not config.DISCORD_BOT_TOKEN:
		print("Discord token was not properly loaded check your .env file")
		return
	
	from flywithdsc import bot
	bot.client.run(config.DISCORD_BOT_TOKEN)
	
	# Import and initialize database and scraper
	from flywithdsc import database, scraper
	database.initialize_database(config.DATABASE_URL)

	# Scrape flights and save them to database
	download = scraper.scrape_flights('LCJ', 'AGP')
	dwnl_count = int(len(download) / 7)
	for x in range(1, dwnl_count+1):
		database.save_flight(config.DATABASE_URL, download[(x-1)*7:x*7])

# Checks if the application was launched directly and was not imported as module
if __name__ == "__main__":
	run_application()
