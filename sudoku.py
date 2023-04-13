"""
This is where all the main code is meant to run. This can be structured however we want, but it will run everything.
In order to meet the requirements, we should *probably* use pygame.
"""
import pygame, sys
from board import Board
from constants import *

def main():
    # CONSTANTS

    main_menu = True
    in_game = False
    game_lose = False
    game_win = False
    difficulty = "easy"

    pygame.init()
    pygame.display.set_caption("Sudoku!")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)

    #Main Loop
    while True:
        screen_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(screen, BG_COLOR, screen_rect)
        #Main menu screen
        while main_menu:
            #WELCOME
            welcome_font = pygame.font.Font(None, 100)
            welcome_surf = welcome_font.render("Welcome to Sudoku!", True, BLACK, BG_COLOR)
            welcome_rect = welcome_surf.get_rect(center=(370,200))
            screen.blit(welcome_surf, welcome_rect)
            #CHOOSE DIFFICULTY
            diff_font = pygame.font.Font(None, 70)
            diff_surf = diff_font.render("Select Game Mode:", True, BLACK, BG_COLOR)
            diff_rect = diff_surf.get_rect(center=(370,400))
            screen.blit(diff_surf, diff_rect)

            # BUTTONS
            # EASY
            pygame.draw.line(screen, BLACK, (re_box_x1, game_button_box_y1), (re_box_x2, game_button_box_y1), 8)
            pygame.draw.line(screen, BLACK, (re_box_x1, game_button_box_y2), (re_box_x2, game_button_box_y2), 8)
            pygame.draw.line(screen, BLACK, (re_box_x1, game_button_box_y1), (re_box_x1, game_button_box_y2), 8)
            pygame.draw.line(screen, BLACK, (re_box_x2, game_button_box_y1), (re_box_x2, game_button_box_y2), 8)
            reset_font = pygame.font.Font(None, 60)
            reset_surf = reset_font.render("EASY", True, BLACK, BG_COLOR)
            reset_rect = reset_surf.get_rect(center=(((re_box_x2-re_box_x1)/2+re_box_x1), ((game_button_box_y2-game_button_box_y1)/2+game_button_box_y1)))
            screen.blit(reset_surf, reset_rect)
            # MEDIUM
            pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y1), (rst_box_x2, game_button_box_y1), 8)
            pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y2), (rst_box_x2, game_button_box_y2), 8)
            pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y1), (rst_box_x1, game_button_box_y2), 8)
            pygame.draw.line(screen, BLACK, (rst_box_x2, game_button_box_y1), (rst_box_x2, game_button_box_y2), 8)
            restart_font = pygame.font.Font(None, 60)
            restart_surf = restart_font.render("MEDIUM", True, BLACK, BG_COLOR)
            restart_rect = restart_surf.get_rect(center=(((rst_box_x2-rst_box_x1)/2+rst_box_x1), ((game_button_box_y2-game_button_box_y1)/2+game_button_box_y1)))
            screen.blit(restart_surf, restart_rect)
            # HARD
            pygame.draw.line(screen, BLACK, (ext_box_x1, game_button_box_y1), (ext_box_x2, game_button_box_y1), 8)
            pygame.draw.line(screen, BLACK, (ext_box_x1, game_button_box_y2), (ext_box_x2, game_button_box_y2), 8)
            pygame.draw.line(screen, BLACK, (ext_box_x1, game_button_box_y1), (ext_box_x1, game_button_box_y2), 8)
            pygame.draw.line(screen, BLACK, (ext_box_x2, game_button_box_y1), (ext_box_x2, game_button_box_y2), 8)
            exit_font = pygame.font.Font(None, 60)
            exit_surf = exit_font.render("HARD", True, BLACK, BG_COLOR)
            exit_rect = exit_surf.get_rect(center=(((ext_box_x2-ext_box_x1)/2+ext_box_x1), ((game_button_box_y2-game_button_box_y1)/2+game_button_box_y1)))
            screen.blit(exit_surf, exit_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    # EASY
                    if x >= re_box_x1 and x <= re_box_x2 and y >= game_button_box_y1 and y <= game_button_box_y2:
                        difficulty = "easy"
                        main_menu = False
                        in_game = True
                    # MEDIUM
                    if x >= rst_box_x1 and x <= rst_box_x2 and y >= game_button_box_y1 and y <= game_button_box_y2:
                        difficulty = "medium"
                        main_menu = False
                        in_game = True
                    # HARD
                    if x >= ext_box_x1 and x <= ext_box_x2 and y >= game_button_box_y1 and y <= game_button_box_y2:
                        difficulty = "hard"
                        main_menu = False
                        in_game = True
            pygame.display.update()

        screen_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(screen, BG_COLOR, screen_rect)
        #sudoku board
        while in_game:
            board_obj = Board(9, 9, 900, 900, screen, difficulty)
            board_obj.draw()
            while in_game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x,y) = pygame.mouse.get_pos()
                        (board_obj.selected_row,board_obj.selected_col) = board_obj.click(x,y)
                        print("("+str(board_obj.selected_row)+","+str(board_obj.selected_col)+")")
                        print("Value: " + str(board_obj.cells[board_obj.selected_row][board_obj.selected_col].tempvalue))
                    if (board_obj.selected_row != -1) and (board_obj.selected_col != -1) and event.type == pygame.KEYDOWN:
                        if not board_obj.cells[board_obj.selected_row][board_obj.selected_col].original:
                            if event.key == 8:
                                board_obj.clear()
                            elif event.key == 49:
                                board_obj.sketch(1)
                            elif event.key == 50:
                                board_obj.sketch(2)
                            elif event.key == 51:
                                board_obj.sketch(3)
                            elif event.key == 52:
                                board_obj.sketch(4)
                            elif event.key == 53:
                                board_obj.sketch(5)
                            elif event.key == 54:
                                board_obj.sketch(6)
                            elif event.key == 55:
                                board_obj.sketch(7)
                            elif event.key == 56:
                                board_obj.sketch(8)
                            elif event.key == 57:
                                board_obj.sketch(9)
                            elif event.key == 13:
                                board_obj.place_number(board_obj.cells[board_obj.selected_row][board_obj.selected_col].tempvalue)
                            board_obj.draw()
                            board_obj.select(board_obj.selected_row, board_obj.selected_col)
                if board_obj.restart == True:
                    in_game = False
                    main_menu = True

                (x,y) = board_obj.find_empty()

                if x == -1 and y == -1:
                    if board_obj.check_board():
                        in_game = False
                        game_win = True
                    else:
                        in_game = False
                        game_lose = True
                pygame.display.update()

            screen_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
            pygame.draw.rect(screen, BG_COLOR, screen_rect)
            #Game win screen
            while game_win:
                #WIN PROMPT
                diff_font = pygame.font.Font(None, 80)
                diff_surf = diff_font.render("Sudoku Solved!", True, BLACK, BG_COLOR)
                diff_rect = diff_surf.get_rect(center=(370, 400))
                screen.blit(diff_surf, diff_rect)

                #EXIT
                pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y1), (rst_box_x2, game_button_box_y1), 8)
                pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y2), (rst_box_x2, game_button_box_y2), 8)
                pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y1), (rst_box_x1, game_button_box_y2), 8)
                pygame.draw.line(screen, BLACK, (rst_box_x2, game_button_box_y1), (rst_box_x2, game_button_box_y2), 8)
                restart_font = pygame.font.Font(None, 60)
                restart_surf = restart_font.render("EXIT", True, BLACK, BG_COLOR)
                restart_rect = restart_surf.get_rect(center=(
                ((rst_box_x2 - rst_box_x1) / 2 + rst_box_x1), ((game_button_box_y2 - game_button_box_y1) / 2 + game_button_box_y1)))
                screen.blit(restart_surf, restart_rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()
                        # EXIT
                        if x >= rst_box_x1 and x <= rst_box_x2 and y >= game_button_box_y1 and y <= game_button_box_y2:
                            pygame.quit()
                            sys.exit()
                pygame.display.update()

            screen_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
            pygame.draw.rect(screen, BG_COLOR, screen_rect)
            #Game lose screen
            while game_lose:
                #LOSE PROMPT
                diff_font = pygame.font.Font(None, 80)
                diff_surf = diff_font.render("Incorrect Solution", True, BLACK, BG_COLOR)
                diff_rect = diff_surf.get_rect(center=(370, 400))
                screen.blit(diff_surf, diff_rect)

                #RESTART
                pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y1), (rst_box_x2, game_button_box_y1), 8)
                pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y2), (rst_box_x2, game_button_box_y2), 8)
                pygame.draw.line(screen, BLACK, (rst_box_x1, game_button_box_y1), (rst_box_x1, game_button_box_y2), 8)
                pygame.draw.line(screen, BLACK, (rst_box_x2, game_button_box_y1), (rst_box_x2, game_button_box_y2), 8)
                restart_font = pygame.font.Font(None, 60)
                restart_surf = restart_font.render("RESTART", True, BLACK, BG_COLOR)
                restart_rect = restart_surf.get_rect(center=(
                ((rst_box_x2 - rst_box_x1) / 2 + rst_box_x1), ((game_button_box_y2 - game_button_box_y1) / 2 + game_button_box_y1)))
                screen.blit(restart_surf, restart_rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()
                        # RESTART
                        if x >= rst_box_x1 and x <= rst_box_x2 and y >= game_button_box_y1 and y <= game_button_box_y2:
                            game_lose = False
                            main_menu = True
                pygame.display.update()

if __name__ == "__main__":
    main()
    quit()