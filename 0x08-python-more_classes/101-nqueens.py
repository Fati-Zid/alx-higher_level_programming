#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # ... (unchanged)

def solve_nqueens(board, row, N, solutions):
    # ... (unchanged)

def print_solutions(N):
    # ... (unchanged)

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
#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # ... (unchanged)

def solve_nqueens(board, row, N, solutions):
    # ... (unchanged)

def print_solutions(N):
    # ... (unchanged)

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
