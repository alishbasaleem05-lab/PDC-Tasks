import multiprocessing
import random
import time

def process_expense(amount):
    print(f'Processing expense: Rs.{amount}')
    time.sleep(1)
    return f'Expense Rs.{amount} processed'

if __name__ == '__main__':
    expenses = [random.randint(100, 500) for _ in range(10)]

    pool = multiprocessing.Pool(processes=4)
    results = pool.map(process_expense, expenses)

    pool.close()
    pool.join()

    print("\nExpense Summary:")
    for r in results:
        print(r)
