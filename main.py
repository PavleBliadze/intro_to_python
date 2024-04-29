from user import add_user
from debit import add_amount
from credit import transfer
while True:
    menu = ["1. Add user", "2. Add amount", "3. Transfer money", "4. Exit"]
    for i in menu:
        print(i)
    chosen = int(input("Enter number: ")) 
    if chosen == 1:
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        IBAN = input("Enter IBAN: ")
        add_user(name, surname, IBAN)
        print("User added successfully")
    elif chosen == 2:
        IBAN = input("Enter IBAN: ")
        amount = input("Enter amount: ")
        add_amount(IBAN, amount)
    elif chosen == 3:
        sender_IBAN = input("Enter your IBAN: ")
        receiver_IBAN = input("Enter receiver IBAN: ")
        amount = input("Enter amount: ")
        transfer(sender_IBAN, receiver_IBAN, amount)
    elif chosen == 4:
        break
    else:
        print("Invalid input!")