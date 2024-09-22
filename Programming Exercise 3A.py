from functools import reduce


def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        amount = float(input(f"Enter the amount for {expense_type}: "))
        expenses.append((expense_type, amount))
    return expenses


def calculate_total(expenses):
    return reduce(lambda total, expense: total + expense[1], expenses, 0)


def find_highest(expenses):
    return max(expenses, key=lambda x: x[1])


def find_lowest(expenses):
    return min(expenses, key=lambda x: x[1])


def main():
    expenses = get_expenses()
    if not expenses:
        print("No expenses were entered.")
        return

    total = calculate_total(expenses)
    highest = find_highest(expenses)
    lowest = find_lowest(expenses)

    print(f"\nTotal Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")


if __name__ == "__main__":
    main()

