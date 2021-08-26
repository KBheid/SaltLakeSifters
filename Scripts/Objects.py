import pygame


class Object:
    def __init__(self):
        pass


# Class for renderable objects
class Renderable(Object):
    def __init__(self):
        Object.__init__(self)
        self.__x = 0
        self.__y = 0
        self.__image = None

    # Load the player image
    def loadImage(self, path):
        self.__image = pygame.image.load(path)

    # Return the player image
    def image(self):
        return self.__image

    # Set the player's position
    def setPosition(self, x, y):
        self.__x = x
        self.__y = y

    # Return the player's position
    def getPosition(self):
        return self.__x, self.__y

    def move(self, xDif, yDif):
        newX, newY = self.__getPosition()
        newX += xDif
        newY += yDif
        self.__setPosition(newX, newY)


# Class for non-renderable objects
class Nonrenderable(Object):
    def __init__(self):
        Object.__init__(self)
