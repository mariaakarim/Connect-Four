import pygame
from button import *
import board_view

PURPLE = [255, 0, 255]
BLUE = [0, 0, 255]
pygame.init()

# create game window
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Main Menu")
pygame.display.update()
on = True

# window loop
def start_game():
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
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.mouse_over(pygame.mouse.get_pos()):
                    board_view.start()
                    pygame.quit()
                    on = False
                    break
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    start_game()
