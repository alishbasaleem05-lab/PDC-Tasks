import threading
import time
import random
import os

# Shared resource: list of expenses
expenses = []
threadLock = threading.Lock()

def add_expense(thread_number):
    """Function called by each thread to add an expense."""
    time.sleep(random.randint(1, 3))  # simulate work delay

    expense = random.randint(100, 1000)
    with threadLock:  # Lock for thread-safe list access
        expenses.append(expense)
        print(f"Thread #{thread_number} (PID {os.getpid()}) added expense: {expense}")
        print(f"Current expenses: {expenses}\n")


def main():
    threads = []

    # Create 10 threads (like 10 users adding expenses)
    for i in range(10):
        t = threading.Thread(target=add_expense, args=(i,))
        threads.append(t)
        t.start()
        t.join()  # Wait after each thread (sequential start)

    print("✅ All expense threads completed.")
    print(f"Final expenses list: {expenses}")


if __name__ == "__main__":
    main()
