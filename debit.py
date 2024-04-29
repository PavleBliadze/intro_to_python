from user import users
def add_amount(IBAN, amount):
    if IBAN in users and amount.isdigit():
        amount = float(amount)
        users[IBAN]['balance'] += amount
        print(f"Balance filled with {amount} GEL.")
    else:
        print("Invalid account number or amount!")
