# Open CSV file
file = open('accounts.csv', 'r')
# Read every line
lines = file.readlines()

accounts = {}

# Split data of the line and create a dictionary
for line in lines:
    parts = line.strip().split(',')
    if parts[0] != 'id':
        account = {'id': parts[0], 'pin': parts[1], 
                'name': parts[2], 'balance': float(parts[3])}
        accounts[parts[0]] = account

print(accounts)