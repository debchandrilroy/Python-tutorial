import sqlite3

def connect_and_insert_data(database_name, table_name):
  """Connects to a database, takes user input, and inserts data.

  Args:
      database_name: The name of the database file (e.g., 'mydatabase.db').
      table_name: The name of the table to insert data into.
  """

  # Connect to the database
  try:
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    print(f"Connected to database: {database_name}")
  except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    return

  # Get user input for data
  Date = input("Enter Date: ")
  Description = input("Enter Description: ")
  Income_Expance = (input("Enter Income & Expance: "))
  Ammount=int(input("Enter Ammount:"))

  # Define the SQL insert statement with placeholders for data
  sql = f"INSERT INTO {table_name} (Date,Description,Income_Expance,Ammount) VALUES (?, ?, ?,?)"

  # Prepare data as a tuple
  data = (Date,Description,Income_Expance,Ammount)

  # Execute the statement with data as a tuple
  try:
    cursor.execute(sql, data)
    conn.commit()
    print("Data inserted successfully!")
  except sqlite3.Error as e:
    print(f"Error inserting data: {e}")

  # Close the connection (always inside a finally block)
  finally:
    if conn:
      conn.close()
      print("Database connection closed.")

# Example usage
database_name = "financeDB.db"
table_name = "pp"
connect_and_insert_data(database_name, table_name)
