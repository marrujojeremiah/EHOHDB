import sqlite3

def remove_duplicates():
    conn = sqlite3.connect("client_db.sqlite3")
    cursor = conn.cursor()
    
    # Find and delete duplicates, keeping the first entry
    cursor.execute("""
    DELETE FROM clients
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM clients
        GROUP BY first_name, last_name
    )
    """)
    
    conn.commit()
    conn.close()
    print("Duplicates removed.")

if __name__ == "__main__":
    remove_duplicates()
