 Expense Tracker Performance Test

This project is a performance benchmarking tool for the Expense Tracker system.  
It compares Threading and Multiprocessing in Python by simulating expense entry operations using different worker counts (5, 10, and 50).

 Features

- Tests both thread-based and process-based parallelism.
- Automatically compares execution time for:
  - 5 workers
  - 10 workers
  - 50 workers
- Uses realistic simulated expense entries.
- Helps determine the most efficient configuration for your Expense Tracker.


 Project Structure
├── simulate_task.py # Worker function for simulating expense entries
├── stress_test_expense_tracker.py # Main test script (threading & multiprocessing)
└── README.md # Project documentation
