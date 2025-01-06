import pandas as pd
from datetime import datetime

# Creating a DataFrame to store financial records
columns = ['DateTime', 'Category', 'Description', 'Amount', 'Type']  # Type either 'Income' or 'Expense'
finance_tracker = pd.DataFrame(columns=columns)

# Predefined list of categories
categories = ['Salary', 'Groceries', 'Entertainment', 'Utilities', 'Rent', 'Miscellaneous']

# Function to add a new transaction
def add_transaction(datetime, category, description, amount, transaction_type):
    global finance_tracker
    new_transaction = pd.DataFrame({
        'DateTime': [datetime],
        'Category': [category],
        'Description': [description],
        'Amount': [amount],
        'Type': [transaction_type]
    })
    finance_tracker = pd.concat([finance_tracker, new_transaction], ignore_index=True)

# Function to show the current records
def show_tracker():
    global finance_tracker
    for index, row in finance_tracker.iterrows():
        print(f"Transaction {index + 1}:")
        print(f"  DateTime: {row['DateTime']}")
        print(f"  Category: {row['Category']}")
        print(f"  Description: {row['Description']}")
        print(f"  Amount: {row['Amount']}")
        print(f"  Type: {row['Type']}")
        print()  # Add a blank line between transactions

# Function to calculate total income, total expenses, and balance
def calculate_balance():
    global finance_tracker
    income = finance_tracker[finance_tracker['Type'] == 'Income']['Amount'].sum()
    expenses = finance_tracker[finance_tracker['Type'] == 'Expense']['Amount'].sum()
    balance = income - expenses
    return income, expenses, balance

# Function to take user input for a new transaction
def user_input_transaction():
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Automatically get the current date and time
    
    # Display existing categories
    print("\nExisting Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    category_choice = input("\nSelect a category by number or type a new category: ")
    
    # Check if the user selected an existing category or entered a new one
    if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
        category = categories[int(category_choice) - 1]
    else:
        category = category_choice
        # Add the new category to the predefined list
        if category not in categories:
            categories.append(category)
    
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    transaction_type = input("Enter the type (Income/Expense): ")
    add_transaction(current_datetime, category, description, amount, transaction_type)

# Main function to interact with the user
def main():
    while True:
        print("\nOptions:")
        print("1. Add a new transaction")
        print("2. Show current financial records")
        print("3. Calculate balance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user_input_transaction()
        elif choice == '2':
            print("\nCurrent Financial Records:")
            show_tracker()
        elif choice == '3':
            income, expenses, balance = calculate_balance()
            print("\nTotal Income: ", income)
            print("Total Expenses: ", expenses)
            print("Current Balance: ", balance)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()