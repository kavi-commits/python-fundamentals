#day 4 week 4 modules and project structure

# 1. import and from x import y

import math
print (math.sqrt(16))

from math import sqrt
print (sqrt(16))

# 2. the _main_ guard
#importing a file runs it top to bottom. Put tast code under if _name_ == "_main_": so it runs only  when you execute that file directly,  not when another file imports it

# 3.  datetime basics
from datetime import date, datetime

d = date.today()        # 2026-10-29
s = d.isoformat()       # "2026-10-29"  (string, JSON-safe)
d2 = date.fromisoformat("2026-10-29")  # string back to date
print(d.strftime("%d %b %Y"))    # 29 Oct 2026
now = datetime.now()    # date+time
 # JSON cannot store dat objects. Convert to a string on save(isoformat) and back on load (fromisoformat)

# build  expense.py

from  datetime import date

class Expense:
    def __init__(self, amount, category, description, expense_date=None):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = expense_date if expense_date is not None else date.today()


    def __str__(self):
        return f"{self.date.isoformat()} | {self.category} | {self.amount:.2f} | {self.description}"

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat(),

        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["amount"],
            data["category"],
            data["description"],
            date.Fromisoformat(data["date"]),
        )

# 5. Build stroge.py

import json
from expense import Expense
def save_expenses(expenses, filename="expenses.json"):
    data = [e.to_dice() for e in expenses]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    return [Expense.from_dict(d) for d in data]

if __name__ == "__main__":
    items = [
        Expense(450, "Food", "Lunch"),
        Expense(1200.5, "Transport", "Bus pass"),
    ]
    save_expenses(items)
    loaded = load_expenses()
    for e in loaded:
        print(e)

