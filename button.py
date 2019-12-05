import pygame
pygame.init()
class PG_Button:
    def __init__(self, col, x_coor, y_coor, base, height, txt=""):
        """ Inializes the board buttons.
        """
        self.col = col
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.base = base
        self.height = height
        self.txt = txt

    def draw(self, window):
        """Display the connect four grid with buttons.
        """
        pygame.draw.rect(window, self.col, (self.x_coor, self.y_coor, self.base, self.height))
        text = pygame.font.SysFont("comicsans", 30)
        label = text.render(self.txt, 1, (0,0,0))
        window.blit(label, (self.x_coor+(self.base//2)//2, self.y_coor+(self.height//2)//2))

    def mouse_over(self, position):
        """Places a disk of player over the grid at the given position.
        """
        if position[0] > self.x_coor and position[0] < self.x_coor + self.base:
            if position[1] > self.y_coor and position[1] < self.y_coor + self.height:
                return True
        return False





