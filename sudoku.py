import pygame

from board import Board

#import buttons

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test!")

#button_handler = buttons.Buttons(surface)

# Initializing RGB Color
color = (225, 0, 0)

# Changing surface color
surface.fill(color)

#button_handler.new_button("aaa", 200, 150, 100, 30, text="Restart")
#button_handler.draw_buttons()

# updates whole pygame screen
pygame.display.flip()

def main():
    playing = True
    board_obj = Board( 9, 9, 100, 100, "screen", "hard")

    while playing:
        pass

if __name__ == "__main__":
    main()
    quit()
"""
This is where all of the main code is meant to run. This can be structured however we want, but it will run everything.
In order to meet the requirements, we should *probably* use pygame.
"""