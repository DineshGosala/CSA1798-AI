def print_solution(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(board, col, n):
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            solve_n_queens(board, col + 1, n)
            board[i][col] = '.' 


def main():
    n = int(input("Enter the size of the chessboard: "))

    board = [['.' for _ in range(n)] for _ in range(n)]

    solve_n_queens(board, 0, n)

if __name__ == "__main__":
    main()
