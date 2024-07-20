import mysql.connector
from tabulate import tabulate
# Database connection details (replace with your actual credentials)
db_host = "localhost"
db_user = "root"
db_password = "Deb@2005"
db_name = "contact_book"

# Connect to MySQL database
try:
    connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()
except mysql.connector.Error as err:
    print("Error connecting to database:", err)
    exit(1)

# Function to add contact data
def add_contact():
    name = input("Enter contact name: ")
    phone = int(input("Enter phone number: "))
    email = input("Enter email address (optional): ")

    try:
        # Insert contact data into the database
        sql = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, phone, email))
        connection.commit()
        print("Contact added successfully!")
    except mysql.connector.Error as err:
        print("Error adding contact:", err)

# Function to remove contact data
def remove_contact():
    name = input("Enter name of contact to remove: ")

    try:
        # Delete contact data from the database
        sql = "DELETE FROM contacts WHERE name = %s"
        cursor.execute(sql, (name,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Contact removed successfully!")
        else:
            print("Contact with name", name, "not found!")
    except mysql.connector.Error as err:
        print("Error removing contact:", err)

# Function to update contact data
def update_contact():
    name = input("Enter name of contact to update: ")

    try:
        # Fetch existing contact data
        sql = "SELECT * FROM contacts WHERE name = %s"
        cursor.execute(sql, (name,))
        contact = cursor.fetchone()

        if contact:
            new_name = input("Update name (leave blank to keep current): ") or contact[0]
            new_phone = input("Update phone number (leave blank to keep current): ") or contact[1]
            new_email = input("Update email address (leave blank to keep current): ") or contact[2]

            # Update contact data
            sql = "UPDATE contacts SET name = %s, phone = %s, email = %s WHERE name = %s"
            cursor.execute(sql, (new_name, new_phone, new_email, name))
            connection.commit()
            print("Contact updated successfully!")
        else:
            print("Contact with name", name, "not found!")
    except mysql.connector.Error as err:
        print("Error updating contact:", err)

# Function to display contact data
def show_contacts():
    try:
        table_name = "contacts"
        sql_query = f"SELECT * FROM {table_name}"
         # Execute the query
        cursor.execute(sql_query)

         # Fetch all rows from the cursor
        rows = cursor.fetchall()

             # Get column names
        column_names = [col[0] for col in cursor.description]

        # Use tabulate to format the table
        table = tabulate(rows, headers=column_names, tablefmt="grid")

        # Print the formatted table
        print(table)

    except mysql.connector.Error as err:
        print("Error displaying contacts:", err)

# Main program loop
while True:
    print("\nContact Book System")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Show Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        show_contacts()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")

# Close database connection
connection.close()
