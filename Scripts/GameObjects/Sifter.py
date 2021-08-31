import pygame.display
import Objects


class Sifter(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        # Set member variables
        self.__lastDirtCount = 0
        self.__dirtCount = 0
        self.dirt = None

        self.dirtS = Objects.Renderable()
        self.dirtS.loadImage("../imgs/Art imgs/Dirt_s.PNG")
        self.dirtS.image = pygame.transform.scale(self.dirtS.image, (400, 400))
        self.dirtS.setPosition(440, 184)

        self.dirtM = Objects.Renderable()
        self.dirtM.loadImage("../imgs/Art imgs/Dirt_m.PNG")
        self.dirtM.image = pygame.transform.scale(self.dirtM.image, (400, 400))
        self.dirtM.setPosition(440, 184)

        self.dirtL = Objects.Renderable()
        self.dirtL.loadImage("../imgs/Art imgs/Dirt_l.PNG")
        self.dirtL.image = pygame.transform.scale(self.dirtL.image, (400, 400))
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

        self.__updateImage()

    def hasDirt(self):
        return self.__dirtCount > 0

    def __updateImage(self):
        # Load new image only if dirtCount has changed
        if not self.__lastDirtCount == self.__dirtCount:
            if self.__dirtCount == 0:
                self.dirt = None
            if self.__dirtCount == 1:
                self.dirt = self.dirtS
            if self.__dirtCount == 2:
                self.dirt = self.dirtM
            if self.__dirtCount == 3:
                self.dirt = self.dirtL
