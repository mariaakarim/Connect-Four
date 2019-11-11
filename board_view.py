import pygame

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

pygame.display.init()

pygame.display.set_caption("CONNECT FOUR")
window = pygame.display.set_mode([WIDTH, HEIGHT],
    pygame.RESIZABLE)

exit_game = False

if __name__ == "__main__":
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        window.fill(YELLOW)
        pygame.draw.rect(window, WHITE, INPUT_BAR, 0)
        #fills board with white circles to represent empty slots in the game
        for col in range(NUM_COLS):
            for row in range(NUM_ROWS):
                circle = [(col*BLOCK) + BLOCK//2, (row*BLOCK)+ BLOCK + BLOCK//2]
                pygame.draw.circle(window, WHITE, circle, RADIUS)
        pygame.display.update()

    pygame.quit()
