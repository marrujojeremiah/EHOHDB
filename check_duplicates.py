import sqlite3

def check_duplicates():
    conn = sqlite3.connect("client_db.sqlite3")
    cursor = conn.cursor()
    
    # Check how many clients are in the database
    cursor.execute("SELECT first_name, last_name, COUNT(*) FROM clients GROUP BY first_name, last_name HAVING COUNT(*) > 1")
    duplicates = cursor.fetchall()
    
    if duplicates:
        print("Duplicate clients found:")
        for dup in duplicates:
            print(f"Name: {dup[0]} {dup[1]}, Count: {dup[2]}")
    else:
        print("No duplicates found.")
    
    conn.close()

if __name__ == "__main__":
    check_duplicates()
