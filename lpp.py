import numpy as np
from typing import Tuple, Dict

def simplex_method(tableau: np.ndarray) -> Tuple[float, Dict[str, float]]:
    num_rows, num_cols = tableau.shape
    num_constraints = num_rows - 1  # Exclude the objective row
    num_decision_vars = num_cols - num_constraints - 2  # Exclude slack vars and RHS
    
    # Step 1: Check if the tableau is optimal (all coefficients in the objective row ≤ 0)
    while np.any(tableau[-1, :-1] > 0):
        # Step 2: Select the entering variable (most positive coefficient in the objective row)
        entering_col = np.argmax(tableau[-1, :-1])
        
        # Step 3: Select the leaving variable (minimum ratio test)
        ratios = []
        for i in range(num_constraints):
            if tableau[i, entering_col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, entering_col])
            else:
                ratios.append(np.inf)
        leaving_row = np.argmin(ratios)
        
        # If all ratios are infinite, the problem is unbounded
        if np.isinf(ratios[leaving_row]):
            raise ValueError("Problem is unbounded (no optimal solution).")
        
        # Step 4: Pivot on the selected element
        pivot = tableau[leaving_row, entering_col]
        tableau[leaving_row, :] /= pivot
        
        for i in range(num_rows):
            if i != leaving_row:
                tableau[i, :] -= tableau[i, entering_col] * tableau[leaving_row, :]
    
    # Extract the optimal solution
    optimal_value = tableau[-1, -1]
    
    # Determine which variables are basic (non-zero in the solution)
    solution = {}
    for col in range(num_decision_vars):
        column = tableau[:-1, col]
        if np.sum(column == 1) == 1 and np.sum(column != 0) == 1:
            row = np.where(column == 1)[0][0]
            solution[f'x{col + 1}'] = tableau[row, -1]
        else:
            solution[f'x{col + 1}'] = 0.0
    
    return optimal_value, solution

if __name__ == "__main__":
    tableau = np.array([
    [1,  1, 1, 0, 4],
    [1, -1, 0, 1, 2],
    [-3, -2, 0, 0, 0]
    ])

    optimal_value, solution = simplex_method(tableau)
    print("Optimal value:", optimal_value)  # Expected: 8.0
    print("Solution:", solution)            # Expected: {'x1': 3.0, 'x2': 1.0}