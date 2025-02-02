def is_safe(board, row, col):
    
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
        
    return True

def solve_8_queens(board, row):
    if row >= 8:
        return True
    
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1 
            if solve_8_queens(board, row + 1):
                return True
            board[row][col] = 0
        
    return False

def print_solution(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print("\n")
 
def solve():
    board = [[0] * 8 for _ in range(8)]
    if solve_8_queens(board, 0):
        print_solution(board)
    else:
        print("No solution exists.")
    
solve()



































# Sample Output
# 1 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 1
# 0 0 0 0 0 1 0 0
# 0 0 1 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 1 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0