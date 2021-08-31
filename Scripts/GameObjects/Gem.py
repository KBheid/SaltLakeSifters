import pygame
import random
import Objects

class Gem(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        gemNum = random.randint(1, 5)
        filename = "../imgs/Art imgs/Gems/gem" + str(gemNum) + ".png"
        self.loadImage(filename)

