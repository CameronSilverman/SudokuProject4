import math, random

class SudokuGenerator:


    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        if self.removed_cells == "easy":
            self.removed_cells = 30
        if self.removed_cells == "medium":
            self.removed_cells = 40
        if self.removed_cells == "hard":
            self.removed_cells = 50
        self.board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

    def get_board(self):
        return self.board
    def print_board(self):
        for x in self.get_board():
            print(x)

    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        for x in self.board:
            if x[col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start,row_start+3):
            for col in range(col_start,col_start+3):
                if self.board[row][col] == num:
                    return False
        return True


    def is_valid(self, row, col, num):
        row_start = 0
        col_start = 0
        if row <=2:
            row_start = 0
        elif row <=5:
            row_start = 3
        elif row <=8:
            row_start = 6
        if col <=2:
            col_start = 0
        elif col <=5:
            col_start = 3
        elif col <=8:
            col_start = 6

        if self.valid_in_row(row,num) and self.valid_in_col(col,num) and self.valid_in_box(row_start,col_start,num):
            return True
        else:
            return False


    def fill_box(self, row_start, col_start):
        unused_in_box = []
        pos_nums = {"1","2","3","4","5","6","7","8","9"}
        while len(pos_nums) > 0:
            unused_in_box.append(int(pos_nums.pop()))
        for row in range(row_start,row_start+3):
            for col in range(col_start,col_start+3):
                self.board[row][col] = unused_in_box.pop()


    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3,3)
        self.fill_box(6,6)


    def fill_remaining(self, row, col):
        # if col >= self.row_length:
        #     row += 1
        #     col = 0
        # if row >= self.row_length:
        #     return True
        #
        # if self.board[row][col] != 0:
        #     return self.fill_remaining(row, col + 1)
        #
        # for num in range(1, self.row_length + 1):
        #     if self.check_if_safe(row, col, num):
        #         self.board[row][col] = num
        #         if self.fill_remaining(row, col + 1):
        #             return True
        #         self.board[row][col] = 0
        # return False
        pass

    def fill_values(self):
        # self.fill_diagonal()
        # self.fill_remaining(9,9)
        pass

    def remove_cells(self):
        count = self.removed_cells
        while count != 0:
            cell_num = random.randint(0, self.row_length * self.row_length - 1)
            row = cell_num // self.row_length
            col = cell_num % self.row_length
            if self.board[row][col] != 0:
                count -= 1
                self.board[row][col] = 0


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_diagonal()
    sudoku.print_board()
