import multiprocessing
import random
import time

class ExpenseProcess(multiprocessing.Process):
    def run(self):
        expense = random.randint(100, 500)
        print(f'[{self.name}] Added expense: Rs.{expense}')
        time.sleep(1)
        print(f'[{self.name}] Finished processing expense.\n')


if __name__ == '__main__':
    for i in range(5):
        process = ExpenseProcess(name=f'ExpenseProcess-{i+1}')
        process.start()
        process.join()
