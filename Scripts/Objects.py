import pygame
import pygame.sprite


class Object:
    def __init__(self):
        pass


# Class for renderable objects
class Renderable(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.__x = 0
        self.__y = 0
        
        self.image = None
        self.rect = None
        self.name = None

    # Load the player image
    def loadImage(self, path):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

    # Return the player image
    def getImage(self):
        return self.image

    # Set the player's position
    def setPosition(self, x, y):
        self.__x = x
        self.__y = y
        self.rect.x = x
        self.rect.y = y

    # Return the player's position
    def getPosition(self):
        return self.__x, self.__y

    def move(self, xDif, yDif):
        newX, newY = self.getPosition()
        newX += xDif
        newY += yDif
        self.setPosition(newX, newY)


# Class for non-renderable objects
class Nonrenderable(Object):
    def __init__(self):
        Object.__init__(self)
