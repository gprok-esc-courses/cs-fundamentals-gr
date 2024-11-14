
n = int(input("Give n: "))

spaces = n // 2
asterisks = 1

while asterisks <= n:
    # print spaces
    for i in range(spaces):
        print(' ', end=' ')
    # print asterisks
    for i in range(asterisks):
        print('*', end=' ')
    # go to the next line
    print()
    # decrease spaces by 1
    # spaces = spaces - 1
    spaces -= 1
    # increase asterisks by 2
    # asterisks = asterisks + 2
    asterisks += 2

for i in range(n // 2):
    print(' ', end=' ')
print('#')