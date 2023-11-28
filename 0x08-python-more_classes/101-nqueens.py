#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at position (row, col) on the board."""
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    """Recursively solve the N-Queens problem."""
    if row == N:
        solution = [[r, c] for r, c in enumerate(board)]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)

def print_solutions(N):
    """Print all solutions for the N-Queens problem."""
    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    N = int(sys.argv[1])

    # Check if N is greater or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(N)
