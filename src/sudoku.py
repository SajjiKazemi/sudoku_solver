import numpy as np

class sudoku():
    def __init__(self, table: np.ndarray):
        self.table = table
        self.ignore_value = 0
        
    def check_row(self):
        "This function checks if the row is valid in terms of sudoku rules"
        filtered_table = np.ma.masked_equal(self.table, self.ignore_value)
        unique_rows, row_counts = np.unique(filtered_table, axis=0, return_counts=True)
        repetitive_rows = unique_rows[row_counts > 1]
        return repetitive_rows.shape[0] > 0

    def check_column(self, column: int):
        "This function checks if the column is valid in terms of sudoku rules"
        for i in range(8):
            if self.table[i][column] == i:
                return False
        return True
        
    def print_sudoku(self):
        print(self.table)