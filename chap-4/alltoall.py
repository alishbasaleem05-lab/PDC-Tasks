# expense_tracker_mpi.py
from mpi4py import MPI
import numpy as np

# Initialize communicator
comm = MPI.COMM_WORLD
size = comm.Get_size()     # total processes
rank = comm.Get_rank()     # current process ID

# Simulated expense data (each process creates its own)
# Example: Branch 0 has expenses [0, 0, 0, ...], Branch 1 has [1, 2, 3, ...]
send_data = (rank + 1) * np.arange(size, dtype=int)

# Prepare empty array to receive data from all processes
recv_data = np.empty(size, dtype=int)

# Alltoall communication: every process sends to every other process
comm.Alltoall(send_data, recv_data)

# Display results
print(f"[Branch {rank}] Sent: {send_data} | Received: {recv_data}")
