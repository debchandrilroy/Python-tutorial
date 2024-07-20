import mysql.connector
from tabulate import tabulate
from colorama import Fore, Back, Style
# Database connection details (replace with your actual credentials)
db_host = "localhost"
db_user = "root"
db_password = "Deb@2005"
db_name = "portfolioDB"
table= "portfolio01"

# Connect to MySQL database
try:
    connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()
except mysql.connector.Error as err:
    print("Error connecting to database:", err)
    exit(1)

# Function to add portfolio data
def add_data():
    Date=input("Date(HHHH-MM-DD):")
    Order_Name=input("Input Order Name:")
    Profit_Loss=input("Profit or Loss:")
    Qty=input("Order QTY:")
    Entry_price=input("Entry Price:")
    Exit_price=input("Exit price:")
    Amount=input("Total Amount:")

    try:
        # Insert contact data into the database
        sql = f"INSERT INTO {table} (Date,Order_Name,Profit_Loss,Qty,Entry_price,Exit_price,Amount) VALUES (%s, %s, %s,%s, %s, %s,%s)"
        cursor.execute(sql, (Date,Order_Name,Profit_Loss,Qty,Entry_price,Exit_price,Amount))
        connection.commit()
        print("Contact added successfully!")
    except mysql.connector.Error as err:
        print("Error adding contact:", err)

#################################################################################################################################

# Function to remove contact data
def remove_data():
    Unique_ID = input("Enter Unique_ID of Data to remove: ")

    try:
        # Delete contact data from the database
        sql = f"DELETE FROM {table} WHERE Unique_ID = %s"
        cursor.execute(sql, (Unique_ID,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Data removed successfully!")
        else:
            print("Data with Unique ID", Unique_ID, "not found!")
    except mysql.connector.Error as err:
        print("Error removing Data:", err)

#####################################################################################

# Function to update data
def update_data():
    Unique_ID = input("Enter Unique_ID of Order Name to update: ")

    try:
        # Fetch existing contact data
        sql = f"SELECT * FROM {table} WHERE  Unique_ID = %s"
        cursor.execute(sql, (Unique_ID,))
        contact = cursor.fetchone()

        if contact:
            new_Date=input("Update Date(HHHH-MM-DD)(leave blank to keep current):")or contact[1]
            new_Order_Name=input("Update Input Order Name(leave blank to keep current):")or contact[2]
            new_Profit_Loss=input("Update Profit or Loss(leave blank to keep current):") or contact[3]
            new_Qty=input("Update Order QTY(leave blank to keep current):")or contact[4]
            new_Entry_price=input("Update Entry Price(leave blank to keep current):")or contact[5]
            new_Exit_price=input("Update Exit price(leave blank to keep current):")or contact[6]
            new_Amount=input("Update Total Amount(leave blank to keep current):")or contact[7]

            # Update contact data
            sql = f"UPDATE {table} SET Date = %s, Order_Name = %s, Profit_Loss = %s, Qty = %s, Entry_price = %s, Exit_price = %s, Amount = %s WHERE Unique_ID = %s"
            cursor.execute(sql, (new_Date, new_Order_Name, new_Profit_Loss, new_Qty, new_Entry_price, new_Exit_price, new_Amount, Unique_ID))
            connection.commit()
            print("Data updated successfully!")
        else:
            print("Contact with name", Unique_ID, "not found!")
    except mysql.connector.Error as err:
        print("Error updating Data:", err)

############################################################


# Function to display contact data
def view_data(cursor, table_name="portfolio01"):
    """Fetches data from the specified table and displays it with color-coded profit/loss.

    Args:
        cursor (mysql.connector.cursor): A MySQL cursor object for executing queries.
        table_name (str, optional): Name of the table to retrieve data from. Defaults to "portfolio01".
    """

    try:
        sql_query = f"SELECT * FROM {table_name}"
        cursor.execute(sql_query)

        rows = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]

        # Color-code profit/loss data
        colored_rows = []
        for row in rows:
            profit_loss_index = column_names.index("Profit_Loss")  # Assuming "Profit_Loss" is the column name
            profit_loss_value = row[profit_loss_index].lower()  # Convert to lowercase for case-insensitive comparison

            colored_row = list(row)
            if profit_loss_value == "profit":
                colored_row[profit_loss_index] = Fore.GREEN + profit_loss_value + Style.RESET_ALL
            elif profit_loss_value == "loss":
                colored_row[profit_loss_index] = Fore.RED + profit_loss_value + Style.RESET_ALL
            colored_rows.append(colored_row)

        table = tabulate(colored_rows, headers=column_names, tablefmt="grid")
        print(table)

    except mysql.connector.Error as err:
        print(f"Error displaying data: {err}")


# Example usage
# Assuming you have established a connection and a cursor
view_data(cursor)  # Use default table_name
view_data(cursor, "another_table")  # Specify a different table

# Main program loop
while True:
    print("\n\n-------------------------PORTFOLIO--------------------------------")
    print("1. Add DATA")
    print("2. Remove DATA")
    print("3. Update DATA")
    print("4. View DATA")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_data()
    elif choice == '2':
        remove_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        view_data()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")

# Close database connection
connection.close()

