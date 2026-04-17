import math
from datetime import datetime

# Central dictionary replacing the old lists
books_db = {}

def add_book_record(book_id, title, author):
    """Adds a new book to the dictionary."""
    if book_id in books_db:
        return False, "Error: Book ID already exists."
    
    books_db[book_id] = {
        "title": title,
        "author": author,
        "status": "Available",
        "student_name": None,
        "issue_date": None,
        "allotted_days": 0
    }
    return True, f"Book '{title}' added successfully!"

def get_all_books():
    """Returns the current database."""
    return books_db

def calculate_fine(days_overdue):
    """Calculates fine based on escalating weekly tiers (10, 20, 60...)."""
    if days_overdue <= 0:
        return 0
    
    total_fine = 0
    remaining_days = days_overdue
    week = 1
    
    while remaining_days > 0:
        days_in_current_week = min(remaining_days, 7)
        
        # Rate pattern: W1=10, W2=10*2, W3=10*2*3 -> 10 * factorial(week)
        rate_per_day = 10 * math.factorial(week)
        
        total_fine += days_in_current_week * rate_per_day
        remaining_days -= days_in_current_week
        week += 1
        
    return total_fine

def issue_book_record(book_id, student_name, issue_date_str, allotted_days):
    """Updates the dictionary to mark a book as issued with dates."""
    if book_id not in books_db:
        return False, "Error: Book ID not found."
    if books_db[book_id]["status"] == "Issued":
        return False, "Error: Book is already issued."
    
    try:
        valid_date = datetime.strptime(issue_date_str, "%Y-%m-%d").date()
    except ValueError:
        return False, "Error: Invalid date format. Use YYYY-MM-DD."

    # Update the dictionary
    books_db[book_id]["status"] = "Issued"
    books_db[book_id]["student_name"] = student_name
    books_db[book_id]["issue_date"] = valid_date
    books_db[book_id]["allotted_days"] = int(allotted_days)
    
    return True, f"Book issued successfully to {student_name}."

def return_book_record(book_id, return_date_str):
    """Calculates days kept, generates fines, and resets the book record."""
    if book_id not in books_db:
        return False, "Error: Book ID not found.", 0
    if books_db[book_id]["status"] == "Available":
        return False, "Error: This book is not currently issued.", 0
        
    try:
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
    except ValueError:
        return False, "Error: Invalid date format. Use YYYY-MM-DD.", 0

    issue_date = books_db[book_id]["issue_date"]
    allotted_days = books_db[book_id]["allotted_days"]
    
    # Calculate overdue status
    days_kept = (return_date - issue_date).days
    if days_kept < 0:
        return False, "Error: Return date cannot be before issue date.", 0

    days_overdue = days_kept - allotted_days
    fine = calculate_fine(days_overdue)
    
    # Reset the dictionary record
    books_db[book_id]["status"] = "Available"
    books_db[book_id]["student_name"] = None
    books_db[book_id]["issue_date"] = None
    books_db[book_id]["allotted_days"] = 0
    
    msg = "Book returned successfully."
    if days_overdue > 0:
        msg += f" It was {days_overdue} days late."
        
    return True, msg, fine
