# expense_tracker_scatter.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Root process (rank 0) has the complete expense list
if rank == 0:
    total_expenses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    print(f"Root process distributing expense data: {total_expenses}")
else:
    total_expenses = None  # Other processes will receive part of it

# Scatter — distributes one element to each process
my_expense = comm.scatter(total_expenses, root=0)

print(f"Process {rank} received expense: {my_expense}")
