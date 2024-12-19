
def read_accounts():
    file = open('accounts.csv', 'r')
    lines = file.readlines()
    accounts = {}
    for line in lines:
        parts = line.strip().split(',')
        if parts[0] != 'id':
            account = {'id': parts[0], 'pin': parts[1], 
                    'name': parts[2], 'balance': float(parts[3])}
            accounts[parts[0]] = account
    return accounts


def login():
    id = input("ID: ")
    pin = input("Pin: ")
    return id, pin


def check_login(id, pin, accounts):
    if id in accounts:
        account = accounts[id]
        if account['pin'] == pin:
            return account 
    return None


def atm_menu():
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("0. EXIT")
    ch = int(input("Choose: "))
    return ch 


def deposit(account):
    amount = float(input("Amount: "))
    if amount > 0:
        account['balance'] += amount
    else:
        print("Invalid amount")


def withdraw(account):
    amount = float(input("Amount: "))
    if amount > 0 and amount <= account['balance']:
        account['balance'] -= amount 
    else:
        print("Invalid amount")


def save(accounts):
    file = open('accounts.csv', 'w')
    file.write('id,pin,name,balance\n')
    for key in accounts:
        a = accounts[key]
        file.write(a['id'] + ',' + a['pin'] + ',' + a['name'] + ',' +
                   str(a['balance']) + '\n')

# Load accounts
accounts = read_accounts()

pin = ""
id = ""
# Loop until admin gives 0000 id and 0000 pin
while pin != '0000' and id != '0000':

    # Display login prompt (user gives id and pin)
    id, pin = login()
    account = check_login(id, pin, accounts)
    # If login ok
    if account is not None:
        print("Welcome,", account['name'])
        # Loop until user selects 0 (EXIT)
        choice = -1
        while choice != 0:
            # Display ATM menu and get user's choice
            choice = atm_menu()
            # Serve user's choice
            match choice:
                case 1:
                    print("Balance", account['balance']) 
                case 2:
                    deposit(account)
                case 3: 
                    withdraw(account)  
                case 0:
                    # If user choice 0: Save account to file
                    save(accounts)
                    print("BYE ...")  
                case _: 
                    print("Wrong choice")
            