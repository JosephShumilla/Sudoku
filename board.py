from cell import Cell
from sudoku_generator import *
import pygame
from main import *
from constants import *
import copy
class Board:
  #instance variables in init function
  def __init__(self, rows, cols, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.rows = rows
    self.cols = cols
    self.selected_row = None
    self.selected_col = None
    if difficulty == 'easy':
      self.board = generate_sudoku(9, 9)
      #elf.board_copy = self.board.copy()
    elif difficulty =='medium':
      self.board = generate_sudoku(9, 40)
    elif difficulty =='hard':
      self.board = generate_sudoku(9, 50)
      #self.board_copy = self.board.copy()
    elif difficulty == 'test': 
      self.board = generate_sudoku(9, 0)
    self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in 
range(9)] for i in range(9)]
    self.board_copy = copy.deepcopy(self.board)
    

  #draws the board
  def draw(self):
    space = self.width/9
    for i in range(0, 10):  #Horizontal Bold Lines
      if (i%3==0) and i != 0:
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), BIG_LINE_WIDTH)
    for i in range(0, 10):   #Vertical Bold Lines
      if (i%3==0) and i!=0:
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i*SQUARE_SIZE, HEIGHT),BIG_LINE_WIDTH)
    for i in range (0, 9):
      for j in range(0, 9):
        self.cells[i][j].draw(self.screen)
    #Draws Normal Lines
    for i in range(1, BOARD_ROWS): 
      pygame.draw.line(screen, LINE_COLOR,
       (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    for j in range(1, BOARD_COLS): 
      pygame.draw.line(screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    for i in range(self.rows): 
      for j in range(self.cols): 
        self.cells[i][j].draw(self.screen)
  #selects a cell
  def select(self, row, col):
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        self.board[i][j] = False
    self.board[row][col] = True
    self.selected_row = row
    self.selected_col = col
    
  #returns a tuple of where the user clicked (row and col) **NOT USED
  def click(self, x, y):
    row = 0
    col = 0
    if 0 <= y < 100: 
      row = 0
    if 100 <= y < 200: 
      row = 1
    if 200 <= y < 300: 
      row = 2
    if 300 <= y < 400: 
      row = 3
    if 400 <= y < 500: 
      row = 4
    if 500<= y < 600: 
      row = 5
    if 600 <= y < 700: 
      row = 6
    if 700 <= y < 800: 
      row = 7
    if 800 <= y < 900:
      row = 8
    if 0 <= x < 100: 
      col = 0
    if 100 <= x < 200: 
      col = 1
    if 200 <= x < 300: 
      col = 2
    if 300 <= x < 400: 
      col = 3
    if 400 <= x < 500: 
      col = 4
    if 500<= x < 600: 
      col= 5
    if 600 <= x < 700: 
      col = 6
    if 700 <= x < 800: 
      col = 7
    if 800 <= x < 900:
      col = 8
    return (col, row)
    
  #clears the board **NOT USED
  def clear(self):
    self.board[self.selected_row][self.selected_col] = 0
    self.update_cells()
  #sketchs the value **NOT USED
  def sketch(self, value):
    self.set_sketched_value = value
    
  #places the value **NOT USED
  def place_number(self, value):
      self.board[self.selected_row][self.selected_col] = value
      self.update_cells()

  #resets to original board
  def reset_to_original(self):
    self.board = self.board_copy
    self.update_cells()
    
  #checks if board is full **NOT USED
  def is_full(self):
    for row in self.board:
      for item in row:
        if item == "0":
          return False
    return True
  #updates board
  def update_board(self):
    self.board.fill_values()
  #finds empty cells **NOT USED
  def find_empty(self):
    for i in range(9):
      for j in range(9): 
        if self.board[i][j] == "0":
          return True
          
  #checks board if its valid        
  def check_board(self):
    
    
    for row in range(9): 
      dict_row = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
      for item in self.board[row]: 
        dict_row[item] += 1
      for value in dict_row.values(): 
        if value == 2: 
          return False
        else: 
          continue
      dict_row = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for col in range(9): 
      dict_col = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
      for item in self.board: 
        dict_col[item[col]] += 1
      for value in dict_col.values(): 
        if value == 2: 
          return False
        else: 
          continue
      dict_col = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for row in range(9): 
      for col in range(9): 
        dict_box = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
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
        for i in range(row_start, row_start + 3): 
              for j in range(col_start, col_start + 3): 
                  if self.board[i][j] == 0: 
                      continue
                  else: 
                      dict_box[self.board[i][j]] += 1
        for value in dict_box.values(): 
          if value == 2: 
            return False
          else: 
            continue
      dict_col = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    return True
      
    
    
      
    
  #update cells
  def update_cells(self): 
    self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in 
    range(9)] for i in range(9)]
    
if __name__ == "__main__": 
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Sudoku")
  screen.fill(BG_COLOR)
  #initialize game state
  player = 1
  number_one = "1"
  number_two = "2"
  number_three = "3"
  number_four = "4"
  number_five = "5"
  number_six = "6"
  number_seven = "7"
  number_eight = "8"
  number_nine = "9"
  winner = 0
  game_over = False
  # Draws the board
  board = Board(BOARD_ROWS, BOARD_COLS, WIDTH, HEIGHT, screen, 'easy')
  board.draw()
  while True: 
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN and not game_over: 
        x, y = event.pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

board = Board(9, 9, 450,450, screen,'test')

