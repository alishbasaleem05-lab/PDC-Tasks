import random

def simulate_expense_entry(count, out_list):
    for _ in range(count):
        expense = {
            "date": f"2025-11-{random.randint(1,30):02d}",
            "item": random.choice(["Tea", "Coffee", "Snacks", "Book", "Groceries"]),
            "cost": round(random.uniform(5, 200), 2)
        }
        out_list.append(expense)
