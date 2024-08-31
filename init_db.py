from database import (
    create_user_table, add_user, create_client_table,
    create_appointments_table, create_behaviors_table,
    create_awol_table, create_documents_table
)

def initialize_database():
    create_user_table()
    create_client_table()
    create_appointments_table()
    create_behaviors_table()
    create_awol_table()
    create_documents_table()

    # Add a default admin user (username: admin, password: admin)
    try:
        add_user('admin', 'admin')
        print("Default admin user created.")
    except:
        print("Admin user already exists.")

if __name__ == "__main__":
    initialize_database()
