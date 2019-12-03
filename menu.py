import pygame
from button import *
import board_view

NUM_COLS = 7
NUM_ROWS = 6
BLOCK = 80

WIDTH = NUM_COLS * BLOCK
HEIGHT = (NUM_ROWS+1) * BLOCK

PURPLE = [255, 0, 255]
BLUE = [0, 0, 255]
pygame.init()
# create game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")
pygame.display.update()
on = True
# window loop
if __name__ == "__main__":
    while on:
        window.fill((0, 0, 0))
        play = PG_Button(PURPLE, 250, 150, 100, 50, "Play")
        play.draw(window)
        instructions = PG_Button(PURPLE, 250, 250, 100, 50, "Instr")
        instructions.draw(window)

        if play.mouse_over(pygame.mouse.get_pos()):
            play.col = BLUE
            play.draw(window)
        if instructions.mouse_over(pygame.mouse.get_pos()):
            instructions.col = BLUE
            instructions.draw(window)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.mouse_over(pygame.mouse.get_pos()):
                    board_view.start()

        pygame.display.flip()
    pygame.quit()