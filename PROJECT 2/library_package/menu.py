# Importing the specific handlers from your new separated files
from .add_book import handle_add
from .show_books import handle_show
from .issue_book import handle_issue, show_fine_notice
from .return_book import handle_return

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