from typing import List

def nQueen(n: int) -> List[List[str]]:
    col = set()
    pos_diag = set()
    neg_diag = set()

    result= []
    board = [["."]*n for _ in range(n)]

    def backtrack(r):
        if r == n:
            #Create a copy of the board to add to resultults
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for c in range(n):
            if c in col or (r-c) in neg_diag or (r+c) in pos_diag:
                continue

            col.add(c)
            neg_diag.add(r-c)
            pos_diag.add(r+c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            neg_diag.remove(r-c)
            pos_diag.remove(r+c)
            board[r][c] = "."

    backtrack(0)
    return result
    
if __name__ == "__main__":
    n = 4  # Change this value to test different board sizes
    resultults = nQueen(n)

    print(f"All solutions for {n}-Queens:")
    for i, board in enumerate(resultults, 1):
        print(f"Solution {i}:")
        for row in board:
            print(row)
        print()