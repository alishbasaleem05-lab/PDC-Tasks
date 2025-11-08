import time
import os
import datetime
import threading
from threading import Thread
from random import randint

# ---------- Lock Definition ----------
threadLock = threading.Lock()

# ---------- Shared Resource ----------
expenses = []


# ---------- Expense Class ----------
class Expense:
    """Represents a single expense entry."""
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.user} - Rs.{self.amount}"


# ---------- Thread Class ----------
class ExpenseThread(Thread):
    """Each thread simulates a user adding expenses with locking."""
    def __init__(self, user, duration):
        Thread.__init__(self)
        self.user = user
        self.duration = duration

    def run(self):
        # Acquire the Lock before accessing shared list
        threadLock.acquire()
        try:
            print(f"---> {self.user}'s thread running, Process ID: {os.getpid()}")
            time.sleep(self.duration)

            amount = randint(100, 1000)
            exp = Expense(self.user, amount)
            expenses.append(exp)

            print(f"✅ {self.user} added: {exp}")
            print(f"---> {self.user}'s thread finished.\n")
        finally:
            # Always release the lock (even if an error occurs)
            threadLock.release()


# ---------- Main Function ----------
def main():
    start_time = time.time()
    print("💸 Expense Tracker using Thread Lock (Mutual Exclusion)\n")

    users = ["Alishba", "Sara", "Hina", "Noor", "Ayesha", "Maryam", "Ali", "Bilal", "Hamza"]
    threads = []

    # Create Threads
    for user in users:
        duration = randint(1, 4)
        t = ExpenseThread(user, duration)
        threads.append(t)

    # Start Threads
    for t in threads:
        t.start()

    # Join Threads
    for t in threads:
        t.join()

    # After all threads finish
    print("\n🏁 All threads completed!")
    print(f"💰 Total Expenses Added: {len(expenses)}")

    print("\n📜 Expense Summary:")
    for exp in expenses:
        print("•", exp)

    print("\n--- Execution Time: %.2f seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
