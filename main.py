try:
	# Trying to import my main package
	from flywithdsc import config
	print("INFO: Config was loaded successfuly!")
except ImportError as e:
	print("ERROR: {e}")
	import sys
	sys.exit(1)

def run_application():
	"""Main function responsible for the entire program"""
	print("Loading FlyWithDsc...")
	print(f"The loaded discord token is: {'loaded correctly' if config.DISCORD_BOT_TOKEN else 'NO TOKEN!'}")

	# Check if the discord token is not loaded and exit
	if not config.DISCORD_BOT_TOKEN:
		print("Discord token was not properly loaded check your .env file")
		return

# Checks if the application was launched directly and was not imported as module
if __name__ == "__main__":
	run_application()
