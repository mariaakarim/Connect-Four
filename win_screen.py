import pygame

pygame.init()
def display():
    """Display a screen declaring the winner of the game.
    """
    window = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Winner!")
    pygame.display.update()
    on = True
    while on:
        window.fill((0, 0, 0))
        text = pygame.font.SysFont("comicsans", 30)
        label = text.render("You win!", True, (0, 128, 0))
        window.blit(label, (110, 150))

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                on = False

        pygame.display.flip()
    pygame.quit()
