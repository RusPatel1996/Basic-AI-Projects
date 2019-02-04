inf = 999999
negInf = -999999
import os

class GameBoard():
    def __init__(self):
        self.board = [[' ' for i in range(0,7)] for j in range (0,6)]
        self.position = []
    
    def show_board(self):
        os.system(['clear','cls'][os.name == 'nt'])
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print(self.board[3])
        print(self.board[4])
        print(self.board[5])
        print("-----------------------------------")
        print("| 0 || 1 || 2 || 3 || 4 || 5 || 6 |")
        
    def moves_left(self):
        for row in range(0,6):
            for col in range(0,7):
                if self.board[row][col] is ' ':
                    return True
        return False
        
    def is_horizontal(self):
        x_count = 0
        o_count = 0
        row = self.position[0]
        for i in range(0,7):
            if self.board[row][i] == 'X':
                o_count = 0
                x_count += 1
            elif self.board[row][i] == 'O':
                x_count = 0
                o_count += 1                
            else:
                x_count = 0
                o_count = 0
            if x_count == 4 or o_count == 4:
                return True
        return False
        
    def is_vertical(self):
        x_count = 0
        o_count = 0
        col = self.position[1]
        for i in range(5,-1,-1):
            if self.board[i][col] == 'X':
                o_count = 0
                x_count += 1
            elif self.board[i][col] == 'O':
                x_count = 0
                o_count += 1
            else:
                x_count = 0
                o_count = 0
            if x_count == 4 or o_count == 4:
                return True
        return False
            
    def is_LR_diagonal(self):
        x_count = 0
        o_count = 0
        row = self.position[0]
        col = self.position[1]
        while row != 5 and col != 0:
            row += 1
            col -= 1
        while row != -1 and col != 7:            
            if self.board[row][col] == 'X':
                o_count = 0
                x_count += 1
            elif self.board[row][col] == 'O':
                x_count = 0
                o_count += 1
            else:
                x_count = 0
                o_count = 0
            if x_count == 4 or o_count == 4:
                return True
            row -= 1
            col += 1
        return False        
        
    def is_RL_diagonal(self):
        x_count = 0
        o_count = 0
        row = self.position[0]
        col = self.position[1]
        while row != 0 and col != 0:
            row -= 1
            col -= 1
        while row != 6 and col != 7:            
            if self.board[row][col] == 'X':
                o_count = 0
                x_count += 1
            elif self.board[row][col] == 'O':
                x_count = 0
                o_count += 1                
            else:
                x_count = 0
                o_count = 0
            if x_count == 4 or o_count == 4:
                return True
            row += 1
            col += 1
        return False
    
    def is_goal(self):
        if (self.is_horizontal() is True or self.is_vertical() is True or
            self.is_LR_diagonal() is True or self.is_RL_diagonal() is True):
            return True
        else:
            return False
    
    def insert(self, char, col):        
        for i in range(5,-1,-1):
            if self.board[i][col] is ' ':
                self.board[i][col] = char
                self.position = [i, col]                
                return True
        return False
    
    def possible_moves(self):
        moves = []
        for col in range(0,7):
            for row in range(5,-1,-1):
                if self.board[row][col] is ' ':
                    moves.append([row,col])
                    break
                else:
                    continue
        return moves    
    
    def check_streak(self, char, streak):
        count = 0
        for row in range(0,6):
            for col in range(0,7):
                if self.board[row][col] == char:
                    count += self.vertical_streak(row, col, streak)
                    count += self.horizontal_streak(row, col, streak)
                    count += self.diagonal_streak(row, col, streak)                
        return count
    
    def vertical_streak(self, row, col, streak):
        consecutiveCount = 0
        for i in range(row, 6):
            if self.board[i][col] == self.board[row][col]:
                consecutiveCount += 1
            else:
                break    
        if consecutiveCount >= streak:
            return 1
        else:
            return 0
        
    def horizontal_streak(self, row, col, streak):
        consecutiveCount = 0
        for j in range(col, 7):
            if self.board[row][j] == self.board[row][col]:
                consecutiveCount += 1
            else:
                break
        if consecutiveCount >= streak:
            return 1
        else:
            return 0
    
    def diagonal_streak(self, row, col, streak):
        total = 0
        consecutiveCount = 0
        j = col
        for i in range(row, 6):
            if j > 6:
                break
            elif self.board[i][j] == self.board[row][col]:
                consecutiveCount += 1
            else:
                break
            j += 1            
        if consecutiveCount >= streak:
            total += 1
        consecutiveCount = 0
        j = col
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif self.board[i][j] == self.board[row][col]:
                consecutiveCount += 1
            else:
                break
            j += 1
        if consecutiveCount >= streak:
            total += 1
        return total
    
    def minimax(self, depth, is_human, alpha, beta):
        score = 0
        if is_human is True:
            if self.is_goal() is True:
                return 10000-depth
            score -= 100*self.check_streak('X', 3)
            score -= 2*self.check_streak('X', 2)            
        if is_human is False:
            if self.is_goal() is True:
                return -10000-depth   
            score += 100*self.check_streak('O', 3)
            score += 2*self.check_streak('O', 2)                     
        if self.moves_left() is False:
            return score-depth
        if depth == 5:
            return score-depth

        moves = self.possible_moves()
        
        if is_human is True:
            v = inf
            for i in moves:
                row = i[0]
                col = i[1]
                if self.board[row][col] is ' ':                
                    self.board[row][col] = 'X'
                    v = min(v, self.minimax(depth+1, False, alpha, beta))
                    self.board[row][col] = ' '
                    if v <= alpha: return v
                    beta = min(beta, v)
        else:
            v = negInf
            for i in moves:
                row = i[0]
                col = i[1]
                if self.board[row][col] is ' ': 
                    self.board[row][col] = 'O'
                    v = max(v, self.minimax(depth+1, True, alpha, beta))
                    self.board[row][col] = ' ' 
                    if v >= beta: return v
                    alpha = max(alpha, v)
                    
        return score+v
            
    def best_move(self):
        bestMove = []
        bestVal = -1000        
        moves = self.possible_moves()        
        for i in moves:
            row = i[0]
            col = i[1]
            if self.board[row][col] is ' ':
                self.board[row][col] = 'O'
                tempVal = self.minimax(1, True, negInf, inf)
                if tempVal > bestVal:
                    bestMove = i
                    bestVal = tempVal
                self.board[row][col] = ' '
        return bestMove
        
class Player():
    def __init__(self):
        self.human = 'X'
        self.computer = 'O'
        self.turn = True
    
    def is_human(self):
        return self.turn
    
    def switch(self):
        if self.turn is True: 
            self.turn = False
        else:
            self.turn = True
    
    def character(self):        
        if self.turn is True:
            return self.human
        else:
            return self.computer
        
def main():    
    print("--Welcome to Connect-Four!--")    
    connect4 = GameBoard()
    player = Player()
    
    connect4.show_board()
    
    while connect4.moves_left() is True:
        if player.is_human() is True:
            print('\n')
            col = int(input("Choose a column to input character (0-6): "))
            if connect4.insert(player.character(), col) is False:
                print("Column Full! It is ", player.character(), "'s Turn!")
                continue
            print('\n')
            connect4.show_board()
            if connect4.is_goal() is True:
                print("\n==You Win!!==\n")
                return
            player.switch()
        else:
            print("\nComputer is thinking...\n")
            move = connect4.best_move()
            print("Computer Move - Column: ", move)
            connect4.insert(player.character(), move[1])
            connect4.show_board()
            if connect4.is_goal() is True:
                print("\n--You Lose!!--\n")
                return
            player.switch()
    print("--It's a Tie!!--\n")
    return

again = "y"
while again is "y":
    main()
    again = str(input("Play again? (y/n)"))
print("Goodbye!")
    
