# Sudoku Solver

## Overview
This project is a Python-based Sudoku solver that utilizes constraint satisfaction techniques to solve Sudoku puzzles efficiently. It incorporates domain filtering, backtracking search, and heuristic strategies to optimize the solving process.

## Features
- **Constraint Checking**: Ensures Sudoku rules are followed for rows, columns, and squares.
- **Domain Filtering**: Prepares and maintains possible values for each cell.
- **Backtracking Search**: Implements a recursive search algorithm with optional forward-checking and heuristics.
- **Heuristic Approaches**:
  - Most Constrained Variable (MRV) for selecting the next cell.
  - Least Constraining Value (LCV) for selecting cell values.
- **State Management**: Stores and restores intermediate states to optimize the search process.
- **Randomized Search**: Allows for non-deterministic solving for different solution paths.

## Requirements
- Python 3.x
- NumPy

Install dependencies with:
```sh
pip install numpy
```

## Usage
### Initializing the Solver
```python
import numpy as np
from sudoku_solver import sudoku

# Define a Sudoku puzzle (0 represents empty cells)
puzzle = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

solver = sudoku(puzzle)
solved_puzzle, nodes_expanded, success = solver.backTrack_search(forward_checking=True, heuristic=True)

if success:
    print("Sudoku Solved:")
    print(solved_puzzle)
else:
    print("No solution found.")
```

## How It Works
1. **Domain Preparation**: Each empty cell is assigned possible values (1-9).
2. **Constraint Checking**: Ensures row, column, and square validity.
3. **Backtracking Search**: Uses a recursive approach to explore valid assignments.
4. **Heuristics (Optional)**:
   - MRV selects the most constrained cell first.
   - LCV chooses values that restrict future possibilities the least.
5. **Solution Output**: Returns the solved Sudoku grid if a solution is found.

## Contributing
Feel free to contribute improvements or optimizations. Fork the repository, make changes, and submit a pull request.

## License
This project is open-source and available under the MIT License.

