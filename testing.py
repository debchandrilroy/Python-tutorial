import sys
from tabulate import tabulate

# Database library to be used (replace with your choice)
db_library = "mysql.connector"  # Example: sqlite3, mysql.connector, psycopg2

# Error handling for invalid library choice
if db_library not in ["sqlite3", "mysql.connector", "psycopg2"]:
    print(f"Error: Invalid database library '{db_library}'. Choose from sqlite3, mysql.connector, or psycopg2.")
    sys.exit(1)

# Import the chosen library
if db_library == "sqlite3":
    import sqlite3
elif db_library == "mysql.connector":
    import mysql.connector
elif db_library == "psycopg2":
    import psycopg2

# Database connection details (replace with your credentials)
host = "localhost"
user = "root"
password = "Deb@2005"
database = "testDB"

# Table name (replace with your actual table name)
table_name = "employees"

# SQL query to fetch all data from the table
sql_query = f"SELECT * FROM {table_name}"

try:
  # Connect to the database using the chosen library
  if db_library == "sqlite3":
      conn = sqlite3.connect(database)
      cursor = conn.cursor()
  elif db_library == "mysql.connector":
      conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
      cursor = conn.cursor()
  elif db_library == "psycopg2":
      conn = psycopg2.connect(host=host, user=user, password=password, database=database)
      cursor = conn.cursor()

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

except Exception as e:
  print(f"Error connecting to database: {e}")

finally:
  # Close the connection (if applicable)
  if db_library in ["mysql.connector", "psycopg2"]:
      conn.close()

