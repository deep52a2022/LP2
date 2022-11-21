
    
def issafe( board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1),  range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, n, 1),  range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True


def solve( board, col, n):
    if col >= n:
        return True
    # decide which row , n => no of rows
    for i in range(n):
        if issafe(board, i, col):
            board[i][col] = 1
            if solve(board, col + 1, n) == True:
                return True
            board[i][col] = 0
    return False
    
    
    
def nQueen( n): 
    board = [[0 for x in range(n)] for x in range(n)] 
    solve(board, 0, n)
    for i in board:
        print(i)

if __name__ == "__main__":
    n = 6
    nQueen(n)
