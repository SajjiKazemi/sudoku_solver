import numpy as np
import copy
import random

class sudoku():
    def __init__(self, table: np.ndarray):
        self.refrence_table = table
        self.table = table
        self.child_table = table
        self.ignore_value = 0
        self.solved = False
        self.saved_tables = []
        self.saved_domains = []
        self.domains = self.prepare_domains()
        self.cells = self.get_cells()
        
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

    def correct_domains(self):
        "This function corrects the domains for the sudoku"
        for i in range(9):
            for j in range(9):
                spec_square = self.det_square(i, j)
                first_digit, second_digit = self.get_square_address(spec_square)
                
                if self.table[i][j] != self.ignore_value:
                    for k in range(9):
                        if self.table[i][j] in self.domains[i][k]:
                            self.domains[i][k].remove(self.table[i][j])
                            if len(self.domains[i][k]) == 0 and self.refrence_table[i][j] != self.ignore_value:
                                self.domains[i][k].append(self.refrence_table[i][j])

                        if self.table[i][j] in self.domains[k][j]:
                            self.domains[k][j].remove(self.table[i][j])
                            if len(self.domains[k][j]) == 0 and self.refrence_table[i][j] != self.ignore_value:
                                self.domains[k][j].append(self.refrence_table[i][j])

                    for k in range(3):
                        for l in range(3):
                            if self.table[i][j] in self.domains[k+first_digit][l+second_digit]:
                                self.domains[k+first_digit][l+second_digit].remove(self.table[i][j])
                                if len(self.domains[k+first_digit][l+second_digit]) == 0 and self.refrence_table[i][j] != self.ignore_value:
                                    self.domains[k+first_digit][l+second_digit].append(self.refrence_table[i][j])

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

    def get_value(self, heuristic = False):
        domain_values = self.domains[self.cells[0][0]][self.cells[0][1]]
        if not heuristic:
            random.shuffle(domain_values)
        else:
            domain_values = self.get_least_constraining_value((self.cells[0][0], self.cells[0][1]))
        return domain_values

    def create_children(self, domain_values: list, cell: tuple):
        self.children = []
        for i in range(len(domain_values)):
            table = copy.deepcopy(self.table)
            table[cell[0]][cell[1]] = domain_values[i]
            self.children.append(sudoku(table))
        self.expa_nodes = 1
        return self.children


    def backTrack_search(self, forward_checking = False, heuristic = False):
        "This function solves the sudoku using backtracking search"
        if forward_checking:
            self.correct_domains()
            self.get_cells(heuristic)
        self.children = self.create_children(self.get_value(heuristic), self.cells[0])            

        while len(self.children) > 0:

            if not self.children[0].check_sudoku():
                del self.children[0]
                pass
            elif self.children[0].is_complete():
                self.solved = True
                return self.children[0].table, self.expa_nodes, True
            else:
                self.child_table, exp_nodes, state = self.children[0].backTrack_search(forward_checking, heuristic)
                self.expa_nodes = self.expa_nodes + exp_nodes
                if state == None:
                    self.expa_nodes = self.expa_nodes + exp_nodes
                    del self.children[0]
                    pass
                elif state == True:
                    return self.child_table, self.expa_nodes, True
        return self.child_table, self.expa_nodes, None
        
    def is_complete(self):
        for i in range(9):
            for j in range(9):
                if self.table[i][j] == self.ignore_value:
                    return False
        return True

    def get_cells(self, heuristic = False):
        self.cells = []
        for i in range(9):
            for j in range(9):
                if self.table[i][j] == self.ignore_value:
                    self.cells.append((i, j))
        if not heuristic:
            random.shuffle(self.cells)
        else:
            self.cell = self.get_most_constrained_variable(self.cells)
        return self.cells
    
    def get_most_constrained_variable(self, cells: list):
        "This function returns the most constrained variable"
        self.mrv = []
        scored_cell = []
        for i in range(len(cells)):
            if len(self.domains[cells[i][0]][cells[i][1]]) == 1:
                scored_cell.append((cells[i][0], cells[i][1], 1000))
            else:
                filtered_column = self.table[:, cells[i][1]][self.table[:, cells[i][1]] != self.ignore_value]
                filtered_row = self.table[cells[i][0]][self.table[cells[i][0]] != self.ignore_value]
                detd_square = self.det_square(cells[i][0], cells[i][1])
                detd_square = self.separate_square(detd_square)
                filtered_square = detd_square.flatten()[detd_square.flatten() != self.ignore_value]
                score = len(filtered_column) + len(filtered_row) + len(filtered_square)
                scored_cell.append((cells[i][0], cells[i][1], score))

        scored_cell = sorted(scored_cell, key=lambda x: x[2], reverse=True)
        scored_cell = np.array(scored_cell)
        cells = scored_cell[:, :2]
        return cells                   
    
    def get_least_constraining_value(self, cell: tuple):
        "This function returns the least constraining value"
        scored_value = []
        domains_column = 0
        domains_row = 0
        domains_square = 0
        domain = self.domains[cell[0]][cell[1]]
        for value in domain:
            for i in range(9):
                domains_column = domains_column + 1 if np.isin(value, self.domains[i][cell[1]]) else domains_column
                domains_row = domains_row + 1 if np.isin(value, self.domains[cell[0]][i]) else domains_row
                detd_square = self.det_square(cell[0], cell[1])
                detd_square_address = self.get_square_address(detd_square)
                for j in range(3):
                    for k in range(3):
                        domains_square = domains_square + 1 if np.isin(value, self.domains[detd_square_address[0]+j][detd_square_address[1]+k]) else domains_square

            score = domains_column + domains_row + domains_square
            domains_column = 0
            domains_row = 0
            domains_square = 0
            scored_value.append((value, score))
        scored_value = sorted(scored_value, key=lambda x: x[1], reverse=True)
        scored_value = [x[0] for x in scored_value]
        return scored_value
    