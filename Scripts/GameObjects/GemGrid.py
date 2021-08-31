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

    def addGem(self, gem):
        # TODO: Use id to determine which gem to add
        self.count += 1

        gem.image = gem.image.convert_alpha()
        gem.image = pygame.transform.scale(gem.image, (100, 100))
        pos = self.getPosition()
        count = self.count
        row = int((count - 1) / 2)
        column = int((count - 1) % 2)
        gem.setPosition(pos[0] + ((column + 1) * 100) - 50, pos[1] + ((row + 1) * 100) - 50)