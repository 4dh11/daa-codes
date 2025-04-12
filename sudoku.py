def is_valid(grid, r, c, k):
    notin_row = k not in grid[r]
    notin_col = k not in [grid[i][c] for i in range(9)]
    notin_submat = k not in [grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
    return notin_row and notin_col and notin_submat

def solve(grid, r = 0, c = 0):
    if r == 9:
        return True
    elif c == 9:
        return solve(grid, r + 1, 0)
    elif grid[r][c] != 0:
        return solve(grid, r, c+1)
    else:
        for k in range(1,10):
            if is_valid(grid, r, c, k):
                grid[r][c] = k
                if solve(grid, r, c + 1):
                    return True
                grid[r][c] = 0
        return False

if __name__ == "__main__":
    grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
    if solve(grid):
        for row in grid:
            print(row)
    else:
        print("No solution exists")