import GameObjects.Gem
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

        self.gems = []
        self.addGem()
        self.addGem()
        self.addGem()
        self.addGem()
        self.addGem()
        self.addGem()
        self.addGem()
        self.addGem()

    def addGem(self):
        # TODO: Use id to determine which gem to add
        gem = GameObjects.Gem.Gem()
        gem.loadImage("../imgs/gems.png")
        self.gems.append(gem)

        length = len(self.gems)
        row = int((length - 1) / 2)
        column = int((length - 1) % 2)
        vOffset = (self.rect.height - 20 - (10 * 4)) / 5
        hOffset = (self.rect.width - 20 - (65 * 2)) / 3

        x, y = self.getPosition()
        gemX = x + 10 + (column + 1) * hOffset
        gemY = y + 10 + (row + 1) * vOffset

        gem.setPosition(gemX, gemY)
