import multiprocessing
import random
import time

# same function as yours 👇
def myFunc(i):
    print('calling myFunc from process n°: %s' % i)
    for j in range(0, i):
        print('output from myFunc is :%s' % j)
    return

# producer process
def add_expenses(queue):
    for i in range(3):
        expense = ("Expense_" + str(i), random.randint(100, 500))
        queue.put(expense)
        print(f"Producer added: {expense}")
        myFunc(i + 1)   # 👈 yahan call kia gaya hai
        time.sleep(1)

# consumer process
def view_expenses(queue):
    time.sleep(2)
    while not queue.empty():
        expense = queue.get()
        print(f"Consumer viewed: {expense}")
        myFunc(2)   # 👈 yahan bhi call kia gaya hai
        time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=add_expenses, args=(queue,))
    p2 = multiprocessing.Process(target=view_expenses, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("End of Expense Tracker Process")
