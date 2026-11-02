from expense import Expense
from storage import load_expenses, save_expenses
from validators import get_positive_number


def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Quit")


def add_expense(expenses):
    amount = get_positive_number("Amount: ")

    category = input("Category: ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Category: ").strip()

    description = input("Description: ").strip()

    expenses.append(Expense(amount, category, description))
    save_expenses(expenses)
    print("Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    for i, e in enumerate(expenses, 1):
        print(i, e)

    total = sum(e.amount for e in expenses)
    print(f"Total: {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose 1-3: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()




