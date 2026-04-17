from .logic import get_balance, deposit, withdraw, get_statement

def display_menu():
    print("\n" + "=" * 50)
    print(" 🏦 SECURE ATM SYSTEM ".center(50))
    print("=" * 50)
    print("  [1] Display Balance")
    print("  [2] Deposit Money")
    print("  [3] Withdraw Money")
    print("  [4] View Statement")
    print("  [0] Exit / Take Card")
    print("=" * 50)

def handle_balance():
    print("\n--- CURRENT BALANCE ---")
    print(f" Available Balance: Rs. {get_balance():.2f}")

def handle_deposit():
    print("\n--- DEPOSIT MONEY ---")
    try:
        amount = float(input(" ➤ Enter amount to deposit: Rs. "))
        success, msg = deposit(amount)
        print(f"\n {'[✓]' if success else '[!]'} {msg}")
    except ValueError:
        print("\n [!] Invalid input. Please enter numbers only.")

def handle_withdraw():
    print("\n--- WITHDRAW MONEY ---")
    try:
        amount = float(input(" ➤ Enter amount to withdraw: Rs. "))
        success, msg = withdraw(amount)
        print(f"\n {'[✓]' if success else '[!]'} {msg}")
    except ValueError:
        print("\n [!] Invalid input. Please enter numbers only.")

def handle_statement():
    print("\n" + " TRANSACTION STATEMENT ".center(50, "-"))
    transactions = get_statement()
    
    if not transactions:
        print(" No transactions yet.")
    else:
        for idx, transaction in enumerate(transactions, 1):
            print(f" {idx:02d} | {transaction}")
            
    print("-" * 50)
    print(f" Current Balance: Rs. {get_balance():.2f}")

def start_application():
    """The infinite loop driving the ATM interface."""
    while True:
        display_menu()
        choice = input(" ➤ Select an option (0-4): ").strip()
        
        if choice == '1':
            handle_balance()
        elif choice == '2':
            handle_deposit()
        elif choice == '3':
            handle_withdraw()
        elif choice == '4':
            handle_statement()
        elif choice == '0':
            print("\n Transaction complete. Please take your card. Goodbye!\n")
            break
        else:
            print("\n [!] Invalid selection. Please choose a number between 0 and 4.")