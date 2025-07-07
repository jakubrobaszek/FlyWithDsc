import sqlite3

def initialize_database(db_path: str):
    # Making a connection (if database does not exist, it will create one)
    with sqlite3.connect(db_path) as con:
        # Creating a cursor for executing SQL
        cur = con.cursor()

        # Table creation if it does not exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS flights (
                id INTEGER PRIMARY KEY,
                download_date TEXT,
                airline TEXT,
                from_airport TEXT,
                to_airport TEXT,
                from_date TEXT,
                to_date TEXT,
                price REAL
            )
        ''')
        con.commit()

# Saved for retrieving data
# def execute(query: str, db_path: str, args=()):
#     with sqlite3.connect(db_path) as con:
#         cur = con.cursor()
#         # If it starts with select
#         if query.lower().startswith('select'):
#             cur.execute(query, args)
#             # Fetches all rows
#             return cur.fetchall()
#         else:
#             cur.execute(query, args)
#             # Will return the rows affected by the change
#             return cur.rowcount

def save_flight(db_path: str, args=()):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute('INSERT INTO flights (download_date, airline, from_airport, to_airport, from_date, to_date, price) VALUES (?, ?, ?, ?, ?, ?, ?)', args)
        return cur.rowcount