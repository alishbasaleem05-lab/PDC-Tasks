import multiprocessing
import time
import random

def expense_tracker():
    name = multiprocessing.current_process().name
    print("Starting process name = %s \n" % name)
    
    # simulate expense-related task
    if "Adder" in name:
        for i in range(3):
            expense = random.randint(100, 500)
            print(f"{name} added expense: Rs.{expense}")
            time.sleep(1)
    else:
        for i in range(3):
            print(f"{name} viewed expense record #{i+1}")
            time.sleep(1)
    
    print("Exiting process name = %s \n" % name)


if __name__ == '__main__':
    # Process 1: Expense Adder
    process_with_name = multiprocessing.Process(
        name='Expense_Adder_Process',
        target=expense_tracker
    )

    # Process 2: Expense Viewer
    process_with_default_name = multiprocessing.Process(
        name='Expense_Viewer_Process',
        target=expense_tracker
    )

    # Start processes
    process_with_name.start()
    process_with_default_name.start()

    # Wait for both to finish
    process_with_name.join()
    process_with_default_name.join()

    print("All Expense Tracker processes completed.\n")
