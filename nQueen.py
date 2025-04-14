from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    col = set()
    neg_diag = set()  # r - c
    pos_diag = set()  # r + c
    res = []
    board = [["."] * n for _ in range(n)]
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r - c) in neg_diag or (r + c) in pos_diag:
                continue
            col.add(c)
            neg_diag.add(r - c)
            pos_diag.add(r + c)
            board[r][c] = "Q"
            backtrack(r + 1)
            col.remove(c)
            neg_diag.remove(r - c)
            pos_diag.remove(r + c)
            board[r][c] = "."
    
    backtrack(0)
    return res

if __name__ == "__main__":
    n = 4  # Change this value to test different board sizes
    results = solve_n_queens(n)
    
    print(f"All solutions for {n}-Queens:")
    for i, board in enumerate(results, 1):
        print(f"Solution {i}:")
        for row in board:
            print(row)
        print()