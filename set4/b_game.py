import math

board = [' '] * 9

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]}|{board[i+1]}|{board[i+2]}")
        if i < 6: print("-+-+-")

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return 'T' if ' ' not in board else None

def minimax(is_max):
    winner = check_winner()
    if winner == 'X': return -1
    if winner == 'O': return 1
    if winner == 'T': return 0
    
    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def best_move(player):
    best_val = -math.inf if player == 'O' else math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            val = minimax(player == 'X')
            board[i] = ' '
            if (player == 'O' and val > best_val) or (player == 'X' and val < best_val):
                best_val, move = val, i
    return move

print("Tic-Tac-Toe: Bot X vs Bot O")
while not check_winner():
    move = best_move('X')
    board[move] = 'X'
    print_board()
    if check_winner(): break
    
    move = best_move('O')
    board[move] = 'O'
    print_board()

print(f"Winner: {check_winner()}")
