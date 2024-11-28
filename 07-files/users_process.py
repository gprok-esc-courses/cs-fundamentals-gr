
file = open('users.csv')

lines = file.readlines()

# for line in lines:
#     line = line.strip()
#     data = line.split(',')
#     print(data[2])

for i in range(1, len(lines)):
    line = lines[i].strip()
    data = line.split(',')
    print(data[2])
