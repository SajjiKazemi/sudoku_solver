import numpy as np
import time

from src import utils, sudoku

def main():
    easy = np.array([[0, 5, 8, 0, 6, 2, 1, 0, 0],
                       [0, 0, 2, 7, 0, 0, 4, 0, 0],
                       [0, 6, 7, 9, 0, 1, 2, 5, 0],
                       [0, 8, 6, 3, 4, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 7, 6, 8, 9, 0],
                       [0, 2, 9, 6, 0, 8, 7, 4, 0],
                       [0, 0, 3, 0, 0, 4, 9, 0, 0],
                       [0, 0, 5, 2, 9, 0, 3, 8, 0]])
    
    medium = np.array([[8, 3, 0, 6, 0, 0, 0, 0, 7],
                       [0, 0, 7, 0, 2, 0, 0, 5, 0],
                       [0, 2, 1, 0, 0, 9, 0, 8, 0],
                       [6, 0, 0, 0, 8, 0, 0, 0, 9],
                       [0, 0, 0, 4, 6, 5, 0, 0, 0],
                       [3, 0, 0, 0, 9, 0, 0, 0, 2],
                       [0, 8, 0, 2, 0, 0, 3, 9, 0],
                       [0, 5, 0, 0, 4, 0, 2, 0, 0],
                       [2, 0, 0, 0, 0, 8, 0, 1, 6]])
    
    hard = np.array([[1, 0, 0, 0, 3, 0, 0, 0, 0],
                       [0, 6, 2, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 7, 0, 2, 8, 0, 4],
                       [0, 7, 0, 1, 4, 0, 0, 0, 2],
                       [0, 4, 0, 0, 0, 0, 0, 9, 0],
                       [8, 0, 0, 0, 5, 6, 0, 7, 0],
                       [6, 0, 9, 8, 0, 7, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 2, 1, 0],
                       [0, 0, 0, 0, 6, 0, 0, 0, 9]])
    
    evil = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 6],
                       [9, 0, 0, 2, 0, 0, 0, 0, 0],
                       [7, 3, 2, 0, 4, 0, 0, 1, 0],
                       [0, 4, 8, 3, 0, 0, 0, 0, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [3, 0, 0, 0, 0, 4, 6, 7, 0],
                       [0, 9, 0, 0, 3, 0, 5, 6, 8],
                       [0, 0, 0, 0, 0, 2, 0, 0, 1],
                       [6, 0, 0, 0, 0, 0, 0, 3, 0]])

    

    ###Backtracking search
    t0 = time.time()

    start_sudoku = sudoku.sudoku(evil)
    solved_sudoku, exp_nodes , state = start_sudoku.backTrack_search(forward_checking=False, heuristic=False)
    if state == True:
        print("Sudoku solved by backtracking search:")
        print(solved_sudoku)
        print("Number of nodes expanded: ", exp_nodes)
    t1 = time.time()
    print("Time elapsed: ", t1-t0)
if __name__ == '__main__':
    main()