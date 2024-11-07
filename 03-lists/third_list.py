import random

size = int(input("Give size: "))

data = []

for i in range(size):
    data.append(random.randint(1, 100))


for i in range(size):
    print(data[i], end=' ')

print()

v = int(input("Search: "))
found = False
for i in range(len(data)):
    if v == data[i]:
        print("FOUND")
        found = True
        break
if not found:
    print("NOT FOUND")

if v in data:
    print("FOUND")
else:
    print("NOT FOUND")


total = 0
for i in range(len(data)):
    # total = total + data[i]
    total += data[i]

print("Total: ", total)
print("Average: ", total/len(data))