def initialize_chessboard():
    return [[0 for _ in range(8)] for _ in range(8)]

def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]
    for i in range(8):
        if board[i][col] == 1 or board[row][i] == 1:
            return False

        for j in range(8):
            if board[i][j] == 1 and (abs(row - i) == abs(col - j)):
                return False

    return True

def solve_queens():
    chessboard = initialize_chessboard()
    solutions = []
    row = 0
    col = 0

    while row >= 0:
        if row == 8:
            # All queens have been placed successfully
            solutions.append([list(row) for row in chessboard])
            row -= 1
            col = chessboard[row].index(1)
            chessboard[row][col] = 0
            col += 1
        elif col == 8:
            # All columns in the current row have been tried
            row -= 1
            if row >= 0:
                col = chessboard[row].index(1)
                chessboard[row][col] = 0
                col += 1
        elif is_safe(chessboard, row, col):
            chessboard[row][col] = 1
            row += 1
            col = 0
        else:
            col += 1

    return solutions

def display_solutions(solutions):
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(' '.join(['Q' if cell else '.' for cell in row]))
        print()

def main():
    solutions = solve_queens()
    display_solutions(solutions)

if __name__ == "__main__":
    main()
