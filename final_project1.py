# Money tracker
expenses = []

BUDGET_LIMIT = 0.0

def add_expense():
    name = input("item:")
    amount = float(input("amount:"))
    expenses.append({"item": name, "amount": amount})
    print("added successfully!\n")
    check_budget()

def view_expense():
    print("Expense list")
    for e in expenses:
        print(f"{e['item']} - ฿{e['amount']}")


def show_total():
    total = sum(e["amount"] for e in expenses)
    print(f" Total spent: ฿{total}\n")


def delete_expense():
    name = input("Enter item name to delete: ")
    for e in expenses:
        if e["item"].lower() == name.lower():
            expenses.remove(e)
            print("Deleted successfully!\n")
            return
    print(" Item not found.\n")


def check_budget() :
    total = sum(e["amount"] for e in expenses)

    if BUDGET_LIMIT == 0:
        return
    
    if total > BUDGET_LIMIT:
        print(" Warning: You spend too much money!\n")
    else:
        print(f"You are still within budget. Remaining: ฿{BUDGET_LIMIT - total:.2f}\n") 
    
def change_budget():
    global BUDGET_LIMIT
    new_limit = float(input("Enter your new limit: ฿"))
    BUDGET_LIMIT = new_limit
    print(f" Budget limit updated to ฿{BUDGET_LIMIT}\n")
    check_budget()


while True:
    print("1. add expense")
    print("2. view expense")
    print("3. show total")
    print("4. delete expense")
    print("5. change budget limit")
    print("6. exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        show_total()
    elif choice == 4:
        delete_expense()
    elif choice == 5:
        change_budget()
    elif choice == 6:
        print("Bye!")
        break
    else:
        print("not found")