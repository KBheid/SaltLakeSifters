import Gem
import Objects
import pygame

class GemGrid(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        self.loadImage("../imgs/rectangle.png")

        x, y = pygame.display.get_window_size()
        x = x / 5
        y = y / 2

        x -= self.rect.width / 2
        y -= self.rect.height / 2

        self.setPosition(x, y)

    def addGem(self, id):
        pass