# expense_tracker_mpi.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("My rank is:", rank)

if rank == 0:
    total_expense = 2500
    destination_process = 4
    comm.send(total_expense, dest=destination_process)
    print("Process 0 sending total expense %s to process %d" % (total_expense, destination_process))

if rank == 1:
    expense_note = "Lunch Expense: 500"
    destination_process = 8
    comm.send(expense_note, dest=destination_process)
    print("Process 1 sending note '%s' to process %d" % (expense_note, destination_process))

if rank == 4:
    received_data = comm.recv(source=0)
    print("Process 4 received total expense data:", received_data)

if rank == 8:
    received_note = comm.recv(source=1)
    print("Process 8 received note:", received_note)
