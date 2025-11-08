# file_operations.py
# ==========================================
# Handles reading and writing expense data to a file.

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/expenses.txt')

def read_expenses():
    """Reads all expense records from the data file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        lines = file.readlines()
    expenses = [line.strip().split(',') for line in lines if line.strip()]
    return expenses

def write_expense(amount, category, date):
    """Appends a new expense entry to the data file."""
    with open(DATA_FILE, 'a') as file:
        file.write(f"{amount},{category},{date}\n")
