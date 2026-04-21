import time

# Fake database (in-memory)
accounts = {
    "Abhinav": {
        "pin": "1234",
        "balance": 5000,
        "history": []
    },
    "Alex": {
        "pin": "1111",
        "balance": 3000,
        "history": []
    }
}


def add_history(user, msg):
    accounts[user]["history"].append(msg)


def login():
    print("🏦 Welcome to Advanced ATM")

    user = input("Enter username: ")
    pin = input("Enter PIN: ")

    if user in accounts and accounts[user]["pin"] == pin:
        print("✅ Login Successful\n")
        return user
    else:
        print("❌ Invalid username or PIN")
        return None


def atm_menu(user):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter choice: ")

        # CHECK BALANCE
        if choice == "1":
            print(f"💰 Balance: {accounts[user]['balance']}")
            add_history(user, "Checked balance")

        # DEPOSIT
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                accounts[user]["balance"] += amount
                add_history(user, f"Deposited {amount}")
                print("✅ Deposit successful")
            else:
                print("❌ Invalid amount")

        # WITHDRAW
        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))

            if amount <= accounts[user]["balance"]:
                accounts[user]["balance"] -= amount
                add_history(user, f"Withdrew {amount}")
                print("✅ Withdraw successful")
            else:
                print("❌ Insufficient balance")

        # HISTORY
        elif choice == "4":
            print("\n📊 Transaction History:")
            for item in accounts[user]["history"]:
                print(" -", item)

        # EXIT
        elif choice == "5":
            print("👋 Logging out...")
            time.sleep(1)
            break

        else:
            print("❌ Invalid choice")


# MAIN PROGRAM
while True:
    user = login()
    if user:
        atm_menu(user)

    again = input("\nTry again? (y/n): ")
    if again.lower() != "y":
        print("🏦 Thank you for using ATM")
        break
    