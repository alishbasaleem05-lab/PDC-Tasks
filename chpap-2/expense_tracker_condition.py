import datetime
import logging
import threading
import time
from random import randrange

# ---------- Logging setup ----------
LOG_FORMAT = '%(asctime)s %(threadName)-15s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# ---------- Shared Resources ----------
condition = threading.Condition()
expenses = []  # shared list between producer and consumer
MAX_EXPENSES = 10  # maximum buffer size


class Expense:
    """Represents a single expense item."""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.name} - Rs.{self.amount}"


# ---------- Producer Thread ----------
class Producer(threading.Thread):
    def __init__(self, users):
        super().__init__(name="Producer")
        self.users = users

    def produce(self):
        with condition:
            if len(expenses) == MAX_EXPENSES:
                logging.info("💼 Expense list full. Producer waiting...")
                condition.wait()

            # create a random expense
            name = self.users[randrange(len(self.users))]
            amount = randrange(100, 1000)
            exp = Expense(name, amount)
            expenses.append(exp)
            logging.info(f"➕ Added: {exp} (Total: {len(expenses)})")

            # notify consumer
            condition.notify()

    def run(self):
        for _ in range(20):
            time.sleep(randrange(1, 3))  # simulate delay
            self.produce()


# ---------- Consumer Thread ----------
class Consumer(threading.Thread):
    def __init__(self):
        super().__init__(name="Consumer")

    def consume(self):
        with condition:
            if len(expenses) == 0:
                logging.info("📭 No expenses to process. Consumer waiting...")
                condition.wait()

            exp = expenses.pop(0)
            logging.info(f"🗑️ Processed & removed: {exp} (Remaining: {len(expenses)})")

            # notify producer
            condition.notify()

    def run(self):
        for _ in range(20):
            time.sleep(randrange(2, 4))
            self.consume()


# ---------- Main Controller ----------
def main():
    users = ["Alishba", "Sara", "Hina", "Noor"]
    producer = Producer(users)
    consumer = Consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    logging.info("✅ All threads completed successfully!")


if __name__ == "__main__":
    main()
