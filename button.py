import pygame
pygame.init()
class PG_Button:
    def __init__(self, col, x_coor, y_coor, base, height, txt=""):
        self.col = col
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.base = base
        self.height = height
        self.txt = txt
    def draw(self, window):
        pygame.draw.rect(window, self.col, self.x_coor, self.y_coor, self.base, self.height)

    def mouse_over(self, position):
        if position[0] > self.x_coor and position[0] < self.x_coor + self.base:
            if position[1] > self.y_coor and position[1] < self.y + self.height:
                return True
        return False



