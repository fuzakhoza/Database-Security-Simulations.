import sqlite3

# 1. Connect to an in-memory database and create a cursor
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 2. Create a mock users table
cursor.execute("CREATE TABLE users (username TEXT, password TEXT);")
cursor.execute("INSERT INTO users VALUES ('admin', 'SuperSecret123');")
cursor.execute("INSERT INTO users VALUES ('fuza', 'KaliLinux2026');")
conn.commit()

# 3. Simulate a login page input
user_input = input("Enter username to search: ")

# VULNERABLE SYSTEM: Directly gluing input into the SQL query string
# SECURE SYSTEM: The '?' acts as a safe placeholder
query = "SELECT * FROM users WHERE username = ?;"
print(f"\n[DEBUG] Executing SQL Query: {query}\n")

try:
    cursor.execute(query,(user_input,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"🔒 Account Found! Username: {row[0]} | Password: {row[1]}")
    else:
        print("❌ User not found.")
except Exception as e:
    print(f"⚠️ SQL Error: {e}")

conn.close()
