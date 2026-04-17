from .logic import add_book_record, get_all_books, issue_book_record, return_book_record

def print_divider():
    print("-" * 65)

def display_menu():
    print("\n" + "=" * 65)
    print(" 📚 CENTRAL LIBRARY MANAGEMENT SYSTEM ".center(65))
    print("=" * 65)
    print("  [1] Add a New Book")
    print("  [2] View All Books")
    print("  [3] Issue a Book")
    print("  [4] Return a Book")
    print("  [5] View Fine Policy")
    print("  [0] Exit System")
    print("=" * 65)

def show_fine_notice():
    print("\n" + "!" * 65)
    print(" LATE RETURN FINE POLICY ".center(65))
    print("!" * 65)
    print(" Fines are applied daily for overdue books. The rate")
    print(" increases exponentially for every week it is late:\n")
    print("   • 1st Week Overdue : Rs. 10 / day")
    print("   • 2nd Week Overdue : Rs. 20 / day  (10 * 2)")
    print("   • 3rd Week Overdue : Rs. 60 / day  (10 * 2 * 3)")
    print("   • 4th Week Overdue : Rs. 240 / day (10 * 2 * 3 * 4)")
    print("!" * 65)

def handle_add():
    print("\n--- ADD A NEW BOOK ---")
    b_id = input(" ➤ Enter Book ID (e.g., B101): ").strip().upper()
    title = input(" ➤ Enter Book Title: ").strip().title()
    author = input(" ➤ Enter Author Name: ").strip().title()
    
    success, msg = add_book_record(b_id, title, author)
    print(f"\n {'[✓]' if success else '[!]'} {msg}")

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

def handle_issue():
    print("\n--- ISSUE A BOOK ---")
    b_id = input(" ➤ Enter Book ID: ").strip().upper()
    student = input(" ➤ Enter Student Name: ").strip().title()
    date_str = input(" ➤ Enter Issue Date (YYYY-MM-DD): ").strip()
    days = input(" ➤ Enter Allotted Days (e.g., 7): ").strip()
    
    if not days.isdigit():
        print("\n [!] Allotted days must be a whole number.")
        return
        
    show_fine_notice()
    
    success, msg = issue_book_record(b_id, student, date_str, int(days))
    print(f"\n {'[✓]' if success else '[!]'} {msg}")

def handle_return():
    print("\n--- RETURN A BOOK ---")
    b_id = input(" ➤ Enter Book ID: ").strip().upper()
    date_str = input(" ➤ Enter Today's Date (YYYY-MM-DD): ").strip()
    
    success, msg, fine = return_book_record(b_id, date_str)
    
    print("\n" + "*" * 40)
    print(f" {'[✓]' if success else '[!]'} {msg}")
    if success and fine > 0:
        print(f" [!] TOTAL FINE APPLIED: Rs. {fine}")
        print("     Please collect payment immediately.")
    print("*" * 40)

def start_application():
    """The infinite loop driving the system."""
    while True:
        display_menu()
        choice = input(" ➤ Select an operation (0-5): ").strip()
        
        if choice == '1':
            handle_add()
        elif choice == '2':
            handle_show()
        elif choice == '3':
            handle_issue()
        elif choice == '4':
            handle_return()
        elif choice == '5':
            show_fine_notice()
        elif choice == '0':
            print("\n Saving data... Shutting down system. Goodbye!\n")
            break
        else:
            print("\n [!] Invalid selection. Please choose a number between 0 and 5.")