import pygame

GAME_WINDOW_HEIGHT = 500
GAME_WINDOW_WIDTH = 600

pygame.display.init()

pygame.display.set_caption("CONNECT FOUR")
window = pygame.display.set_mode([GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT],
    pygame.RESIZABLE)

yellow = [255, 255, 0]
exit_game = False


if __name__ == "__main__":
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        window.fill(yellow)
        pygame.display.update()

    pygame.quit()
