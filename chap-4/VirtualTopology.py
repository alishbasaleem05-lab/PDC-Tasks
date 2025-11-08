# expense_tracker_grid_topology.py
from mpi4py import MPI
import numpy as np

# Directions for neighbor identification
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0, 0, 0, 0]

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    # Build a grid of processes (like a 2D expense cluster)
    grid_row = int(np.floor(np.sqrt(size)))
    grid_column = size // grid_row

    # Adjust if grid too large
    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    if rank == 0:
        print(f"\n🧾 Expense Tracker Grid Topology: {grid_row} x {grid_column}\n")

    # Create Cartesian communicator (like grid connections)
    cartesian_comm = comm.Create_cart(
        (grid_row, grid_column), periods=(True, True), reorder=True
    )

    # Get coordinates of each process in the grid
    my_row, my_col = cartesian_comm.Get_coords(cartesian_comm.rank)

    # Find neighbors (up, down, left, right)
    neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_comm.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_comm.Shift(1, 1)

    print(
        f"Process {rank} at (Row={my_row}, Col={my_col})\n"
        f"  ↑ UP = {neighbour_processes[UP]}\n"
        f"  ↓ DOWN = {neighbour_processes[DOWN]}\n"
        f"  ← LEFT = {neighbour_processes[LEFT]}\n"
        f"  → RIGHT = {neighbour_processes[RIGHT]}\n"
    )
