
#A simple expense tracker to record and view expenses.
expenses = []

def add_expense(amount, description):
    expenses.append({"amount": amount, "description": description})
    print("Expense added.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Your expenses:")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['description']}: ${expense['amount']}")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(amount, description)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")
