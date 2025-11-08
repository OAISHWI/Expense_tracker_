# main.py
# ==========================================
# Entry point for the Expense Tracker console application.

from modules.expense import Expense
from modules.file_operations import read_expenses, write_expense
from modules.category_summarizer import summarize_by_category

def main_menu():
    """Displays the main menu and handles user navigation."""
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense_screen()
        elif choice == '2':
            view_expenses_screen()
        elif choice == '3':
            summarize_screen()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_expense_screen():
    """Collects new expense data and saves it."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").capitalize()
        date = input("Enter date (YYYY-MM-DD): ")

        expense = Expense(amount, category, date)
        write_expense(expense.amount, expense.category, expense.date)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def view_expenses_screen():
    """Displays all recorded expenses."""
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    print(f"{'Amount':<10} {'Category':<15} {'Date':<10}")
    print("-" * 35)
    for amount, category, date in expenses:
        print(f"{amount:<10} {category:<15} {date:<10}")

def summarize_screen():
    """Displays a summary of expenses by category."""
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return

    summary = summarize_by_category(expenses)
    print("\n--- Expense Summary by Category ---")
    print(f"{'Category':<15} {'Total Amount':<10}")
    print("-" * 30)
    for category, total in summary.items():
        print(f"{category:<15} {total:<10.2f}")

if __name__ == "__main__":
    main_menu()
