def show_balance(balance):
    balance = float(balance)
    print("Current Balance $ " + str(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    current_balance = balance + float(amount)
    return str(current_balance)

def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    current_balance = float(balance) - float(amount)
    return str(current_balance)

def logout(name):
    print("Goodbye", name)