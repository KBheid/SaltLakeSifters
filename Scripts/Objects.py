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

    # Load the player image
    def loadImage(self, path, size=None):
        img = pygame.image.load(path)
        if size is not None:
            img = pygame.transform.scale(img, size)

        self.image = img
        self.rect = self.image.get_rect(topleft = (self.__x, self.__y))

    # Return the player image
    def getImage(self):
        return self.image

    # Set the player's position
    def setPosition(self, x, y):
        self.__x = x
        self.__y = y
        if self.rect is not None:
            self.rect.topleft = (self.__x, self.__y)

    # Return the player's position
    def getPosition(self):
        return self.__x, self.__y

    def getRect(self):
        return self.rect


# Class for non-renderable objects
class Nonrenderable(Object):
    def __init__(self):
        Object.__init__(self)
