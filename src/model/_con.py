import sqlite3

# Define the global variables
conn = None
cursor = None

try:
    # Path to the SQLite database file
    db_file_path = "./my.db"

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Example SQL query execution
    cursor.execute("SELECT * FROM com")
    rows = cursor.fetchall()

    # Print the query results
    for row in rows:
        print(row)

    conn.close()
except sqlite3.Error as e:
    print("Error connecting to SQLite: ", e)


def db_insert(txt: str):
    db_file_path = "./my.db"

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO com (command) VALUES ('{txt}')")
    conn.commit()

    conn.close()