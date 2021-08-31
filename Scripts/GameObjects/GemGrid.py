import GameObjects.Gem
import Objects
import pygame

class GemGrid(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        self.image = pygame.Surface((300, 600))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.count = 0

        self.setPosition(20, 84)

    def addGem(self):
        # TODO: Use id to determine which gem to add
        self.count += 1
