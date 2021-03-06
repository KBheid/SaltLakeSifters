import GameObjects.Gem
import Objects
import pygame

class GemGrid(Objects.Renderable):
    def __init__(self):
        Objects.Renderable.__init__(self)

        self.loadImage("../imgs/Art imgs/plate.png", (450, 650))
        self.rect = self.image.get_rect()
        # self.count = 0

        self.setPosition(-50, 84)
        self.__gemList = [0, 0, 0, 0, 0]
        self.gemCountNumberList = [None, None, None, None, None]

    def getGemCountNumber(self, id) -> Objects.Renderable:
        font = pygame.freetype.Font("../fonts/IniyaDisplay-ow0Ra.otf", 50)
        text = font.render("x"+str(self.__gemList[id - 1]), 100)
        number = Objects.Renderable()
        number.image = text[0]

        pos = self.getPosition()
        row = id - 1
        column = 1
        number.setPosition(pos[0] + ((column + 1) * 225) - 180, pos[1] + ((row + 1) * 100) - 20)
        return number


    def addGem(self, gem) -> bool:
        # TODO: Use id to determine which gem to add
        # self.count += 1

        self.__gemList[gem.id - 1] += 1
        pygame.mixer.music.load("../sfx/pickGem.mp3")
        pygame.mixer.music.play()

        if self.__gemList[gem.id - 1] == 1:
            gem.image = gem.image.convert_alpha()
            gem.image = pygame.transform.scale(gem.image, (100, 100))
            pos = self.getPosition()
            # count = self.count
            # row = int((count - 1) / 2)
            # column = int((count - 1) % 2)
            # gem.setPosition(pos[0] + ((column + 1) * 100) - 50, pos[1] + ((row + 1) * 100) - 50)
            row = gem.id - 1
            column = 0
            gem.setPosition(pos[0] + ((column + 1) * 225) - 50, pos[1] + ((row + 1) * 100) - 50)
            return True

        return False

    def getGemNum(self, gem) -> int:
        return self.__gemList[gem.id - 1]