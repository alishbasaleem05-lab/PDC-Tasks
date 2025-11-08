import time
import os
import datetime
import random
from threading import Thread

# ---------- Expense class ----------
class Expense:
    """Represents a single expense entry."""
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.user} - Rs.{self.amount}"


# ---------- Custom Thread Class ----------
class ExpenseThread(Thread):
    """Each thread simulates one user adding expenses."""
    def __init__(self, user, duration, expenses_list):
        Thread.__init__(self)
        self.user = user
        self.duration = duration
        self.expenses_list = expenses_list

    def run(self):
        print(f"--> {self.user}'s thread running (Process ID: {os.getpid()})")
        time.sleep(self.duration)  # simulate work (time to make expense)
        amount = random.randint(100, 1000)
        exp = Expense(self.user, amount)
        self.expenses_list.append(exp)
        print(f"✅ {self.user} added an expense: {exp}")
        print(f"--> {self.user}'s thread finished.\n")


# ---------- Main Function ----------
def main():
    start_time = time.time()
    expenses = []

    print("💸 Expense Tracker using Custom Thread Class\n")

    # Create multiple user threads (each one acts like a producer)
    users = ["Alishba", "Sara", "Hina", "Noor", "Ayesha", "Maryam", "Ali", "Bilal", "Hamza"]
    threads = []

    for user in users:
        duration = random.randint(1, 5)
        t = ExpenseThread(user, duration, expenses)
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("\n🏁 All expense threads completed!")
    print(f"💰 Total Expenses Added: {len(expenses)}")

    # Display all expenses
    print("\n📜 Expense Summary:")
    for exp in expenses:
        print("•", exp)

    print("\n--- Execution Time: %.2f seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
