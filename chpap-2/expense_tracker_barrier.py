import datetime
from random import randrange
from threading import Barrier, Thread
from time import sleep, ctime

class Expense:
    """Represents a single expense item."""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.name} - Rs. {self.amount}"


class ExpenseTracker:
    """Main expense tracker class."""
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount):
        expense = Expense(name, amount)
        self.expenses.append(expense)
        print(f"✅ {name} added: Rs. {amount}")

    def total_expense(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"\n💰 Total Expense: Rs. {total}\n")


# ----- Barrier + Threads -----

num_users = 3
barrier = Barrier(num_users)
users = ["Alishba", "Sara", "Hina"]
tracker = ExpenseTracker()


def user_task():
    """Simulate each user adding an expense before waiting at the barrier."""
    name = users.pop()
    sleep(randrange(2, 5))  # random delay (like real users)
    amount = randrange(100, 1000)
    tracker.add_expense(name, amount)
    print(f"{name} reached the barrier at {ctime()}")
    barrier.wait()  # all users must reach this point before continuing


def main():
    threads = []
    print("💸 Expense Tracker Simulation Started!\n")

    # start all user threads
    for _ in range(num_users):
        t = Thread(target=user_task)
        threads.append(t)
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()

    print("\n🏁 All users reached the barrier! Now calculating total...")
    tracker.total_expense()
    print("✅ Process complete at:", ctime())


if __name__ == "__main__":
    main()
