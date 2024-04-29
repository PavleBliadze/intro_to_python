users = {}  
def add_user(name, surname, IBAN):
    if IBAN.startswith("TB") and len(IBAN) == 5 and IBAN[2:].isdigit():
        users[IBAN] = {'name': name, 'surname': surname, 'balance': 0}
    else:
        print("In IBAN, the first two letters should be TB and the other three should be numbers (example: TB012).")