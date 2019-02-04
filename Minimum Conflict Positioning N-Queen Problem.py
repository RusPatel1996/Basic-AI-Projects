import os
import random

def game_board(n):
    os.system(['clear','cls'][os.name == 'nt'])
    board = [[' ' for col in range(0,n)] for row in range(0,n)]
    return board

def show_board(board, n):
    for row in range(0, n):
        print('|', end='')
        for col in range(0, n):
            print(board[row][col], end='|', flush=True)        
        print('\r')

def randomize(board, n):
    for col in range(0,n):
        board[random.randint(0,n-1)][col] = 'Q'

def clear_col(board, n, col):
    for row in range(0,n):
        board[row][col] = ' '

def conflicts_in_position(board, n, row, col):
    total = 0
    for i in range(0,n):
        if board[i][col] is 'Q':
            total += 1
    for j in range(0,n):
        if board[row][j] is 'Q':
            total += 1
    i = row
    j = col
    while i is not 0 and j is not 0:
        i -= 1
        j -=1
        if board[i][j] is 'Q':
            total += 1
    i = row
    j = col
    while i is not n-1 and j is not n-1:
        i += 1
        j +=1
        if board[i][j] is 'Q':
            total += 1
    i = row
    j = col
    while i is not n-1 and j is not 0:
        i += 1
        j -=1
        if board[i][j] is 'Q':
            total += 1
    i = row
    j = col
    while i is not 0 and j is not n-1:
        i -= 1
        j += 1
        if board[i][j] is 'Q':
            total += 1
    return total

def min_conflict_move(value_board, board, n):
    for col in range(n-1, -1, -1):
        minimum_move = 999
        clear_col(board, n, col)
        for row in range(0,n):
            move_value = conflicts_in_position(board, n, row, col)
            if move_value < minimum_move:
                minimum_move = move_value
                move = row
            value_board[row][col] = move_value
        board[move][col] = 'Q'

n = int(input("N: "))
board = game_board(n)
value_board = game_board(n)
randomize(board, n)
print("------NxN Queen------\n")
print("Random Positions: ")

'''
board[1][0] = 'Q'
board[4][1] = 'Q'
board[6][2] = 'Q'
board[3][3] = 'Q'
board[0][4] = 'Q'
board[2][5] = 'Q'
board[5][6] = 'Q'
board[7][7] = 'Q'
'''

show_board(board, n)
print('\r')
min_conflict_move(value_board, board, n)
print("Conflict values: ")
show_board(value_board, n)
print('\r')
print("Min-Conflict Positions: ")
show_board(board, n)
print('\r')
input("Press Enter to continue...")

