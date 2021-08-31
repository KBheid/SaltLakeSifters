import pygame.display
import Objects


class Sifter(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        # Set member variables
        self.__lastDirtCount = 0
        self.__dirtCount = 3

        self.dirtS = Objects.Renderable()
        self.dirtS.loadImage("../imgs/dirt_s.png")
        self.dirtS.setPosition(440, 184)

        self.dirtM = Objects.Renderable()
        self.dirtM.loadImage("../imgs/dirt_m.png")
        self.dirtM.setPosition(440, 184)

        self.dirtL = Objects.Renderable()
        self.dirtL.loadImage("../imgs/dirt_l.png")
        self.dirtL.setPosition(440, 184)


        self.loadImage("../imgs/Art imgs/Sifter.png")
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (600, 600))
        self.rect.size = 600, 600;

        # Set the X and Y positions to the center of the screen
        x, y = pygame.display.get_window_size()
        x = x / 2
        y = y / 2

        x -= self.rect.width / 2
        y -= self.rect.height / 2

        self.setPosition(340, 84)

    def moveRect(self):
        self.rect.topleft = 2000, 2000

    def resetRect(self):
        self.rect.topleft = 340, 84

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
