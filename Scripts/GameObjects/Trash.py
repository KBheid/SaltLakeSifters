import pygame
import random
import Objects

class Trash(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        gemNum = random.randint(1, 5)
        filename = "../imgs/Art imgs/Trash/trash" + str(gemNum) + ".png"
        self.loadImage(filename)

