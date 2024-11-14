
def print_characters(ch, n, e):
    for i in range(n):
        print(ch, end=e)

n = int(input("Give n: "))

spaces = n // 2
asterisks = 1

while asterisks <= n:
    print_characters(' ', spaces, ' ')
    print_characters('*', asterisks, ' ')
    # go to the next line
    print()
    # decrease spaces by 1
    # spaces = spaces - 1
    spaces -= 1
    # increase asterisks by 2
    # asterisks = asterisks + 2
    asterisks += 2

print_characters(' ', n // 2, ' ')
print('#')