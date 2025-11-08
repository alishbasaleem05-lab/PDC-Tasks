import multiprocessing

def add_expense(day):
    print(f"Processing expenses for Day {day}")
    for i in range(day):
        print(f"Expense {i + 1} recorded for Day {day}")
    return

if __name__ == '__main__':
    for day in range(1, 6):
        process = multiprocessing.Process(target=add_expense, args=(day,))
        process.start()
        process.join()
