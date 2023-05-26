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