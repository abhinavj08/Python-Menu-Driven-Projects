from .logic import return_book_record

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