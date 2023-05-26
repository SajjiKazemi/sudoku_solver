import numpy as np
import copy

class sudoku():
    def __init__(self, table: np.ndarray):
        self.refrence_table = table
        self.table = table
        self.ignore_value = 0
        self.solved = False
        self.saved_tables = []
        self.saved_domains = []
        
    def check_row(self, row: int):
        "This function checks if the row is valid in terms of sudoku rules"
        filtered_row = self.table[row][self.table[row] != self.ignore_value]
        unique_elements = np.unique(filtered_row)
        if len(filtered_row) != len(unique_elements):
            return False
        return True

    def check_column(self, column: int):
        "This function checks if the column is valid in terms of sudoku rules"
        filtered_column = self.table[:, column][self.table[:, column] != self.ignore_value]
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
    
    def separate_square(self, spec_square: int):
        "This function separates the sudoku into 9 squares"
        first_digit, second_digit = self.get_square_address(spec_square)
        for k in range(3):
            for l in range(3):
                detd_square = self.table[first_digit: first_digit+3, second_digit: second_digit+3]
        # for i in range(9):
        #     self.squares.append(self.table[self.det_square(i, 0):self.det_square(i, 0)+3, self.det_square(i, 1):self.det_square(i, 1)+3])
        # return self.squares
        return detd_square
    
    def check_square(self, square: int):
        "This function checks if the square is valid in terms of sudoku rules"
        detd_squares = self.separate_square(square)
        filtered_square = detd_squares.flatten()[detd_squares.flatten() != self.ignore_value]
        unique_elements = np.unique(filtered_square)
        if len(filtered_square) != len(unique_elements):
            return False
        return True
    
    def check_constraints(self, row: int, column: int):
        "This function checks if the constraints are satisfied"
        if not self.check_row(row):
            return False
        if not self.check_column(column):
            return False
        if not self.check_square(self.det_square(row, column)):
            return False
        return True

    def check_sudoku(self):
        "This function checks if the sudoku is valid in terms of sudoku rules"
        for i in range(9):
            if not self.check_row(i):
                return False
            if not self.check_column(i):
                return False
            if not self.check_square(i):
                return False
        return True

    def prepare_domains(self):
        "This function prepares the domains for the sudoku cells"
        self.domains = []
        for i in range(9):
            self.domains.append([])
            for j in range(9):
                if self.table[i][j] == self.ignore_value:
                    self.domains[i].append([1, 2, 3, 4, 5, 6, 7, 8, 9])
                else:
                    self.domains[i].append([self.table[i][j]])
        return self.domains
    
    def get_square_address(self, square: int):
        if square == 0:
            return 0, 0
        elif square == 1:
            return 0, 3
        elif square == 2:
            return 0, 6
        elif square == 3:
            return 3, 0
        elif square == 4:
            return 3, 3
        elif square == 5:
            return 3, 6
        elif square == 6:
            return 6, 0
        elif square == 7:
            return 6, 3
        elif square == 8:
            return 6, 6

    def correct_domains(self, row: int, column: int):
        "This function corrects the domains for the sudoku"
        for i in range(9-row):
            for j in range(9-column):
                spec_square = self.det_square(row+i, column+j)
                first_digit, second_digit = self.get_square_address(spec_square)

                if self.table[row+i][column+j] != self.ignore_value:
                    for k in range(9-column):
                        if self.table[row+i][column+j] in self.domains[row+i][column+k]:
                            self.domains[row+i][column+k].remove(self.table[row+i][column+j])
                            if len(self.domains[row+i][column+k]) == 0 and self.refrence_table[row+i][column+j] != self.ignore_value:
                                self.domains[row+i][column+k] = [self.refrence_table[row+i][column+j]]
                    for l in range(9-row):
                        if self.table[row+i][column+j] in self.domains[row+k][column+j]:
                            self.domains[row+k][column+j].remove(self.table[row+i][column+j])
                            if len(self.domains[row+k][column+j]) == 0 and self.refrence_table[row+i][column+j] != self.ignore_value:
                                self.domains[row+k][column+j] = [self.refrence_table[row+i][column+j]]
                    
                    for k in range(3):
                        for l in range(3):
                            if self.table[first_digit+k][second_digit+l] in self.domains[row+i][column+j]:
                                self.domains[row+i][column+j].remove(self.table[first_digit+k][second_digit+l])
                                if len(self.domains[row+i][column+j]) == 0 and self.refrence_table[row+i][column+j] != self.ignore_value:
                                    self.domains[row+i][column+j] = [self.refrence_table[row+i][column+j]]
        return self.domains

        
    
    def set_cell(self):
        for i in range(9):
            for j in range(9):
                if self.table[i][j] == self.ignore_value:
                    if len(self.domains[i][j]) == 0:
                        return False
                    else:
                        while self.table[i][j] == self.ignore_value and len(self.domains[i][j]) != 0:
                            self.table[i][j] = self.domains[i][j][0]
                            self.domains[i][j].remove(self.domains[i][j][0])
                            if self.check_constraints(i, j):
                                self.saved_states()
                                self.correct_domains(i, j)
                                return True
                            else:
                                self.table[i][j] = self.ignore_value
                        return False
        
                #if len(self.domains[i][j]) == 1:
                #    self.table[i][j] = self.domains[i][j][0]
        print("No cell to set")
        print("Sudoku is solved!")
        self.solved = True
        return self.solved
    
    def saved_states(self):
        self.saved_tables.append(copy.deepcopy(self.table))
        self.saved_domains.append(copy.deepcopy(self.domains))

    def return_to_last_state(self):
        if len(self.saved_tables) > 1:
            del self.saved_tables[-1]
            del self.saved_domains[-1]
        self.table = self.saved_tables[-1]
        self.domains = self.saved_domains[-1]


    def backTrack_search(self):
        self.prepare_domains()
        self.correct_domains(row=0, column=0)
        #self.saved_states()
        
        while not self.solved:
            while self.set_cell():
                pass
            self.return_to_last_state()

        
        return self.table