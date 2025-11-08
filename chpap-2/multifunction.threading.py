import threading
import time
import random
import os

# Shared data (expense list)
expenses = []
threadLock = threading.Lock()

# 🧾 Function A — Add expense
def add_expense():
    print(threading.currentThread().getName() + ' --> starting\n')
    time.sleep(2)
    expense = random.randint(100, 1000)

    with threadLock:
        expenses.append(expense)
        print(f"{threading.currentThread().getName()} added expense: {expense}")
        print(f"Current Expenses: {expenses}\n")

    print(threading.currentThread().getName() + ' --> exiting\n')


# 💸 Function B — View all expenses
def view_expenses():
    print(threading.currentThread().getName() + ' --> starting\n')
    time.sleep(2)

    with threadLock:
        if expenses:
            print(f"{threading.currentThread().getName()} viewed expenses: {expenses}")
        else:
            print(f"{threading.currentThread().getName()} found no expenses.\n")

    print(threading.currentThread().getName() + ' --> exiting\n')


# 🧮 Function C — Calculate total expenses
def calculate_total():
    print(threading.currentThread().getName() + ' --> starting\n')
    time.sleep(2)

    with threadLock:
        total = sum(expenses)
        print(f"{threading.currentThread().getName()} calculated total = {total}\n")

    print(threading.currentThread().getName() + ' --> exiting\n')


if __name__ == "__main__":
    # Create threads for each function
    t1 = threading.Thread(name='Add_Expense_Function', target=add_expense)
    t2 = threading.Thread(name='View_Expense_Function', target=view_expenses)
    t3 = threading.Thread(name='Total_Calc_Function', target=calculate_total)

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all to complete
    t1.join()
    t2.join()
    t3.join()

    print("✅ All functions executed successfully.")
    print(f"Final Expenses List: {expenses}")
