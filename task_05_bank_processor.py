balance = float(input("Enter the opening balance: "))
daily_limit = 500
withdraw_today = 0
total_deposited = 0
total_withdrawn = 0
transaction_history = []

def transaction_record(type, amount, balance):
    record = {
        "type": type,
        "amount": amount,
        "balance_after": balance
    }

    transaction_history.append(record)

def deposit(balance):
    global total_deposited

    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("Amount must be greater that zero!")
    else:
        balance += amount
        total_deposited += amount
        transaction_record("Deposit", amount, balance)
        print("Deposit successful!")

    return balance

def withdraw(balance):
    global withdraw_today, total_withdrawn

    amount = float(input("Enter withdraw amount: "))

    if amount <= 0:
        print("Amount must be greater that zero!")
    elif amount > balance :
        print("Insufficient Balance!")
    elif amount > daily_limit - withdraw_today:
        print("Daily withdrawal limit exceeded!")
    else:
        balance -= amount
        withdraw_today += amount
        total_withdrawn += amount

        transaction_record("Withdraw", amount, balance)


def check_banalce(balance):
    print(f"\nCurrent Balance: {balance:.2f}")

def summary(balance):
    print("\n------Transaction Summary--------")
    print(f"Final Balance: {balance:.2f}")
    print(f"Total Deposit: {total_deposited:.2f}")
    print(f"Total Withdraw: {total_withdrawn:.2f}")
    print("\n------Transaction History--------")

    if not transaction_history:
        print("NO SUCCESSFUL TRANSACRIONS.")
    else:
        for transaction in transaction_history:
            print(transaction)

while True:
    print("\n--------MENU---------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction summary")
    print("5. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        balance = deposit(balance)
        
    elif choice == 2:
        balance = withdraw(balance)
        
    elif choice == 3:
        check_banalce(balance)
        
    elif choice == 4:
        summary(balance)
        
    elif choice == 5:
        summary(balance)
        print("GOOD BYE")
        break

    else:
        print("Invalid Option. Try again.")
        
