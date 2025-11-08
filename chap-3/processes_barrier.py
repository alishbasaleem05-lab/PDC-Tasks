import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, sleep
from datetime import datetime

def record_expense_with_barrier(sync_barrier, lock):
    name = multiprocessing.current_process().name
    sync_barrier.wait()  # dono process ek saath start hon
    now = datetime.fromtimestamp(time())
    with lock:
        print(f"{name} ----> Expense recorded at {now}")

def record_expense_without_barrier():
    name = multiprocessing.current_process().name
    now = datetime.fromtimestamp(time())
    print(f"{name} ----> Expense recorded at {now}")

if __name__ == '__main__':
    # Barrier set for 2 processes
    sync_barrier = Barrier(2)
    lock = Lock()

    # Processes with barrier (wait for each other)
    Process(name='P1 - record_expense_with_barrier',
            target=record_expense_with_barrier,
            args=(sync_barrier, lock)).start()
    Process(name='P2 - record_expense_with_barrier',
            target=record_expense_with_barrier,
            args=(sync_barrier, lock)).start()

    # Processes without barrier (independent)
    Process(name='P3 - record_expense_without_barrier',
            target=record_expense_without_barrier).start()
    Process(name='P4 - record_expense_without_barrier',
            target=record_expense_without_barrier).start()
