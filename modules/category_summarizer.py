# category_summarizer.py
# ==========================================
# Provides logic for summarizing expenses by category.

def summarize_by_category(expenses):
    """Groups expenses by category and returns totals."""
    summary = {}
    for amount, category, _ in expenses:
        summary[category] = summary.get(category, 0) + float(amount)
    return summary
