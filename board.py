from sudoku_generator import generate_sudoku
from cell import Cell
import pygame, sys
from constants import *

class Board:
  """
  Constructor for the Board class.
  screen is a window from PyGame.
  difficulty is a variable to indicate if the user chose easy, medium, or hard.
  """
  def __init__(self, rows, cols, width, height, screen, difficulty):
    self.rows = rows
    self.cols = cols
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.board = generate_sudoku(self.cols,self.difficulty)
    self.cells = [[0 for x in range(0,9)]for y in range(0,9)]
    self.selected_row = -1
    self.selected_col = -1
    self.restart = False
    for row in range(0,9):
      for col in range(0,9):
        self.cells[row][col] = Cell(self.board[row][col],row,col,self.screen,80,80)
    for row in range(0, 9):
      for col in range(0, 9):
        if self.cells[row][col].value == 0:
          self.cells[row][col].original = False
    for x in self.board:
      print(x)



  """
  Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
  Draws every cell on this board.
  """
  def draw(self):

    #GRID
    for i in range(1,5):
      pygame.draw.line(self.screen, BLACK, ((i-1)*240 + 10, 10), ((i-1)*240 + 10, 730), 8)
    for i in range(1,5):
      pygame.draw.line(self.screen, BLACK, (10, (i-1)*240 + 10), (730, (i-1)*240 + 10), 8)

    #BUTTONS
    #RESET
    pygame.draw.line(self.screen, BLACK, (re_box_x1, menu_button_box_y1), (re_box_x2, menu_button_box_y1), 8)
    pygame.draw.line(self.screen, BLACK, (re_box_x1, menu_button_box_y2), (re_box_x2, menu_button_box_y2), 8)
    pygame.draw.line(self.screen, BLACK, (re_box_x1, menu_button_box_y1), (re_box_x1, menu_button_box_y2), 8)
    pygame.draw.line(self.screen, BLACK, (re_box_x2, menu_button_box_y1), (re_box_x2, menu_button_box_y2), 8)
    reset_font = pygame.font.Font(None, 60)
    reset_surf = reset_font.render("RESET", True, BLACK, BG_COLOR)
    reset_rect = reset_surf.get_rect(center=(130,805))
    self.screen.blit(reset_surf, reset_rect)
    #RESTART
    pygame.draw.line(self.screen, BLACK, (rst_box_x1, menu_button_box_y1), (rst_box_x2, menu_button_box_y1), 8)
    pygame.draw.line(self.screen, BLACK, (rst_box_x1, menu_button_box_y2), (rst_box_x2, menu_button_box_y2), 8)
    pygame.draw.line(self.screen, BLACK, (rst_box_x1, menu_button_box_y1), (rst_box_x1, menu_button_box_y2), 8)
    pygame.draw.line(self.screen, BLACK, (rst_box_x2, menu_button_box_y1), (rst_box_x2, menu_button_box_y2), 8)
    restart_font = pygame.font.Font(None, 60)
    restart_surf = restart_font.render("RESTART", True, BLACK, BG_COLOR)
    restart_rect = restart_surf.get_rect(center=(370, 805))
    self.screen.blit(restart_surf, restart_rect)
    #EXIT
    pygame.draw.line(self.screen, BLACK, (ext_box_x1, menu_button_box_y1), (ext_box_x2, menu_button_box_y1), 8)
    pygame.draw.line(self.screen, BLACK, (ext_box_x1, menu_button_box_y2), (ext_box_x2, menu_button_box_y2), 8)
    pygame.draw.line(self.screen, BLACK, (ext_box_x1, menu_button_box_y1), (ext_box_x1, menu_button_box_y2), 8)
    pygame.draw.line(self.screen, BLACK, (ext_box_x2, menu_button_box_y1), (ext_box_x2, menu_button_box_y2), 8)
    exit_font = pygame.font.Font(None, 60)
    exit_surf = exit_font.render("EXIT", True, BLACK, BG_COLOR)
    exit_rect = exit_surf.get_rect(center=(610, 805))
    self.screen.blit(exit_surf, exit_rect)

    #CELLS
    for row in self.cells:
      for cell in row:
        cell.draw()

  """
  Marks the cell at (row, col) in the board as the current selected cell.
  Once a cell has been selected, the user can edit its value or sketched value. 
  """
  def select(self, row, col):
    RED = (255,0,0)
    self.draw()
    # TOP
    pygame.draw.line(self.screen, RED, (row * 80 + 10, col * 80 + 10),
                     ((row + 1) * 80 + 10, col * 80 + 10), 4)
    # BOTTOM
    pygame.draw.line(self.screen, RED, (row * 80 + 10, (col + 1) * 80 + 10),
                     ((row + 1) * 80 + 10, (col + 1) * 80 + 10), 4)
    # LEFT
    pygame.draw.line(self.screen, RED, (row * 80 + 10, col * 80 + 10),
                     (row * 80 + 10, (col + 1) * 80 + 10), 4)
    # RIGHT
    pygame.draw.line(self.screen, RED, ((row + 1) * 80 + 10, col * 80 + 10),
                     ((row + 1) * 80 + 10, (col + 1) * 80 + 10), 4)

  """
  Clears the value cell. Note that the user can only remove the cell values and sketched value that are filled 
  by themselves.
  """
  def clear(self):
    if (not self.cells[self.selected_row][self.selected_col].original):
      self.cells[self.selected_row][self.selected_col].tempvalue = 0
    self.update_board()

  """
  Sets the sketched value of the current selected cell equal to user entered value.
  It will be displayed at top left corner of the cell using in the draw() function.
  """
  def sketch(self, value):
    self.cells[self.selected_row][self.selected_col].set_sketched_value(value)
    self.update_board()

  """
  Sets the value of the current selected cell equal to user entered value.
  Called when the user presses the Enter key.
  """
  def place_number(self, value):
    self.cells[self.selected_row][self.selected_col].set_cell_value(self.cells[self.selected_row][self.selected_col].tempvalue)

  """
  Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
  """
  def reset_to_original(self):
    for row, cell_row in enumerate(self.cells):
      for col, cel in enumerate(cell_row):
        if self.cells[row][col].original == False:
          self.cells[row][col].tempvalue = 0
          self.cells[row][col].draw()
    self.update_board()


  """
    If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) 
    of the cell which was clicked. Otherwise, this function returns None.
    """

  def click(self, x, y):
    row = 0
    col = 0
    # CELL
    if x >= 10 and x <= 730 and y >= 10 and y <= 730:
      for r in range(0, 9):
        if x <= ((r + 1) * 80 + 10):
          row = r
          break
      for c in range(0, 9):
        if y <= ((c + 1) * 80 + 10):
          col = c
          break
      self.select(row, col)
      return (row, col)
    # RESET
    elif x >= 20 and x <= 240 and y >= 775 and y <= 835:
      self.reset_to_original()
      self.update_board()
      return (-1, 1)
    # RESTART
    elif x >= 260 and x <= 480 and y >= 775 and y <= 835:
      self.restart = True
      return(-1,1)
    # EXIT
    elif x >= 500 and x <= 720 and y >= 775 and y <= 835:
      pygame.quit()
      sys.exit()
    else:
      return (-1,-1)
  """
  Returns a Boolean value indicating whether the board is full or not. 
  """
  def is_full(self):
    isFull = True
    for row, cell_row in enumerate(self.cells):
      for col, cel in enumerate(cell_row):
        if self.cells[row][col].tempvalue == 0:
          isFull = False
    return isFull

  """
  Updates the underlying 2D board with the values in all cells.
  """
  def update_board(self):
    for r in range(0,9):
      for c in range(0,9):
        self.board[r][c] = self.cells[r][c].tempvalue
    print()
    for x in self.board:
      print(x)

  """
  Finds an empty cell and returns its row and col as a tuple (x, y).
  """
  def find_empty(self):
    for r in range(0, 9):
      for c in range(0, 9):
        if self.board[r][c] == 0:
          return (r,c)
    return (-1,-1)

  """
  Check whether the Sudoku board is solved correctly.
  """
  def check_board(self):
    is_valid = True
    for row in range(0,9):
      for col in range(0,9):
        num = self.board[row][col]
        row_start = 0
        col_start = 0
        if row <= 2:
          row_start = 0
        elif row <= 5:
          row_start = 3
        elif row <= 8:
          row_start = 6
        if col <= 2:
          col_start = 0
        elif col <= 5:
          col_start = 3
        elif col <= 8:
          col_start = 6

        valid_in_row = True
        count = 0
        for x in self.board[row]:
          if x == num:
            count += 1
        if count > 1:
          valid_in_row = False

        valid_in_col = True
        count = 0
        for x in self.board:
          if x[col] == num:
            count += 1
        if count > 1:
          valid_in_col = False

        valid_in_box = True
        count = 0
        for r in range(row_start, row_start + 3):
          for c in range(col_start, col_start + 3):
            if self.board[r][c] == num:
              count += 1
        if count > 1:
          valid_in_box = False
        print(f"({row},{col}): {valid_in_row}, {valid_in_col}, {valid_in_box}")
        if (not valid_in_row) or (not valid_in_col) or (not valid_in_box):
          is_valid = False
    return is_valid