# expense_tracker_send_recv.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("Process rank: %i" % rank)

# Suppose branch 1 and branch 5 exchange expense summaries
if rank == 1:
    data_send = "Branch 1 Expense Summary: $1200"
    destination_process = 5
    source_process = 5

    # First receive, then send (to avoid deadlock)
    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print(f"[Branch 1] Sent data → {destination_process}: {data_send}")
    print(f"[Branch 1] Received data ← {source_process}: {data_received}")

elif rank == 5:
    data_send = "Branch 5 Expense Summary: $980"
    destination_process = 1
    source_process = 1

    # First send, then receive (to avoid deadlock)
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)

    print(f"[Branch 5] Sent data → {destination_process}: {data_send}")
    print(f"[Branch 5] Received data ← {source_process}: {data_received}")
