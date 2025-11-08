# expense_tracker_reduce.py
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

# Har process apna khud ka expense list banata hai
array_size = 5
my_expenses = (rank + 1) * np.arange(array_size, dtype=np.int32)

# Ye array total (sum) receive karega root process par
total_expenses = np.zeros(array_size, dtype=np.int32)

print(f"Process {rank} sending its expense data: {my_expenses}")

# Reduce operation — sab processes ke data ko combine karke root(0) pe bhejta hai
comm.Reduce(my_expenses, total_expenses, root=0, op=MPI.SUM)

# Root process (rank 0) total show karega
if rank == 0:
    print(f"\nFinal Total Expense collected from all processes: {total_expenses}")
