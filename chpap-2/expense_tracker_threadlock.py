import threading
import time
import os
from random import randint
from threading import Thread

# Shared resource: expense list
expenses = []

# Define a Lock for synchronization
threadLock = threading.Lock()

class ExpenseThread(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire Lock before accessing shared resource
        threadLock.acquire()
        try:
            print(f"\n---> {self.name} running (PID: {os.getpid()})")
            
            # Simulate adding expense
            expense = randint(100, 1000)
            expenses.append(expense)
            print(f"{self.name} added expense: {expense}")
            print(f"Current expenses: {expenses}")

        finally:
            # Always release Lock (even if error)
            threadLock.release()

        # Simulate processing time
        time.sleep(self.duration)
        print(f"---> {self.name} completed in {self.duration} sec\n")


def main():
    start_time = time.time()

    # Create multiple expense threads
    threads = []
    for i in range(1, 10):
        t = ExpenseThread(f"UserThread#{i}", randint(1, 5))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all to finish
    for t in threads:
        t.join()

    # Final result
    print("\n✅ All threads finished.")
    print(f"Final expense list: {expenses}")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
