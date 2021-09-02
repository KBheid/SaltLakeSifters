import pygame
import random
import Objects


class Trash(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        gemNum = random.randint(1, 5)
        filename = "../imgs/Art imgs/Trash/trash" + str(gemNum) + ".png"
        self.loadImage(filename)

        randscale = max(0.5, random.random())
        self.loadImage(filename, (int(self.rect.width * randscale), int(self.rect.height * randscale)))

        self.image = pygame.transform.rotate(self.image, random.randint(0, 3)*90)
