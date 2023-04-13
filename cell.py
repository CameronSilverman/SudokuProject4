import pygame
from constants import *

class Cell:
    """
    Constructor for the Cell class
    """
    def __init__(self, value, row, col, screen, width, height):
        self.value = value
        self.tempvalue = value
        self.row = row
        self.col = col
        self.screen = screen
        self.width = width
        self.height = height
        self.sketched = False
        self.original = True

    """
    Setter for this cell’s value
    """
    def set_cell_value(self, value):
        self.tempvalue = value
        self.sketched = False
    """
    Setter for this cell’s sketched value
    """
    def set_sketched_value(self, value):
        self.tempvalue = value
        self.sketched = True
    """
    Draws this cell, along with the value inside it.
    If this cell has a nonzero value, that value is displayed.
    Otherwise, no value is displayed in the cell.
    The cell is outlined red if it is currently selected.
    """
    def draw(self):
        num_font = pygame.font.Font(None,60)
        if self.tempvalue != 0:
            if self.sketched == False:
                num_surf = num_font.render(str(self.tempvalue), True, BLACK, BG_COLOR)
            else:
                num_surf = num_font.render(str(self.tempvalue), True, GREY, BG_COLOR)

            num_rect = num_surf.get_rect(center = (10 + (self.row)*self.width + 40,10 + (self.col)*self.height + 40))
            self.screen.blit(num_surf, num_rect)
        else:
            num_surf = num_font.render(str(self.tempvalue), True, BG_COLOR, BG_COLOR)
            num_rect = num_surf.get_rect(center=(10 + (self.row) * self.width + 40, 10 + (self.col) * self.height + 40))
            self.screen.blit(num_surf, num_rect)

        #TOP
        pygame.draw.line(self.screen, BLACK, (self.row * self.width + 10, self.col * self.height + 10),
                         ((self.row + 1) * self.width + 10, self.col * self.height + 10), 4)
        #BOTTOM
        pygame.draw.line(self.screen, BLACK, (self.row * self.width + 10, (self.col+1) * self.height + 10),
                         ((self.row + 1) * self.width + 10, (self.col+1) * self.height + 10), 4)
        #LEFT
        pygame.draw.line(self.screen, BLACK, (self.row * self.width + 10, self.col * self.height + 10),
                         (self.row * self.width + 10, (self.col+1) * self.height + 10), 4)
        #RIGHT
        pygame.draw.line(self.screen, BLACK, ((self.row + 1) * self.width + 10, self.col * self.height + 10),
                         ((self.row + 1) * self.width + 10, (self.col + 1) * self.height + 10), 4)
