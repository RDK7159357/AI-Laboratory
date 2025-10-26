import random

ROWS, COLS = 6, 7

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(b):
    for row in b:
        print('|'.join(row))
    print('-' * 13)

def drop(b, col, p):
    for r in range(ROWS-1, -1, -1):
        if b[r][col] == ' ':
            b[r][col] = p
            return r
    return -1

def check_win(b, p):
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(b[r][c+i] == p for i in range(4)):
                return True
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(b[r+i][c] == p for i in range(4)):
                return True
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(b[r+i][c+i] == p for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if all(b[r-i][c+i] == p for i in range(4)):
                return True
    return False

def bot_move(b, p):
    for c in range(COLS):
        if b[0][c] == ' ':
            r = drop(b, c, p)
            if r >= 0 and check_win(b, p):
                return c
            if r >= 0:
                b[r][c] = ' '
    
    valid = [c for c in range(COLS) if b[0][c] == ' ']
    return random.choice(valid) if valid else -1

board = create_board()
print("Connect Four: Bot R vs Bot Y")
player = 'R'

while True:
    col = bot_move(board, player)
    if col == -1:
        print("Draw!")
        break
    
    drop(board, col, player)
    print(f"Player {player} drops in column {col}")
    print_board(board)
    
    if check_win(board, player):
        print(f"Player {player} wins!")
        break
    
    player = 'Y' if player == 'R' else 'R'
