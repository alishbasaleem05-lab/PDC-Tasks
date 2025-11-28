from threading import Thread
from queue import Queue
import time
import random
import os

# Shared queue to hold expenses
expense_queue = Queue()
# List to store processed expenses
expense_data = []

# Producer thread adds expenses to the queue
class ExpenseProducer(Thread):
    def _init_(self, queue, name, expenses_to_add):
        super()._init_()
        self.queue = queue
        self.name = name
        self.expenses_to_add = expenses_to_add

    def run(self):
        print(f"[{self.name}] Starting Producer (PID: {os.getpid()})")
        for expense in self.expenses_to_add:
            print(f"[{self.name}] Queuing expense: {expense}")
            self.queue.put(expense)
            time.sleep(random.uniform(0.5, 1.5))
        print(f"[{self.name}] Finished adding all expenses.\n")


# Consumer thread processes expenses from the queue
class ExpenseConsumer(Thread):
    def _init_(self, queue, name):
        super()._init_()
        self.queue = queue
        self.name = name

    def run(self):
        print(f"[{self.name}] Starting Consumer (PID: {os.getpid()})")
        while True:
            expense = self.queue.get()
            expense_data.append(expense)
            print(f"[{self.name}] Processed expense: {expense}")
            self.queue.task_done()
            time.sleep(random.uniform(0.5, 1.0))


# Function to display all processed expenses
def view_expenses():
    print("\nCurrent Expense Data:")
    if not expense_data:
        print("No expenses recorded yet.")
    else:
        for idx, exp in enumerate(expense_data, start=1):
            print(f"{idx}. {exp['item']} - ${exp['amount']} ({exp['date']})")
    print()


def main():
    # Sample expenses to add
    new_expenses = [
        {"item": "Coffee", "amount": 3.5, "date": "2025-11-05"},
        {"item": "Snacks", "amount": 7.0, "date": "2025-11-05"},
        {"item": "Book", "amount": 15.0, "date": "2025-11-05"},
        {"item": "Internet Bill", "amount": 40.0, "date": "2025-11-05"},
        {"item": "Movie Ticket", "amount": 10.0, "date": "2025-11-05"},
    ]

    producer = ExpenseProducer(expense_queue, "ExpenseProducer", new_expenses)
    consumer = ExpenseConsumer(expense_queue, "ExpenseConsumer")
    consumer.daemon = True  # Daemon thread ends with main program

    consumer.start()
    producer.start()
    producer.join()  # Wait for producer to finish
    expense_queue.join()  # Wait for all items in queue to be processed

    print("\nAll expenses have been processed successfully!")
    view_expenses()


if _name_ == "_main_":
    main()
