# Dictionary to store account state
account_data = {
    "balance": 0.0,
    "transactions": []
}

def get_balance():
    """Returns the current account balance."""
    return account_data["balance"]

def deposit(amount):
    """Adds money to the balance and records the transaction."""
    if amount <= 0:
        return False, "Deposit amount must be greater than zero."
    
    account_data["balance"] += amount
    account_data["transactions"].append(f"Deposited : + Rs. {amount:.2f}")
    return True, f"Successfully deposited Rs. {amount:.2f}."

def withdraw(amount):
    """Deducts money if sufficient funds exist and records the transaction."""
    if amount <= 0:
        return False, "Withdrawal amount must be greater than zero."
    
    if amount > account_data["balance"]:
        return False, "Insufficient funds! Transaction declined."
    
    account_data["balance"] -= amount
    account_data["transactions"].append(f"Withdrew  : - Rs. {amount:.2f}")
    return True, f"Please collect your cash: Rs. {amount:.2f}."

def get_statement():
    """Returns the list of all transactions."""
    return account_data["transactions"]