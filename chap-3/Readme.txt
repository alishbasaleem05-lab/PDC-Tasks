🧵 Python Multiprocessing – Chapter 3

Inter-Process Communication & Process Management

This project demonstrates 12 different Python multiprocessing concepts using practical examples.
Each file illustrates a different inter-process communication (IPC) technique or process management feature.

📂 Project Files (12 Total)
1️⃣ communicating_with_pipes.py

Demonstrates direct data transfer between processes using Pipes.

Two ends: send and receive.

Example: Parent → Child or Child → Parent communication.

2️⃣ communicating_with_queues.py

Uses Queue for process-safe communication.

Multiple producers and consumers.

Ideal for realistic message-passing without conflicts.

3️⃣ killing_process.py

Demonstrates terminating processes using terminate().

Difference between killing and joining a process.

4️⃣ spawning_processes.py

Shows how to spawn new processes.

Different start methods: spawn, fork, forkserver.

spawn is recommended for safety.

5️⃣ naming_process.py

Assigns custom names to processes.

Helps in debugging and log readability.

Example: "Worker-1", "Downloader-Process".

6️⃣ process_pool.py

Demonstrates process pools for parallel task execution.

Automatic process management.

Methods used: map, starmap, apply, apply_async.

7️⃣ barrier_example.py

Uses Barrier to synchronize multiple processes.

Processes wait at a point and continue together.

8️⃣ process_with_subclass.py

Shows subclassing multiprocessing.Process.

Override the run() method.

Object-oriented approach to process creation.

9️⃣ run_bg_process.py

Runs a background process.

Main program continues without being blocked.

Useful for logging, monitoring, or background tasks.

🔟 run_bg_process_no_daemon.py

Background process without daemon flag.

Child process continues running even after the main program exits.

Best for long-running background tasks.

1️⃣1️⃣ run_bg_process_daemon.py

Background daemon process.

Automatically terminates when the main program ends.

Ideal for short-lived background work.

1️⃣2️⃣ multiprocessing_overview.py

Introductory file covering basic multiprocessing concepts:

Process creation

Start & join

Target functions

Requirements

Python 3.7+

Built-in multiprocessing module (no external libraries required)

Project Goal

This project is designed for beginners to understand inter-process communication and process management in Python.
Each file is a standalone demonstration of a key concept, providing hands-on examples.