# expense.py
# ==========================================
# Defines the Expense class to represent an expense entry.

class Expense:
    """Represents an expense record with amount, category, and date."""
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        """Returns a readable string representation of the expense."""
        return f"Amount: {self.amount}, Category: {self.category}, Date: {self.date}"
