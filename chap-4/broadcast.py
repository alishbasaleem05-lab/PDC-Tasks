# expense_tracker_broadcast.py
from mpi4py import MPI

# Initialize communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Only process 0 (like Head Office) sets the budget
if rank == 0:
    monthly_budget = 50000   # Head Office sets total budget
    print(f"[Head Office] Set total monthly budget = {monthly_budget}")
else:
    monthly_budget = None    # Other branches don’t know yet

# Broadcast budget from process 0 to all others
monthly_budget = comm.bcast(monthly_budget, root=0)

# Each branch receives the same shared budget
print(f"[Branch {rank}] Received shared monthly budget = {monthly_budget}")
