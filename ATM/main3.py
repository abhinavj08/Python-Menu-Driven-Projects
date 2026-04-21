import time
import json
import os

FILE = "bank_data.json"


# ---------------- LOAD / SAVE DATA ----------------
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {
        "Abhinav": {"pin": "1234", "balance": 5000, "history": []},
        "Alex": {"pin": "1111", "balance": 3000, "history": []}
    }


def save_data():
    with open(FILE, "w") as f:
        json.dump(accounts, f, indent=4)


accounts = load_data()


# ---------------- UTIL ----------------
def add_history(user, msg):
    accounts[user]["history"].append(msg)
    save_data()


# ---------------- LOGIN ----------------
def login():
    print("\n🏦 Welcome to Advanced ATM")

    user = input("Enter username: ")

    if user not in accounts:
        print("❌ User not found")
        return None

    attempts = 3
    while attempts > 0:
        pin = input("Enter PIN: ")

        if pin == accounts[user]["pin"]:
            print("✅ Login Successful\n")
            return user
        else:
            attempts -= 1
            print(f"❌ Wrong PIN. Attempts left: {attempts}")

    print("🔒 Account locked (too many attempts)")
    return None


# ---------------- CREATE ACCOUNT ----------------
def create_account():
    print("\n🆕 Create New Account")

    name = input("Enter username: ")

    if name in accounts:
        print("❌ Account already exists")
        return

    pin = input("Set 4-digit PIN: ")
    accounts[name] = {"pin": pin, "balance": 0, "history": []}
    save_data()

    print("✅ Account created successfully")


# ---------------- ATM MENU ----------------
def atm_menu(user):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter choice: ")

        # BALANCE
        if choice == "1":
            print(f"💰 Balance: {accounts[user]['balance']}")
            add_history(user, "Checked balance")

        # DEPOSIT
        elif choice == "2":
            amount = float(input("Enter amount: "))
            if amount > 0:
                accounts[user]["balance"] += amount
                add_history(user, f"Deposited {amount}")
                save_data()
                print("✅ Deposited")

        # WITHDRAW
        elif choice == "3":
            amount = float(input("Enter amount: "))
            if amount <= accounts[user]["balance"]:
                accounts[user]["balance"] -= amount
                add_history(user, f"Withdrew {amount}")
                save_data()
                print("✅ Withdraw successful")
            else:
                print("❌ Insufficient balance")

        # TRANSFER
        elif choice == "4":
            to_user = input("Transfer to: ")

            if to_user not in accounts:
                print("❌ User not found")
                continue

            amount = float(input("Amount: "))

            if amount <= accounts[user]["balance"]:
                accounts[user]["balance"] -= amount
                accounts[to_user]["balance"] += amount

                add_history(user, f"Sent {amount} to {to_user}")
                add_history(to_user, f"Received {amount} from {user}")

                save_data()
                print("✅ Transfer successful")
            else:
                print("❌ Insufficient balance")

        # HISTORY
        elif choice == "5":
            print("\n📊 History:")
            for h in accounts[user]["history"]:
                print(" -", h)

        # EXIT
        elif choice == "6":
            print("👋 Logging out...")
            time.sleep(1)
            break

        else:
            print("❌ Invalid choice")


# ---------------- MAIN PROGRAM ----------------
while True:
    print("\n1. Login")
    print("2. Create Account")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user = login()
        if user:
            atm_menu(user)

    elif choice == "2":
        create_account()

    elif choice == "3":
        print("🏦 Thank you for using ATM")
        break

    else:
        print("❌ Invalid choice")