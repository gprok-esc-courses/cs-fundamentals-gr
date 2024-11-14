
# Initialize 2d 3x3 list to be the board
board = [['-'] * 3 for i in range(3)]

# Create a player variable, initially X
player = 'X'

# Loop until ???
while True:
    # Display board
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=' ')
        print()

    # Prompt current user to play row and col
    print(player, "plays")
    r = int(input("Row: "))
    c = int(input("Col: "))

    # If row, col cell is empty
    if board[r][c] == '-':
        # Mark with current player
        board[r][c] = player
        # Change player
        player = 'X' if player == 'O' else 'O'
        # Check for winner
        # if winner stop the loop
        # if not winner, check for Tie
        # if tie stop the loop
    # Else
    else:
        # error message
        print("Error: Invalid poisition")