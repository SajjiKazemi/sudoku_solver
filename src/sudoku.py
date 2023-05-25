import numpy as np

class sudoku():
    def __init__(self, table: np.ndarray):
        self.table = table
        self.ignore_value = 0
        
    def check_row(self, row: int):
        "This function checks if the row is valid in terms of sudoku rules"
        filtered_row = self.table[row][self.table[row] != self.ignore_value]
        unique_elements = np.unique(filtered_row)
        if len(filtered_row) != len(unique_elements):
            return False
        return True

    def check_column(self, column: int):
        "This function checks if the column is valid in terms of sudoku rules"
        filtered_column = self.table[column][self.table[column] != self.ignore_value]
        unique_elements = np.unique(filtered_column)
        if len(filtered_column) != len(unique_elements):
            return False
        return True
        
    def print_sudoku(self):
        print(self.table)

    def det_square(self, row: int, column: int):
        "This function determines the square of the given row and column"
        if row < 3:
            if column < 3:
                return 0
            elif column < 6:
                return 1
            else:
                return 2
        elif row < 6:
            if column < 3:
                return 3
            elif column < 6:
                return 4
            else:
                return 5
        else:
            if column < 3:
                return 6
            elif column < 6:
                return 7
            else:
                return 8
    
    def separate_squares(self):
        "This function separates the sudoku into 9 squares"
        self.squares = []
        for i in range(9):
            self.squares.append(self.table[self.det_square(i, 0):self.det_square(i, 0)+3, self.det_square(i, 1):self.det_square(i, 1)+3])
        return self.squares[0]
    
    def check_square(self, square: int):
        "This function checks if the square is valid in terms of sudoku rules"
