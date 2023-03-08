from sudoku_generator import generate_sudoku
from cell import Cell

class Board:

  def __init__(self, rows, cols, width, height, screen, difficulty):
      self.rows = rows
      self.cols = cols
      self.width = width
      self.height = height
      self.screen = screen
      self.difficulty = difficulty
      self.board = generate_sudoku(self.cols,self.difficulty)


  def draw(self):
    pass


  def select(self, row, col):
    pass

  def click(self, x, y):
    pass

  def clear(self):
    pass


  def sketch(self, value):
    pass


  def place_number(self, value):
    pass


  def reset_to_original(self):
    pass

  def is_full(self):
    pass

  def update_board(self):
    pass


  def find_empty(self):
    pass


  def check_board(self):
    pass