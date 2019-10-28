import pygame

GAME_WINDOW_HEIGHT = 750
GAME_WINDOW_WIDTH = 600

pygame.display.init()

pygame.display.set_caption("CONNECT FOUR")
window = pygame.display.set_mode([GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT],
    pygame.RESIZABLE)

yellow = [255, 255, 0]
exit_game = False

#pygame.draw.circle(window, (0,0, 255), (450, 450), 20, 2)
if __name__ == "__main__":
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        window.fill(yellow)
        #fills board with white circles to represent empty slots in the game
        for i in range(50, 600, 100):
            for j in range(100, 800, 100):
                pygame.draw.circle(window, (255, 255, 255), (i, j), 35, 0)
        
        pygame.display.update()

    pygame.quit()
