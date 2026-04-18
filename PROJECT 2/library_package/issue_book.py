from .logic import issue_book_record

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