import threading
import multiprocessing
import time
from simulate_task import simulate_expense_entry  

NUM_WORKERS_LIST = [5, 10, 50]
SIZE_EACH = 100000

def run_thread_test(num_threads, size_each):
    out_list = []
    start_time = time.time()
    jobs = []
    for _ in range(num_threads):
        t = threading.Thread(target=simulate_expense_entry, args=(size_each, out_list))
        jobs.append(t)
    for j in jobs: j.start()
    for j in jobs: j.join()
    print(f"🧵 {num_threads} threads completed in {time.time() - start_time:.2f} sec")

def run_process_test(num_processes, size_each):
    manager = multiprocessing.Manager()
    out_list = manager.list()
    start_time = time.time()
    jobs = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=simulate_expense_entry, args=(size_each, out_list))
        jobs.append(p)
    for j in jobs: j.start()
    for j in jobs: j.join()
    print(f"⚙️ {num_processes} processes completed in {time.time() - start_time:.2f} sec")

if __name__ == "__main__":
    print("Running threading and multiprocessing comparison...\n")

    print(" THREADING TEST ")
    for workers in NUM_WORKERS_LIST:
        run_thread_test(workers, SIZE_EACH)

    print("\n MULTIPROCESSING TEST ")
    for workers in NUM_WORKERS_LIST:
        run_process_test(workers, SIZE_EACH)
