#   Creating a User Account Create a class called PersonAccount. It has firstname, lastname, 
# incomes, expenses properties and it has total_income, total_expense, account_info, 
# add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description.
#  The same goes for expenses.
#!/usr/bin/env python3

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  # List to store (amount, description) tuples
        self.expenses = []  # List to store (amount, description) tuples

    def add_income(self, amount, description=""):
        """Adds an income with a description."""
        self.incomes.append((amount, description))

    def add_expense(self, amount, description=""):
        """Adds an expense with a description."""
        self.expenses.append((amount, description))

    def total_income(self):
        """Calculates total income."""
        return sum(income[0] for income in self.incomes)

    def total_expense(self):
        """Calculates total expenses."""
        return sum(expense[0] for expense in self.expenses)

    def account_balance(self):
        """Calculates account balance."""
        return self.total_income() - self.total_expense()

    def account_info(self):
        """Returns a summary of the account."""
        return f"Account Holder: {self.firstname} {self.lastname}\n" \
               f"Total Income: {self.total_income()}\n" \
               f"Total Expenses: {self.total_expense()}\n" \
               f"Account Balance: {self.account_balance()}"


# Example usage:
account = PersonAccount("Mark", "Gitonga")

# Adding incomes
account.add_income(5000, "Salary")
account.add_income(2000, "Freelance work")

# Adding expenses
account.add_expense(1500, "Rent")
account.add_expense(500, "Groceries")

# Printing account information
print(account.account_info())