import multiprocessing
import time

def expense_task():
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    if name == 'background_expense_checker':
        # Background process checking updates
        for i in range(0, 5):
            print(f"{name} ---> Checking expense update {i}\n")
            time.sleep(1)
    else:
        # Foreground process adding expenses
        for i in range(5, 10):
            print(f"{name} ---> Adding new expense {i}\n")
            time.sleep(1)

    print(f"Exiting {name}\n")


if __name__ == '__main__':
    # Daemon process (runs in background)
    background_process = multiprocessing.Process(
        name='background_expense_checker',
        target=expense_task
    )
    background_process.daemon = True

    # Normal process (runs in foreground)
    main_process = multiprocessing.Process(
        name='main_expense_adder',
        target=expense_task
    )
    main_process.daemon = False

    background_process.start()
    main_process.start()
