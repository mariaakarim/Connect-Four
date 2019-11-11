import pygame
from board import *

NUM_COLS = 7
NUM_ROWS = 6
BLOCK = 80 # if one position in a 2D array was represented graphically as a
           # square this would be the size
WIDTH = NUM_COLS * BLOCK
HEIGHT = (NUM_ROWS+1) * BLOCK # adding plus one so we can fit the input bar
RADIUS = 35
INPUT_BAR = [0, 0, NUM_COLS*BLOCK, RADIUS*2]
YELLOW = [255, 255, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
PURPLE = [255, 0, 255]

pygame.display.init()

pygame.display.set_caption("CONNECT FOUR")
window = pygame.display.set_mode([WIDTH, HEIGHT],
    pygame.RESIZABLE)

exit_game = False
game_board = Board(NUM_ROWS, NUM_COLS)

def draw_player1_disk(row, col):
    circle = [(col*BLOCK) + BLOCK//2, (row*BLOCK)+ BLOCK + BLOCK//2]
    pygame.draw.circle(window, RED, circle, RADIUS)

def draw_player2_disk(row, col):
    circle = [(col*BLOCK) + BLOCK//2, (row*BLOCK)+ BLOCK + BLOCK//2]
    pygame.draw.circle(window, YELLOW, circle, RADIUS)

def draw_empty_disk(row, col):
    circle = [(col*BLOCK) + BLOCK//2, (row*BLOCK)+ BLOCK + BLOCK//2]
    pygame.draw.circle(window, WHITE, circle, RADIUS)

def display_board():
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS):
            if game_board.board[row, col] == 1:
                draw_player1_disk(row, col)
            elif game_board.board[row, col] == 2:
                draw_player2_disk(row, col)
            else:
                draw_empty_disk(row, col)


if __name__ == "__main__":
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        window.fill(PURPLE)
        pygame.draw.rect(window, WHITE, INPUT_BAR, 0)
        #fills board with white circles to represent empty slots in the game
        display_board()

        pygame.display.update()

    pygame.quit()
