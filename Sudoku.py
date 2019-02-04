board = [
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

def showBoard(board):
    alphabetize = 'A'
    print(' ', end=' ')
    for i in range (1,10):
        print(i, end=' ')
    print('')    
    for i in range (0,9):
        print(alphabetize, end= '|')
        for j in range (0,9):
            print(board[i][j], end='|')
        print('')
        alphabetize = chr(ord(alphabetize)+1)

def checkRow(board, i, x):
    for j in range(0,9):
        if(board[i][j] == x):
            return True
    return False

def checkColumn(board, j, x):
    for i in range(0,9):
        if(board[i][j] == x):
            return True
    return False

def checkBox(board, i, j, x):
    for row in range(0,3):
        for col in range(0,3):
            if(board[i+row][j+col] == x):
                return True
    return False        

def checkConstraints(board, i, j, x):
    return (not checkRow(board, i, x)
            and not checkColumn(board, j, x) 
            and not checkBox(board, (i-(i%3)), (j-(j%3)), x))
        
def findEmptySpace(board, _list):
    for i in range(0,9):
        for j in range(0,9):
            if(board[i][j]==0):
                _list[0]=i
                _list[1]=j
                return True
    return False

def formulateSolution(board):   
    _list = [0,0]       
    if(not findEmptySpace(board,_list)): 
        return True    
    i =_list[0]
    j =_list[1]    
    for x in range(0,9):
        if(checkConstraints(board, i, j, x+1)):
            board[i][j] = x+1
            if(formulateSolution(board)):
                return True
            board[i][j] = 0        
    return False

print("Original Problem")
showBoard(board)
print('\n')
if(formulateSolution(board) == True):
    print("solution: ")
    showBoard(board)
else:
    print("Impossible Sudoku!")
