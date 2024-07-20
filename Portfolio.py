import csv
from datetime import datetime

def get_current_month():
    """Returns the current month as a string (e.g., '2024-06')"""
    today = datetime.today()
    return today.strftime('%Y-%m')

def create_csv_file(filename):
    """Creates a new CSV file with headers if it doesn't exist"""
    headers = ['Date', 'Description', 'Amount', 'Income/Expense']
    try:
        with open(filename, 'x', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
    except FileExistsError:
        pass  # File already exists, no need to create headers

def add_income_expense(filename, date, description, amount, income_expense):
    """Adds a new income or expense record to the CSV file"""
    try:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date, description, amount, income_expense])
    except ValueError:
        print("Error: Invalid data format. Please ensure correct values.")

def view_transactions(filename, month=None):
    """Displays all or month-specific transactions from the CSV file"""
    if not month:
        month = get_current_month()  # Display current month by default
    print(f"\nTransactions for {month}:")

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Date'].startswith(month):
                print(f"{row['Date']}: {row['Description']} ({row['Income/Expense']}) - ₹{row['Amount']}")

def calculate_totals(filename, month=None):
    """Calculates total income and expenses for a specific month (or current month)"""
    if not month:
        month = get_current_month()  # Calculate for current month by default
    total_income = 0
    total_expense = 0

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Date'].startswith(month):
                amount = float(row['Amount'])
                if row['Income/Expense'] == 'Income':
                    total_income += amount
                else:
                    total_expense += amount

    print(f"\nTotal Income for {month}: ₹{total_income:.2f}")
    print(f"Total Expense for {month}: ₹{total_expense:.2f}")
    print(f"Balance for {month}: ₹{total_income - total_expense:.2f}")

# Example usage
filename = 'finances.csv'  # Replace with your desired filename
create_csv_file(filename)

while True:
    print("\nMenu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Calculate Totals")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        add_income_expense(filename, date, description, amount, 'Income')
    elif choice == '2':
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        add_income_expense(filename, date, description, amount, 'Expense')
    elif choice == '3':
        month = input("Enter month to view (YYYY-MM) or press Enter for current month: ")
        view_transactions(filename, month)
    elif choice == '4':
        month = input("Enter month to calculate totals for (YYYY-MM) or press Enter for current month: ")
        calculate_totals(filename, month)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
