import csv
import os
from datetime import datetime

FILE = "expenses.csv"

def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "note"])

def add_expense():
    date = input("Date (YYYY-MM-DD, leave empty for today): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Category (Food, Travel, etc): ").strip()
    amount = float(input("Amount: "))
    note = input("Note (optional): ").strip()

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully.\n")

def view_summary():
    expenses = {}
    total = 0

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amt = float(row["amount"])
            cat = row["category"]
            total += amt
            expenses[cat] = expenses.get(cat, 0) + amt

    print("\n📊 Expense Summary")
    print("-" * 30)
    for cat, amt in expenses.items():
        print(f"{cat}: ₹{amt:.2f}")
    print(f"\n💰 Total Spending: ₹{total:.2f}")

    highest = max(expenses, key=expenses.get)
    print(f"🔥 Highest Spending Category: {highest}")

def filter_by_date():
    start = input("Start date (YYYY-MM-DD): ")
    end = input("End date (YYYY-MM-DD): ")

    start_d = datetime.fromisoformat(start)
    end_d = datetime.fromisoformat(end)

    print("\n📅 Expenses in Range\n")

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = datetime.fromisoformat(row["date"])
            if start_d <= d <= end_d:
                print(f"{row['date']} | {row['category']} | ₹{row['amount']} | {row['note']}")

def main():
    init_file()

    while True:
        print("\n📈 Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Filter by Date")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            filter_by_date()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
