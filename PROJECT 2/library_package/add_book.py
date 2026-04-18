from .logic import add_book_record

def handle_add():
    print("\n--- ADD A NEW BOOK ---")
    b_id = input(" ➤ Enter Book ID (e.g., B101): ").strip().upper()
    title = input(" ➤ Enter Book Title: ").strip().title()
    author = input(" ➤ Enter Author Name: ").strip().title()
    
    success, msg = add_book_record(b_id, title, author)
    print(f"\n {'[✓]' if success else '[!]'} {msg}")