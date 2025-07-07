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
	
	from flywithdsc import database
	database.initialize_database(config.DATABASE_URL)

	from datetime import datetime
	database.save_flight(
		config.DATABASE_URL, 
		(
			str(datetime.now())[:19], # download_date
			'Ryanair', # airline
			'JFK', # from_airport
			'WMI', # to_airport
			'2025-07-08 10:00:00', # from_date
			'2025-07-08 18:30:00', # to_date
			890.50 # price
		))

# Checks if the application was launched directly and was not imported as module
if __name__ == "__main__":
	run_application()
