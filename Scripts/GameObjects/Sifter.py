import pygame.display
import Game
import Objects


class Sifter(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        self.loadImage("../imgs/circle.png")

        # Set the X and Y positions to the center of the screen
        x, y = pygame.display.get_window_size()
        x = x / 2
        y = y / 2

        x -= self.rect.width / 2
        y -= self.rect.width / 2

        self.setPosition(x, y)
