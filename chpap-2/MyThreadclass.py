from threading import Thread, Lock
import time
import os
import random

# Shared resource: Expense list
expenses = []
threadLock = Lock()

# 🧾 Thread Class Definition
class ExpenseThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        # Acquire lock before modifying shared resource
        threadLock.acquire()
        try:
            print(f"ID of process running {self.name} (PID: {os.getpid()})")

            # Simulate adding an expense
            expense = random.randint(100, 1000)
            expenses.append(expense)
            print(f"{self.name} added expense: {expense}")
            print(f"Current expenses: {expenses}\n")

        finally:
            # Always release the lock to avoid deadlocks
            threadLock.release()

        time.sleep(random.randint(1, 3))
        print(f"{self.name} completed.\n")


def main():
    # Create multiple expense threads
    thread1 = ExpenseThread("UserThread#1")
    thread2 = ExpenseThread("UserThread#2")
    thread3 = ExpenseThread("UserThread#3")

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all to finish
    thread1.join()
    thread2.join()
    thread3.join()

    print("✅ All expense threads finished.")
    print(f"Final Expenses List: {expenses}")


if __name__ == "__main__":
    main()
