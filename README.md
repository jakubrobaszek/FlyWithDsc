# FlyWithDsc - Flight Deal Finder with a Discord Bot

FlyWithDsc is a work-in-progress project to create a Python tool for finding and analyzing flight prices from airlines (initially Ryanair and Wizzair) and sharing this information via a Discord bot.

## Main Project Goals

*   ✈️ **Automated Data Retrieval:** Regularly check flight prices for defined routes and dates.
*   💾 **Data Storage:** Save the collected flight information into a local SQLite database.
*   📊 **Price Analysis:** Utilize the Pandas library to analyze price trends and find the best deals.
*   🤖 **Discord Bot Interface:** Allow users to interact with the system through Discord commands (e.g., search for flights, subscribe to price alerts).
*   🌍 **Multilingual Support (Planned):** Adapt bot responses to user/server language preferences.

## Project Status

⚠️ **This project is currently in the early stages of development.**

Currently implemented/in progress:
*   Basic project structure (folders, configuration).
*   Mechanism for loading configuration from an `.env` file.
*   A basic 'main.py' file for the application's entry point.

**Next Steps:**
*   Full implementation of the `database.py` module for saving and retrieving data.
*   Development of the `scraper.py` module to fetch flight data (initially for Ryanair).
*   Implementation of the `analyzer.py` module for data analysis.
*   Building the Discord bot logic in `bot.py`.

## Tech Stack

*   **Language:** Python3
*   **Web Scraping / API Interaction:** `requests` (for JSON APIs)
*   **Database:** `SQLite3` (built-in `sqlite3` module)
*   **(Planned) Data Analysis:** `Pandas`, `NumPy`
*   **Discord Bot:** `discord.py`
*   **Configuration:** `python-dotenv` (for `.env` files)
*   **Version Control:** `Git`, `GitHub`, `GitLab`
*   **Virtual Environment:** `venv`
*   **(Planned) Testing:** `pytest`
*   **(Planned) Code Formatting/Linting:** `Black`, `Flake8`/`Ruff`

## Prerequisites

*   Python 3.9 or newer
*   `pip` (Python package manager)
*   `Git` (optional, if cloning the repository)

## Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jakubrobaszek/FlyWithDsc.git
    cd FlyWithDsc
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Linux/macOS:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Remember to update `requirements.txt` later using `pip freeze > requirements.txt` if you are trying to make a commit)*

4.  **Set up environment variables:**
    *   Copy the `.env_example` file to a new file named `.env`:
        ```bash
        cp .env_example .env  # Linux/macOS
        # copy .env_example .env  # Windows
        ```
    *   Open the `.env` file in a text editor and fill in the required values, especially `DISCORD_BOT_TOKEN` and `DATABASE_URL` (e.g., `DATABASE_URL="flights_data.sqlite3"`).
        ```ini
        # Example .env content
        DISCORD_BOT_TOKEN="YOUR_ACTUAL_DISCORD_BOT_TOKEN_HERE"
        DATABASE_URL="flights_data.sqlite3"
        ```

5.  **Run the application (at the current stage):**
    From the root project folder `FlyWithDsc/`, execute:
    ```bash
    python main.py
    ```

## Project Structure (Simplified)
```
FlyWithDsc/
├── flywithdsc/ # Main application package
│ ├── __init__.py # Package implementation
│ ├── config.py # Configuration
│ ├── database.py # Database handling
│ ├── scraper.py # (To be done) Data scraping
│ ├── analyzer.py # (To be done) Data analysis
│ └── bot.py # (To be done) Discord bot logic
├── .env # (Local, not in Git) Environment variables
├── .env_example # Example .env file
├── .gitignore # Files ignored by Git
├── main.py # Main application entry point
├── requirements.txt # (To be generated/updated) Dependencies
└── README.md # This file
```