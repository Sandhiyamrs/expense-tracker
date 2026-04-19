from expense import Expense
from storage import load_expenses, save_expenses
from utils import validate_amount, get_today_date

def add_expense():
    amount = input("Enter amount: ")
    amount = validate_amount(amount)

    if amount is None:
        return

    category = input("Enter category: ")
    note = input("Enter note: ")
    date = get_today_date()

    expense = Expense(amount, category, date, note)

    expenses = load_expenses()
    expenses.append(expense.to_dict())
    save_expenses(expenses)

    print("Expense added successfully!\n")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.\n")
        return

    print("\n==== All Expenses ====")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['note']}")
    print()

def filter_expenses():
    category = input("Enter category to filter: ")

    expenses = load_expenses()
    filtered = [exp for exp in expenses if exp["category"].lower() == category.lower()]

    if not filtered:
        print("No matching expenses.\n")
        return

    print(f"\n==== Expenses in {category} ====")
    for exp in filtered:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['note']}")
    print()


def show_total():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.\n")
        return

    total = sum(exp["amount"] for exp in expenses)

    print(f"\nTotal Spending: ₹{total}\n")


def menu():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Show Total Spending")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            show_total()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()