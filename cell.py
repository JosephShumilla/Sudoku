import pygame
from constants import *

class Cell:   #Initializes the cell object
  def __init__(self, value, row, col, screen):
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen
    self.selected = False
  #Sets the cell value to value
  def set_cell_value(self, value):
    self.value = value

  def set_sketched_value(self, value):
    self.sketched_value = value
    
  def draw(self, screen):
    # Draws game board from 2d list
    number_font = pygame.font.Font(None,50)
    one = number_font.render("1", 0, NUMBER_COLOR)
    two = number_font.render("2", 0, NUMBER_COLOR)
    three = number_font.render("3", 0, NUMBER_COLOR)
    four = number_font.render("4", 0, NUMBER_COLOR)
    five = number_font.render("5", 0, NUMBER_COLOR)
    six = number_font.render("6", 0, NUMBER_COLOR)
    seven = number_font.render("7", 0, NUMBER_COLOR)
    eight = number_font.render("8", 0, NUMBER_COLOR)
    nine = number_font.render("9", 0, NUMBER_COLOR)
    
    if self.selected:
      # All statements to handle selection by user
      pygame.draw.rect(screen, (255,0,0), (pygame.Rect(self.col*SQUARE_SIZE,  self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 15))
      self.selected = False
    if self.value == "1":
      one_rect = one.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(one, one_rect)
      #If the user selects 2, etc
    if self.value == "2":
      two_rect = two.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(two, two_rect)
    if self.value == "3":
      three_rect = three.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(three, three_rect)
    if self.value == "4":
      four_rect = four.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(four, four_rect)
    if self.value == "5": 
      five_rect = five.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(five, five_rect)
    if self.value == "6": 
      six_rect = six.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(six, six_rect)
    if self.value == "7": 
      seven_rect = seven.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(seven, seven_rect)
    if self.value == "8":
      eight_rect = eight.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(eight, eight_rect)
    if self.value == "9":
      nine_rect = nine.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      screen.blit(nine, nine_rect)  
