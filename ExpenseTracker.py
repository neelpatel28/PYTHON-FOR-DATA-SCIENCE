class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category].append(amount)
        else:
            self.expenses[category] = [amount]
        print("Expense added.")

    def view_expenses(self):
        print("\nExpense Summary:")
        for cat, amounts in self.expenses.items():
            print(cat, ":", amounts)

    def total_expense(self):
        total = sum(sum(v) for v in self.expenses.values())
        print("Total Expense:", total)

    def category_wise_report(self):
        print("\nCategory-wise Report:")
        for cat, amounts in self.expenses.items():
            print(cat, "Total:", sum(amounts))

    def save_to_file(self):
        with open("expenses.txt", "w") as f:
            for cat, amounts in self.expenses.items():
                f.write(f"{cat}:{amounts}\n")
        print("Expenses saved to file.")

    def load_from_file(self):
        try:
            with open("expenses.txt", "r") as f:
                for line in f:
                    cat, amounts = line.strip().split(":")
                    self.expenses[cat] = eval(amounts)
            print("Expenses loaded successfully.")
        except:
            print("No saved data found.")


tracker = ExpenseTracker()

while True:
    print("\nSmart Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Report")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        cat = input("Enter Category: ")
        amt = float(input("Enter Amount: "))
        tracker.add_expense(cat, amt)

    elif choice == '2':
        tracker.view_expenses()

    elif choice == '3':
        tracker.total_expense()

    elif choice == '4':
        tracker.category_wise_report()

    elif choice == '5':
        tracker.save_to_file()

    elif choice == '6':
        tracker.load_from_file()

    elif choice == '7':
        break

    else:
        print("Invalid choice.")
