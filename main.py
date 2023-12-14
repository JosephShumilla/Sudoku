import pygame
from constants import *
from cell import *
from board import *
import copy

#draw game start screen
def draw_game_start(screen):

  start_title_font = pygame.font.Font(None, 50)
  button_font = pygame.font.Font(None, 45)
  # Color background
  screen.fill(BG_COLOR)
  # Initialize and draw title
  title_surface = start_title_font.render("Sudoku!", 0, TITLE_COLOR)
  title_rectangle = title_surface.get_rect(center=(WIDTH // 2,
                                                   HEIGHT // 2.5 - 150))
  screen.blit(title_surface, title_rectangle)
  option_surface = start_title_font.render("Select Game Mode:", 0, TITLE_COLOR)
  option_rectangle = option_surface.get_rect(center=(WIDTH // 2,
                                                     HEIGHT // 2 - 50))
  screen.blit(option_surface, option_rectangle)
  
  #initialize text for the buttons
  easy_text = button_font.render("Easy", 0, (255, 255, 255))
  medium_text = button_font.render("Medium", 0, (255, 255, 255))
  hard_text = button_font.render("Hard", 0, (255, 255, 255))
  quit_text = button_font.render("Quit", 0, (255, 255, 255))

  #initialize the surface of the buttons
  easy_surface = pygame.Surface(
    (easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
  easy_surface.fill(TITLE_COLOR)
  easy_surface.blit(easy_text, (10, 10))

  medium_surface = pygame.Surface(
    (medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
  medium_surface.fill(TITLE_COLOR)
  medium_surface.blit(medium_text, (10, 10))

  hard_surface = pygame.Surface(
    (hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
  hard_surface.fill(TITLE_COLOR)
  hard_surface.blit(hard_text, (10, 10))

  quit_surface = pygame.Surface(
    (quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
  quit_surface.fill(QUIT_COLOR)
  quit_surface.blit(quit_text, (10, 10))
  # Initialize button rectangle with positioning
  quit_rectangle = quit_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 95))
  easy_rectangle = easy_surface.get_rect(center=(WIDTH // 3.5 - 30,
                                                 HEIGHT // 4 + 150))
  medium_rectangle = medium_surface.get_rect(center=(WIDTH // 3.5 + 90,
                                                     HEIGHT // 4 + 150))
  hard_rectangle = hard_surface.get_rect(center=(WIDTH // 3.5 + 210,
                                                 HEIGHT // 4 + 150))
  # Draw buttons
  screen.blit(easy_surface, easy_rectangle)
  screen.blit(medium_surface, medium_rectangle)
  screen.blit(hard_surface, hard_rectangle)
  screen.blit(quit_surface, quit_rectangle)
  #button loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if easy_rectangle.collidepoint(event.pos):
          global difficulty
          difficulty = 'easy'
          return
        elif medium_rectangle.collidepoint(event.pos):
          difficulty = 'medium'
          return
        elif hard_rectangle.collidepoint(event.pos):
          difficulty = 'hard'
          return
        elif quit_rectangle.collidepoint(event.pos):
          sys.exit()
    pygame.display.update()

#draws the game over screen
def draw_game_over(screen):
  game_over_font = pygame.font.Font(None, 40)
  screen.fill(BG_COLOR)
  if board.check_board():
    text = 'Game Won!'
  else:
    text = "Game Over!"
  game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
  game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2,
                                                   HEIGHT // 2 - 100))
  screen.blit(game_over_surf, game_over_rect)
  restart_surf = game_over_font.render('Press r to play again...', 0,
                                       LINE_COLOR)
  restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
  screen.blit(restart_surf, restart_rect)
  #  Added key to return to main menu
  menu_surf = game_over_font.render('Press m to return to the main menu...', 0,
                                    LINE_COLOR)
  menu_rect = menu_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
  screen.blit(menu_surf, menu_rect)

#main block
if __name__ == "__main__":
  #main variables 
  game_continue = True
  game_over = False
  winner = 0
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption('Sudoku')
  #draws the start screen
  draw_game_start(screen)
  
  #draws the board
  screen.fill((255, 255, 255))
  board = Board(9, 9, WIDTH, HEIGHT, screen, difficulty)
  board_copy = copy.deepcopy(board.board)
  print_board(board.board)
  board.draw()
  #generates numbers on the board
  for row in range(9):
    for col in range(9):
      x = Cell(str(board.board[row][col]), row, col, screen)
      x.draw(screen)
      
  #game loop where player plays
  while game_continue:
    while game_continue: 
      count = 0
      count1 = 0
      #checks if board is full
      for row in board.board: 
        for col in row: 
          if col == 0: 
            count1 = count1 + 1
          else: 
            continue
      if count1 == 0: 
        draw_game_over(screen)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
          
          #checks if user clicked on a cell
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
          x, y = event.pos
          row = y // SQUARE_SIZE
          col = x // SQUARE_SIZE 
          global selected_row
          selected_row = row
          global selected_col
          selected_col = col
          #highlights square red if user clicks on it
          if board.board[row][col] == 0: 
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE , SQUARE_SIZE, SQUARE_SIZE), 5)
            count = count + 1
            
        if event.type == pygame.KEYDOWN:
          #if user clicks one on keyboard it shows up on board
            if event.key == pygame.K_1: 
              x = Cell(str(1), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 1
              selected_row = 0
              selected_col = 0
          #if user clicks two on keyboard it shows up on board
            if event.key == pygame.K_2: 
              x = Cell(str(2), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 2
              selected_row = 0
              selected_col = 0
          #if user clicks three on keyboard it shows up on board
            if event.key == pygame.K_3: 
              x = Cell(str(3), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 3
              selected_row = 0
              selected_col = 0
          #if user clicks four on keyboard it shows up on board
            if event.key == pygame.K_4: 
              x = Cell(str(4), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 4
              selected_row = 0
              selected_col = 0
          #if user clicks five on keyboard it shows up on board
            if event.key == pygame.K_5: 
              x = Cell(str(5), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 5
              selected_row = 0
              selected_col = 0
          #if user clicks six on keyboard it shows up on board
            if event.key == pygame.K_6: 
              x = Cell(str(6), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 6
              selected_row = 0
              selected_col = 0
          #if user clicks seven on keyboard it shows up on board
            if event.key == pygame.K_7: 
              x = Cell(str(7), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 7
              selected_row = 0
              selected_col = 0
          #if user clicks eight on keyboard it shows up on board
            if event.key == pygame.K_8: 
              x = Cell(str(8), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 8
              selected_row = 0
              selected_col = 0
          #if user clicks nine on keyboard it shows up on board
            if event.key == pygame.K_9: 
              x = Cell(str(9), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 9
              selected_row = 0
              selected_col = 0
          #if user clicks backspace then cell returns to 0
            if event.key == pygame.K_BACKSPACE:
              x = Cell(str(0), selected_row, selected_col, screen)
              x.draw(screen)
              board.board[selected_row][selected_col] = 0

        #if user clicks r, then it should reset the board
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
            screen.fill(BG_COLOR)
            board.reset_to_original()
            board.draw()
            board.board = board_copy
            for row in range(9):
              for col in range(9):
                x = Cell(str(board.board[row][col]), row, col, screen)
                x.draw(screen)
          #if user clicks m then this should return to main menu
          if event.key == pygame.K_m:
            draw_game_start(screen)
            screen.fill((255, 255, 255))
            board = Board(9, 9, WIDTH, HEIGHT, screen, difficulty)
            print_board(board.board)
            board.draw()
            board.board = board_copy
            for row in range(9):
              for col in range(9):
                x = Cell(str(board.board[row][col]), row, col, screen)
                x.draw(screen)
  
      pygame.display.update()
