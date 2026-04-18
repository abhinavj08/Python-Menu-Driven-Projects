from .logic import get_all_books

def print_divider():
    print("-" * 65)

def handle_show():
    books = get_all_books()
    if not books:
        print("\n [!] The library currently has no books.")
        return
        
    print("\n" + " CURRENT BOOK INVENTORY ".center(65, "-"))
    print(f"{'ID':<6} | {'Title':<20} | {'Status':<10} | {'Issued To'}")
    print_divider()
    for b_id, details in books.items():
        student = details['student_name'] if details['student_name'] else "---"
        title_display = details['title'][:17] + "..." if len(details['title']) > 20 else details['title']
        print(f"{b_id:<6} | {title_display:<20} | {details['status']:<10} | {student}")
    print_divider()