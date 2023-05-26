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
    test.backTrack_search()
    print(test.table)


if __name__ == '__main__':
    main()