import logging
import threading
import time
import random
import os

# Logging setup for thread info
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared data (like a wallet or list of expenses)
expenses = []

# Semaphore: controls synchronization between producer and consumer
semaphore = threading.Semaphore(0)
threadLock = threading.Lock()


# 🧾 Consumer Thread (reads expenses)
def consumer():
    logging.info('Consumer waiting for new expense...')

    # Wait for producer to add data
    semaphore.acquire()

    # Once allowed, consume safely
    with threadLock:
        if expenses:
            expense = expenses.pop(0)
            logging.info(f'Consumer processed expense: {expense}')
        else:
            logging.info('No expenses available to consume.')


# 💸 Producer Thread (adds new expense)
def producer():
    time.sleep(random.randint(1, 3))  # simulate delay
    expense = random.randint(100, 1000)

    with threadLock:
        expenses.append(expense)
        logging.info(f'Producer added expense: {expense} (PID: {os.getpid()})')

    # Notify consumer
    semaphore.release()


def main():
    threads = []

    for i in range(5):
        # Create a consumer–producer pair
        t_consumer = threading.Thread(target=consumer, name=f"Consumer-{i+1}")
        t_producer = threading.Thread(target=producer, name=f"Producer-{i+1}")

        threads.append(t_consumer)
        threads.append(t_producer)

        # Start threads
        t_consumer.start()
        t_producer.start()

    # Wait for all threads
    for t in threads:
        t.join()

    logging.info("✅ All producer-consumer threads finished.")
    logging.info(f"Final expenses list: {expenses}")


if __name__ == "__main__":
    main()
