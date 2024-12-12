
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

            # Display ATM menu and get user's choice

            # Serve user's choice

            # If user choice 0: Save account to file