def is_safe(board, row, col):
    for c, r in enumerate(board):
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def solve(col, n, board, solutions):
    if col == n:
        solutions.append(board[:])
        return
    for row in range(1, n + 1):
        if is_safe(board, row, col):
            board.append(row)
            solve(col + 1, n, board, solutions)
            board.pop()

def n_queen(n):
    solutions = []
    solve(0, n, [], solutions)
    return solutions

# Example usage
n = 4  # Set your desired number of queens
solutions = n_queen(n)
if not solutions:
    print("No solution possible")
else:
    for sol in solutions:
        print(sol)
