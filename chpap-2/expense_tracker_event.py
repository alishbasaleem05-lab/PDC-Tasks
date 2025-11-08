import datetime
import logging
import threading
import time
import random

# ---------- Logging setup ----------
LOG_FORMAT = '%(asctime)s %(threadName)-15s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# ---------- Shared resources ----------
expenses = []
event = threading.Event()

# ---------- Expense class ----------
class Expense:
    """Represents a single expense item."""
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.user} - Rs.{self.amount}"


# ---------- Consumer thread ----------
class Consumer(threading.Thread):
    def __init__(self):
        super().__init__(name="Consumer")

    def run(self):
        while True:
            time.sleep(2)  # simulate delay in processing
            event.wait()  # wait for signal from Producer

            if not expenses:
                # if producer finished and list empty
                logging.info("📭 No more expenses to consume.")
                break

            exp = expenses.pop(0)
            logging.info(f"🗑️ Consumer processed: {exp} (Remaining: {len(expenses)})")

            event.clear()  # pause consumer until next item


# ---------- Producer thread ----------
class Producer(threading.Thread):
    def __init__(self, users):
        super().__init__(name="Producer")
        self.users = users

    def run(self):
        for _ in range(5):
            time.sleep(2)
            user = random.choice(self.users)
            amount = random.randint(100, 1000)
            exp = Expense(user, amount)
            expenses.append(exp)

            logging.info(f"➕ Producer added: {exp} (Total: {len(expenses)})")

            # notify the consumer
            event.set()
            event.clear()

        # when done, signal consumer to stop
        event.set()


# ---------- Main Function ----------
def main():
    users = ["Alishba", "Sara", "Hina", "Noor"]
    producer = Producer(users)
    consumer = Consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    logging.info("✅ Producer and Consumer finished execution.")


if __name__ == "__main__":
    main()
