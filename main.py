import numpy as np

from src import utils, sudoku

def main():
    sample = np.array([[0, 5, 8, 0, 6, 2, 1, 0, 0],
                       [0, 0, 2, 7, 0, 0, 4, 0, 0],
                       [0, 6, 7, 9, 0, 1, 2, 5, 0],
                       [0, 8, 6, 3, 4, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 7, 6, 8, 9, 0],
                       [0, 2, 9, 6, 0, 8, 7, 4, 0],
                       [0, 0, 3, 0, 0, 4, 9, 0, 0],
                       [0, 0, 5, 2, 9, 0, 3, 8, 0]])

    test = sudoku.sudoku(sample)
    print(test.get_random_value())

    ###Backtracking search
    start_sudoku = sudoku.sudoku(sample)
    solved_sudoku, state = start_sudoku.backTrack_search()
    if state == True:
        print("Sudoku solved by backtracking search:")
        print(solved_sudoku)


if __name__ == '__main__':
    main()