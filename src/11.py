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




        for i in range(9):
            for j in range(9):
                if self.table[i][j] == self.ignore_value and len(self.domains[i][j]) == 1:
                    scored_cell.append((i, j, 100))
                elif self.table[i][j] == self.ignore_value:
                    filtered_column = self.table[:, j][self.table[:, j] != self.ignore_value]
                    filtered_row = self.table[i][self.table[i] != self.ignore_value]
                    detd_square = self.det_square(i, j)
                    detd_square = self.separate_square(detd_square)
                    filtered_square = detd_square.flatten()[detd_square.flatten() != self.ignore_value]
                    score = len(filtered_column) + len(filtered_row) + len(filtered_square)
                    if score > scored_cell[2]:
                        scored_cell = (i, j, score)