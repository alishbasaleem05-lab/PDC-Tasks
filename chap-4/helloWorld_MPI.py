# hello.py
from mpi4py import MPI

comm = MPI.COMM_WORLD     # communicator that connects all processes
rank = comm.Get_rank()    # get process number (rank)
print("Hello World from process", rank)
