import multiprocessing
import time


# Producer Process (AddExpense)

class AddExpense(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        # Example list of expenses
        expenses = [
            ("Tea", 50),
            ("Lunch", 200),
            ("Transport", 100),
            ("Snacks", 80),
            ("Dinner", 250)
        ]
        for item in expenses:
            print(f"🧾 Adding expense: {item}")
            self.queue.put(item)
            time.sleep(1)   # simulate delay between entries
        print("✅ All expenses have been added!\n")


# Consumer Process (DisplayDashboard)

class DisplayDashboard(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        time.sleep(0.5)  # small delay so producer starts first
        while True:
            if self.queue.empty():
                print("⚠️  No more expenses to display. Exiting Dashboard...\n")
                break
            expense = self.queue.get()
            print(f"📊 Dashboard updated → {expense}")
            time.sleep(1)


# Main Program

if __name__ == "__main__":
    # Create a multiprocessing Queue
    queue = multiprocessing.Queue()

    # Create Producer and Consumer processes
    producer = AddExpense(queue)
    consumer = DisplayDashboard(queue)

    # Start both processes
    producer.start()
    consumer.start()

    # Wait for both to finish
    producer.join()
    consumer.join()

    print("🏁 Program finished successfully!")
