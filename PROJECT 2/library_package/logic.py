import math
from datetime import datetime

# Simple database
books_db = {}

# ➤ Add Book
def add_book(book_id, title, author):
    if book_id in books_db:
        return "Book ID already exists!"

    books_db[book_id] = {
        "title": title,
        "author": author,
        "status": "Available",
        "student": "",
        "issue_date": "",
        "days": 0
    }
    return "Book added successfully!"

# ➤ Show Books
def show_books():
    return books_db

# ➤ Calculate Fine (simplified logic)
def calculate_fine(days_late):
    if days_late <= 0:
        return 0

    fine = 0
    week = 1

    while days_late > 0:
        days = min(7, days_late)
        fine += days * (10 * math.factorial(week))
        days_late -= days
        week += 1

    return fine

# ➤ Issue Book
def issue_book(book_id, student, date_str, days):
    if book_id not in books_db:
        return "Book not found!"
    
    if books_db[book_id]["status"] == "Issued":
        return "Book already issued!"

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except:
        return "Wrong date format!"

    books_db[book_id]["status"] = "Issued"
    books_db[book_id]["student"] = student
    books_db[book_id]["issue_date"] = date
    books_db[book_id]["days"] = int(days)

    return "Book issued!"

# ➤ Return Book
def return_book(book_id, return_date_str):
    if book_id not in books_db:
        return "Book not found!", 0

    if books_db[book_id]["status"] == "Available":
        return "Book not issued!", 0

    try:
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
    except:
        return "Wrong date format!", 0

    issue_date = books_db[book_id]["issue_date"]
    allowed_days = books_db[book_id]["days"]

    days_kept = (return_date - issue_date).days

    if days_kept < 0:
        return "Invalid return date!", 0

    late_days = days_kept - allowed_days
    fine = calculate_fine(late_days)

    # Reset book
    books_db[book_id]["status"] = "Available"
    books_db[book_id]["student"] = ""
    books_db[book_id]["issue_date"] = ""
    books_db[book_id]["days"] = 0

    return "Book returned!", fine