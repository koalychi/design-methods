class Board:
    def __init__(self, size):
        self.board = [[0 for _ in range(size)] for _ in range(size)]
    
    def place_queen(self, row, col):
        self.board[row][col] = 1
    
    def remove_queen(self, row, col):
        self.board[row][col] = 0
    
    def is_safe_position(self, row, col):
        # Check the column for another queen
        for i in range(len(self.board)):
            if self.board[i][col] == 1:
                return False
        
        # Check the row for another queen
        for j in range(len(self.board[row])):
            if self.board[row][j] == 1:
                return False
        
        # Check the diagonals for another queen
        # Diagonal 1 (top left to bottom right)
        for i, j in zip(range(row, len(self.board)), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        
        # Diagonal 2 (top right to bottom left)
        for i, j in zip(range(row, len(self.board)), range(col, len(self.board[row]))):
            if self.board[i][j] == 1:
                return False
        
        # Diagonal 3 (bottom left to top right)
        for i, j in zip(range(row, -1, -1), range(col, len(self.board[row]))):
            if self.board[i][j] == 1:
                return False
        
        # Diagonal 4 (bottom right to top left)
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        
        return True
   

class Queen:
    def __init__(self, position):
        self.position = position

class Solution:
    def __init__(self, size):
        self.board = Board(size)
        self.queens = []
    
    def add_queen(self, queen):
        row, col = queen.position
        if self.board.is_safe_position(row, col):
            self.board.place_queen(row, col)
            self.queens.append(queen)
            return True
        return False
    
    def remove_queen(self):
        if self.queens:
            last_queen = self.queens.pop()
            row, col = last_queen.position
            self.board.remove_queen(row, col)
    
    def is_complete(self):
        return len(self.queens) == 8
    
    def find_solutions(self, col=0):
        if col >= 8:
            if self.is_complete():
                # Print or store the solution
                print(self.board.board)
            return
        for row in range(8):
            queen = Queen((row, col))
            if self.add_queen(queen):
                self.find_solutions(col + 1)
                self.remove_queen()  # Backtrack

# Usage
solution = Solution(8)
solution.find_solutions()