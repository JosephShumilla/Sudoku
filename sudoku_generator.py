import random
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
def print_board(board): 
    x = board
    for item in x: 
        for cell in item: 
            print(cell, end=" ")
        print()
    return 
class SudokuGenerator: 
    def __init__(self, row_length, removed_cells): 
      # Constructor for class
        self.row_length = row_length 
        self.removed_cells = removed_cells
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.box_length = 3
    def get_board(self): 
      # returns board
        return self.board

    def valid_in_row(self,row, num): 
      # checks if input valid in row
        count = 0
        for item in self.board[row]: 
            if item == num: 
                count = count + 1
            else: 
                continue
        if count > 0: 
            return False
        else: 
            return True
    def valid_in_col(self,col,num):
      # checks input in col
        count = 0 
        for item in self.board: 
            if item[col] == num: 
                count = count + 1
            else: 
                continue
        if count > 0: 
            return False
        else: 
            return True

    def valid_in_box(self,row_start, col_start, num): 
      # Checks if input is valid in sudoku "box"
        dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        count = 0
        for i in range(row_start, row_start + 3): 
            for j in range(col_start, col_start + 3): 
                if self.board[i][j] == 0: 
                    continue
                else: 
                    dict[self.board[i][j]] += 1
        dict[num] += 1
        for value in dict.values(): 
            if value == 2: 
                count = count + 1
            else: 
                continue
        if count > 0: 
            return False
        else: 
            return True
    def is_valid(self, row, col, num): 
      # Checks if input is valid in row and col
        count = 0
        if 0 <= row < 3: 
            row_start = 0
        if 3 <= row < 6: 
            row_start = 3
        if 6 <= row < 9: 
            row_start = 6
        if 0 <= col < 3: 
            col_start = 0
        if 3 <= col< 6: 
            col_start = 3
        if 6 <= col <= 9: 
            col_start = 6
        if self.valid_in_row(row, num): 
            count = count + 1
        if self.valid_in_col(col, num): 
            count = count + 1
        if self.valid_in_box(row_start, col_start, num):
            count = count + 1
        if count == 3: 
            return True
        else:
            return False
    def fill_box(self, row_start, col_start):
      # generates box
        unused_in_box = [1,2,3,4,5,6,7,8,9]
        for i in range(row_start, row_start + 3): 
            for j in range(col_start, col_start + 3): 
                x = random.randint(1,9)
                while x not in unused_in_box: 
                    x = random.randint(1,9)
                self.board[i][j] = x
                unused_in_box.remove(x)
        return self.board
    def fill_diagonal(self): 
        self.fill_box(0,0)
        self.fill_box(3,3)
        self.fill_box(6,6)
        return self.board
    def remove_cells(self): 
      # removes appropriate cells from
        list = []
        while self.removed_cells > 0: 
            x = random.randint(0,8)
            y = random.randint(0,8)
            while (x,y) in list: 
                x = random.randint(0,8)
                y = random.randint(0,8)
            list.append((x, y))
            self.board[x][y] = 0
            self.removed_cells = self.removed_cells - 1
    def fill_remaining(self, row, col):
      # Given by Professor Zhou, fills remaining cells in sudoku board
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
        return self.board


    


    



    
            