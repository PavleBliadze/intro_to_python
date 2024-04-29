from user import users
def transfer(sender_IBAN, receiver_IBAN, amount):
    if amount.isdigit():
        amount = float(amount)
        if sender_IBAN in users:
            if users[sender_IBAN]['balance'] >= amount:
                if receiver_IBAN in users:
                    users[sender_IBAN]['balance'] -= amount
                    users[receiver_IBAN]['balance'] += amount
                    print(f"Transfer successful! {amount} GEL transferred to {users[receiver_IBAN]['name']} {users[receiver_IBAN]['surname']}.")
                else:
                    print("The receiver account number does not exist.")
            else:
                print("Not enough balance.")
        else:
            print("The sender account number does not exist.")
    else:
        print("Amount must be a number!")
        

