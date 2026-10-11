#ATM SIMULATION 

notes = (500, 200, 100, 50)
note_count = [20, 30, 50 ,100]

# Account Number
accounts = { 
    1001: {"name": "Sahejveer", "pin": 1232, "balance": 74000, "history":[] },
    1002: {"name": "Priyanshu", "pin": 1980, "balance": 50000, "history":[] },
}

def get_amount():
    while True: 
        amount = input("Enter the amount you want to withdraw:")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a valid amount greater than 0.")

def add_history(account, text, amount):
    entry = (text, amount, account["balance"])
    account["history"].append(entry)

def give_notes(amount):
    to_give = [0,0,0,0]
    left = amount
    for i in range(len(notes)):
        how_many = left // notes[i]
        if how_many > note_count[i]:
            how_many = note_count[i]
        to_give[i] = how_many
        left = left - how_many * notes[i]

    if left !=0:
        return None

    for i in range(len(notes)):
        note_count[i] = note_count[i] - to_give[i]
    return to_give

def login():
    account_number=input("Enter your account number: ")
    if not account_number.isdigit() or int(account_number) not in accounts:
        print("Account number not found. ")
        return 0
    account_number = int(account_number)

    tries = 3
    while tries > 0:
        pin = input("Enter your PIN: ")
        if pin.isdigit() and int(pin) == accounts[account_number]["pin"]:
            print("\nWELCOME", accounts[account_number]["name"])
            return account_number
        tries = tries - 1
        print("WRONG PIN!", tries, "tries left")

    print("Too many wrong attempts. Card blocked. Please contact your bank.")
    return 0

def check_balance(account):
    print("Your Balance is ₹", account["balance"])

def deposit(account):
    amount = get_amount()
    account["balance"] = account["balance"] + amount
    add_history(account, "Deposit", amount)
    print("Deposit done. New balance is ₹", account["balance"])

def withdraw(account):
    amount = get_amount()

    if amount > account["balance"]:
        print("Insufficient balance. Your balance is ₹", account["balance"])
    elif amount % 50 !=0:
        print("Please enter an amount in multiples of 50")
    else:
        result = give_notes(amount)
        if result == None:
            print("ATM does not have sufficient notes to dispense this amount. Please try a different amount.")
        else:
            account["balance"] = account["balance"] - amount
            add_history(account, "Withdraw", amount)
            print("Please collect your cash:")
            for i in range(len(notes)):
                if result[i] > 0:
                    print(result[i], "notes of ₹", notes[i])
            print(" Remaining balance is ₹", account["balance"])

def mini_statement(account):
    print("\n--- LAST 5 TRANSACTIONS ---")
    if len(account["history"]) == 0:
        print("No transactions yet:")
    for entry in account["history"][-5:]:
        print(entry[0], "₹", entry[1], "Balance after transaction: ₹", entry[2])

def main():
    print("=== WELCOME TO PY-BANK ATM ===")
    account_number = login()
    if account_number == 0:
        return
    account = accounts[account_number]

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw")
        print("4. Mini Statement\n0. Exit")
        choice = input("Enter your choice: ")
 
        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            mini_statement(account)
        elif choice == "0":
            print("Thank you! Visit again.")
            break
        else:
            print("Wrong choice, try again")
 
 
main()
