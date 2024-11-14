# Display a tree of n asterisks
# For example: 
# if n is 5
# display:
#   *
#  ***
# *****
#   #

n = int(input("Give n: "))

spaces = n // 2
asterisks = 1

while asterisks <= n:
    # print spaces
    print(' ' * spaces, end='')
    # print asterisks
    print('*' * asterisks)
    # decrease spaces by 1
    # spaces = spaces - 1
    spaces -= 1
    # increase asterisks by 2
    # asterisks = asterisks + 2
    asterisks += 2