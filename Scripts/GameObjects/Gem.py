import pygame
import pygame.freetype
import random
import Objects

class Gem(Objects.Renderable):
    def getRandomGemNum(self) -> int:
        # 1 Jade       5% 1~5
        # 2 Sapphire   15% 6~20
        # 3 blood Ruby 20% 21~40
        # 4 emerald    30% 41~70
        # 5 ruby       30% 71~100
        rand = random.randint(1, 100)
        gemNum = 5
        if rand < 6:
            gemNum = 1
        elif rand < 21:
            gemNum = 2
        elif rand < 41:
            gemNum = 3
        elif rand < 71:
            gemNum = 4
        return gemNum

    # def updateText(self, gem):

    def __init__(self):
        Objects.Renderable.__init__(self)

        self.id = self.getRandomGemNum()
        filename = "../imgs/Art imgs/Gems/gem" + str(self.id) + ".png"
        self.loadImage(filename)

