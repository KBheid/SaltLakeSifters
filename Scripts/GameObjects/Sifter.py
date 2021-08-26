import pygame.display
import Objects


class Sifter(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        # Set member variables
        self.__lastDirtCount = 0
        self.__dirtCount = 3

        self.loadImage("../imgs/tmp/sieve%d.png"%self.__dirtCount)

        # Set the X and Y positions to the center of the screen
        x, y = pygame.display.get_window_size()
        x = x / 2
        y = y / 2

        x -= self.rect.width / 2
        y -= self.rect.width / 2

        self.setPosition(x, y)

    def addDirt(self, amount):
        self.__lastDirtCount = self.__dirtCount
        self.__dirtCount += amount
        if self.__dirtCount > 3:
            self.__dirtCount = 3
            return

        self.__updateImage()

    def sift(self, amount):
        self.__lastDirtCount = self.__dirtCount
        self.__dirtCount -= amount
        if self.__dirtCount < 0:
            self.__dirtCount = 0
            return

        # TODO: Create gems

        self.__updateImage()

    def __updateImage(self):
        # Load new image only if dirtCount has changed
        if not self.__lastDirtCount == self.__dirtCount:
            self.loadImage("../imgs/tmp/sieve%d.png" % self.__dirtCount)
