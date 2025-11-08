from mpi4py import MPI

# Initialize communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Each process adds its own expense amount
# (you can think of each process as a user)
expense = (rank + 1) * 1000  # example expense: process 0 = 1000, process 1 = 2000, etc.

# Gather all expenses to the root process (rank 0)
all_expenses = comm.gather(expense, root=0)

# Root process prints total report
if rank == 0:
    print("=== Expense Tracker (Gather Example) ===")
    print(f"Rank {rank} is collecting data from all {size} processes...\n")

    total = 0
    for i in range(size):
        print(f"Received expense {all_expenses[i]} from process {i}")
        total += all_expenses[i]

    print(f"\nTotal Expense Collected: {total}")
