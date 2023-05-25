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