import pygame
from board import Board
from colors import *
import win_screen

NUM_COLS = 7
NUM_ROWS = 6
BLOCK = 80 # if one position in a 2D array was represented graphically as a
           # square this would be the size

WIDTH = NUM_COLS * BLOCK
HEIGHT = (NUM_ROWS+1) * BLOCK # adding plus one so we can fit the input bar
RADIUS = 35 # radius of circles on the board

INPUT_BAR = [0, 0, NUM_COLS*BLOCK, RADIUS*2] # bar to show what column user is
                                             # about to pick

GAME_BOARD = Board(NUM_ROWS, NUM_COLS)
pygame.font.init()
GAME_FONT = pygame.font.SysFont("comicsansms", 50)

pygame.display.init()

pygame.display.set_caption("CONNECT FOUR")
window = pygame.display.set_mode([WIDTH, HEIGHT], 0)

def print_on_input_bar(sentence):
    """Display the sentence on the board's title bar."""
    text = GAME_FONT.render(sentence, 1, RED)
    window.blit(text, [40, 10])
    pygame.display.update()
    pygame.time.wait(2000)

def draw_player1_disk(row, col):
    """Place Player Ones disk on the board.
    """
    circle = [(col*BLOCK) + BLOCK//2, (row*BLOCK) + BLOCK + BLOCK//2]
    pygame.draw.circle(window, RED, circle, RADIUS)


def draw_player2_disk(row, col):
    """Place Player Twos disk on the board.
    """
    circle = [(col*BLOCK) + BLOCK//2, (row*BLOCK)+ BLOCK + BLOCK//2]
    pygame.draw.circle(window, YELLOW, circle, RADIUS)


def draw_empty_disk(row, col):
    """Place white circles on the board to display empty spots.
    """
    circle = [(col*BLOCK) + BLOCK//2, (row*BLOCK)+ BLOCK + BLOCK//2]
    pygame.draw.circle(window, WHITE, circle, RADIUS)


def display_board():
    """Display connect four board.
    """
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS):
            if GAME_BOARD.board[row, col] == 1:
                draw_player1_disk(row, col)
            elif GAME_BOARD .board[row, col] == 2:
                draw_player2_disk(row, col)
            else:
                draw_empty_disk(row, col)


def start():
    """Start a new game of connect four.
    """
    exit_game = False
    turn = 1  # represent which player's turn it is
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            # display disc about to be dropped in INPUT bar
            if event.type == pygame.MOUSEMOTION:
                coord_x = event.pos[0]
                sel_col = coord_x//BLOCK
                if turn == 1:
                    draw_player1_disk(-1, sel_col)
                else:
                    draw_player2_disk(-1, sel_col)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos[0]  # the x coordinate
                sel_col = pos // BLOCK  # scale it to one block in the array
                row = GAME_BOARD.get_next_open_row(sel_col)
                if row is None:
                    print_on_input_bar("This column is full");
                    exit_game = True
                else:
                    if turn == 1:
                        GAME_BOARD.place_disk(row, sel_col, 1)
                        display_board()
                        if GAME_BOARD.check_winner(1, row, sel_col):
                            print_on_input_bar("Player 1 wins!")
                            win_screen.display()
                            exit_game = True

                        turn = 2
                        pygame.display.update()
                    elif turn == 2:
                        GAME_BOARD.place_disk(row, sel_col, 2)
                        display_board()
                        if GAME_BOARD.check_winner(2, row, sel_col):
                            print_on_input_bar("Player 2 wins!")
                            win_screen.display()
                            exit_game = True

                        turn = 1
                        pygame.display.update()

        window.fill(PURPLE)
        pygame.draw.rect(window, WHITE, INPUT_BAR, 0)
        # fills board with white circles to represent empty slots in the game
        display_board()

    pygame.quit()
