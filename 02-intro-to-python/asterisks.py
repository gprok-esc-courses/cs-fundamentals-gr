
n = int(input("Give n: "))

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()