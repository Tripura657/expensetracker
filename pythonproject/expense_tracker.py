import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store expenses
FILE_NAME = "expense_tracker.csv"

# Function to initialize CSV file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(FILE_NAME, index=False)

# Function to add a new expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")

    new_expense = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Amount": [amount],
        "Description": [description]
    })

    df = pd.read_csv(FILE_NAME)
    df = pd.concat([df, new_expense], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print("\n--- All Expenses ---")
        print(df)

# Function to view expenses by category
def view_by_category():
    df = pd.read_csv(FILE_NAME)
    category = input("Enter the category to filter: ")
    filtered = df[df["Category"].str.lower() == category.lower()]
    if filtered.empty:
        print(f"No expenses found in category: {category}")
    else:
        print(f"\n--- Expenses in Category: {category} ---")
        print(filtered)

# Function to generate expense summary and visualization
def show_summary():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses recorded yet.")
        return

    summary = df.groupby("Category")["Amount"].sum()
    print("\n--- Expense Summary by Category ---")
    print(summary)

    # Plotting the summary
    summary.plot(kind="bar", title="Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.show()

# Main menu
def main():
    initialize_file()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Expense Summary & Visualization")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
