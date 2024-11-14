
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
print(board)

board = []
for row in range(3):
    r = []
    for col in range(3):
        r.append('-')
    board.append(r)
print(board)

board = [['-'] * 3 for i in range(3)]
board[1][0] = 'X'
print(board)