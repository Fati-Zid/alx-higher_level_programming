#!/usr/bin/python3
import sys


def print_solutions(board):
    """Print all solutions for the N-Queens problem."""
    for row in board:
        print(row)


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at position (row, col) on the board."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """Recursively solve the N-Queens problem."""
    # Base case: If all queens are placed, add the solution to the list
    if col >= N:
        solution = [row[:] for row in board]  # Create a copy of the board
        solutions.append(solution)
        return

    # Consider this column and try placing the queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen in board[i][col]
            board[i][col] = 1
            # Recur to place the rest of the queens
            solve_nqueens_util(board, col + 1, N, solutions)
            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0


def solve_nqueens(N):
    """Solve the N-Queens problem."""
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print_solutions(solution)
