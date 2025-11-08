import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import multiprocessing
import time

# Function 1: Create (Produce) Expenses

def produce_expenses(pipe):
    output_pipe, _ = pipe
    expenses = [
        ("Tea", 10),
        ("Snacks", 30),
        ("Travel", 100),
        ("Books", 250),
        ("Lunch", 150)
    ]
    for item, amount in expenses:
        time.sleep(1)
        expense_data = {"item": item, "amount": amount}
        output_pipe.send(expense_data)
        print(f"[Producer] Sent: {expense_data}")
    output_pipe.close()


# Function 2: Process (Multiply) Expenses

def process_expenses(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            expense = input_pipe.recv()
            expense["amount"] *= 2  # Example processing: doubling cost
            output_pipe.send(expense)
            print(f"[Processor] Processed: {expense}")
    except EOFError:
        output_pipe.close()


# Function 3: GUI Application

def start_expense_tracker(pipe):
    root = tk.Tk()
    root.title("Expense Tracker (with Multiprocessing Pipes)")
    root.geometry("600x400")

    columns = ("Item", "Amount", "Date")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill=tk.BOTH, expand=True, pady=20)

    def update_expenses():
        try:
            while True:
                expense = pipe.recv()
                expense["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tree.insert('', tk.END, values=(expense["item"], expense["amount"], expense["date"]))
                root.update()
        except EOFError:
            print("No more data in pipe.")

    # Start updating expenses in GUI
    root.after(100, update_expenses)
    root.mainloop()


# MAIN

if __name__ == "__main__":
    # Create first pipe (for sending original expenses)
    pipe_1 = multiprocessing.Pipe(True)
    producer = multiprocessing.Process(target=produce_expenses, args=(pipe_1,))
    producer.start()

    # Create second pipe (for sending processed expenses)
    pipe_2 = multiprocessing.Pipe(True)
    processor = multiprocessing.Process(target=process_expenses, args=(pipe_1, pipe_2))
    processor.start()

    # Close unnecessary pipe ends in main
    pipe_1[0].close()
    pipe_2[0].close()

    # Start GUI to receive and display processed expenses
    start_expense_tracker(pipe_2[1])

    producer.join()
    processor.join()

    print("All processes completed successfully!")
