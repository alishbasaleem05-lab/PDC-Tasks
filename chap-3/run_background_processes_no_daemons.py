import multiprocessing
import time

def expense_task():
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    if name == 'background_tracker':
        for i in range(0, 5):
            print(f"{name} ---> Checking new expenses {i}\n")
            time.sleep(1)
    else:
        for i in range(5, 10):
            print(f"{name} ---> Adding new expense {i}\n")
            time.sleep(1)

    print(f"Exiting {name}\n")


if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_tracker',
        target=expense_task
    )
    background_process.daemon = False  # Background tracker

    main_process = multiprocessing.Process(
        name='main_user_process',
        target=expense_task
    )
    main_process.daemon = False  # User adds expenses

    background_process.start()
    main_process.start()
