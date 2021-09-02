import math

import pygame
import sys
import time # Used for ensuring that frames occur every X milliseconds
import Controls
import Objects
import random
from GameObjects import Sifter, GemGrid, Gem, Trash


# The framerate that the game runs at
FRAMERATE = 60


# TODO: This should be a singleton class
class Game:

    # Constructor
    def __init__(self):
        # Initialize the pygame
        pygame.init()

        # Create window and set window properties
        self.__size = 1280, 768
        self.__title = "Salt Lake Sifters"
        # TODO: Load the window icon
        self.__window = pygame.display.set_mode(self.__size)
        pygame.display.set_caption(self.__title)
        # TODO: Set the window icon

        # Initialize the control system
        self.__controls = Controls.Controls()

        # Initialize the game state
        self.__running = True

        # Initialize the renderable objects queue
        self.__renderables = []
        self.__clickables = []

        self.__digging = False
        self.__dirtOnShovel = False
        self.__sieving = False
        self.__picking = False
        self.__dragging = False
        self.__shakeSieveCount = 0
        self.__dirtCount = 0

        self.__startUp()

    # Add a sprite to be rendered
    def addSprite(self, sprite):
        if sprite not in self.__renderables:
            self.__renderables.append(sprite)

    # Add a sprite to be clickable
    def addClickableSprite(self, sprite):
        if sprite not in self.__clickables:
            self.__clickables.append(sprite)

    def shakeSifter(self):
        if self.__shakeSieveCount <= 0:
            return

        pos = self.sifter.getPosition()
        bia = 20
        bia = -bia if ( self.__shakeSieveCount % 2 == 0 ) else bia
        self.sifter.setPosition(pos[0] + bia, pos[1])
        self.__shakeSieveCount -= 1

    # Main loop
    def mainLoop(self):
        elapsedTime = 0
        lastTime = time.time()

        while self.__running:
            curTime = time.time()
            elapsedTime = curTime - lastTime

            if elapsedTime >= 1/FRAMERATE:
                elapsedTime = 0
                lastTime = curTime

                self.__eventLoop()
                self.__gameLoop()
                self.__renderLoop()

        pygame.quit()
        sys.exit()

    # Event loop
    def __eventLoop(self):
        self.__controls.update()
        if self.__controls.quitPressed:
            self.__running = False

        if self.__controls.spaceKeyPressed:
            if self.sifter.hasDirt() and not self.__picking:
                self.sifter.sift(1)

                # Create gems or trash
                #   [1-5] trash
                #   [0, 6-9] treasure
                rand = random.randint(0, 9)
                if 0 < rand < 6:
                    self.trash = Trash.Trash()
                    self.__renderables.append(self.trash)
                    self.__clickables.append(self.trash)
                    self.trash.setPosition(350, 95)

                    self.gem = None
                    self.__picking = True
                else:
                    # Create new gem
                    self.gem = Gem.Gem()
                    self.gem.image = pygame.transform.scale(self.gem.image, (100, 100))
                    self.__renderables.append(self.gem)
                    self.__clickables.append(self.gem)

                    self.gem.setPosition(590, 285)

                    self.trash = None
                    self.__picking = True

                # Shake the sifter
                self.__shakeSieveCount = min(self.__shakeSieveCount + 8, 24)

        # Handle clicks
        if self.__controls.leftClickPressed:
            pos = pygame.mouse.get_pos()

            # Get all sprites whose rect intersects with the mouse position
            clicked_sprites = [s for s in self.__clickables if s.rect.collidepoint(pos)]

            for sp in clicked_sprites:
                if sp is self.shovel:
                    self.__digging = True

                if self.__picking and sp is self.gem or sp is self.trash:
                    self.__dragging = True

        if self.__dragging:
            pos = pygame.mouse.get_pos()
            if self.gem is not None:
                self.gem.setPosition(pos[0] - self.gem.image.get_rect().width/2, pos[1] - self.gem.image.get_rect().height/2)
            if self.trash is not None:
                self.trash.setPosition(pos[0] - 170, pos[1] - 200)

        # If the player was digging and is no longer holding left click, they are no longer digging
        if self.__digging and not self.__controls.leftClickHeld:
            self.__digging = False
            self.__dirtOnShovel = False
            self.shovel.loadImage("../imgs/Art imgs/shovel.png")
            self.shovel.image = pygame.transform.scale(self.shovel.image, (180, 241))
            self.shovel.setPosition(1040, 80)

        # HANDLE MOTION WITHOUT CLICKING
        pos = pygame.mouse.get_pos()
        if self.sifter.rect.collidepoint(pos) and self.__digging and self.__dirtOnShovel:
            self.sifter.addDirt(1)
            self.shovel.loadImage("../imgs/Art imgs/shovel.png")
            self.shovel.image = pygame.transform.scale(self.shovel.image, (180, 241))
            self.__dirtOnShovel = False

        if self.rawDirt.rect.collidepoint(pos[0], pos[1]+50) and self.__digging:
            self.shovel.loadImage("../imgs/Art imgs/shovel_with_dirt.png")
            self.shovel.image = pygame.transform.scale(self.shovel.image, (180, 241))
            self.__dirtOnShovel = True


        # Update shovel position to match mouse if digging
        if self.__digging:
            pos = pygame.mouse.get_pos()
            self.shovel.setPosition(pos[0] - 67, pos[1] - 112)

    # Game loop
    def __gameLoop(self):

        if self.__dragging and not self.__controls.leftClickHeld:
            self.__dragging = False
            pos = pygame.mouse.get_pos()
            if self.gemGrid.rect.collidepoint(pos):
                if self.gem is not None:
                    self.__picking = False
                    gem = self.gem
                    self.__clickables.remove(self.gem)
                    self.gem = None

                    # a duplicated gem, once picked, doesn't really exist
                    if not self.gemGrid.addGem(gem):
                        self.__renderables.remove(gem)
                        number = self.gemGrid.getGemCountNumber(gem.id)
                        # keep track of the numbers
                        previousNum = self.gemGrid.gemCountNumberList[gem.id - 1]
                        if previousNum is not None:
                            self.__renderables.remove(previousNum)
                        self.gemGrid.gemCountNumberList[gem.id - 1] = number
                        self.__renderables.append(number)
                if self.trash is not None:
                    self.trash.setPosition(350, 95)
            elif self.sifter.rect.collidepoint(pos) and self.trash is not None:
                self.trash.setPosition(350, 95)
            else:
                if self.gem is not None:
                    self.gem.setPosition(590, 285)
                if self.trash is not None:
                    self.__picking = False
                    self.__renderables.remove(self.trash)
                    self.__clickables.remove(self.trash)
                    self.trash = None

        # If it needs to be shaken, shake it
        self.shakeSifter()

    # Render loop
    # ORDER MATTERS
    def __renderLoop(self):
        self.__window.fill((206, 237, 239))

        self.__window.blit(self.sifter.getImage(), self.sifter.getPosition())

        if self.sifter.dirt is not None:
            self.__window.blit(self.sifter.dirt.getImage(), self.sifter.dirt.getPosition())

        for object in self.__renderables:
            self.__window.blit(object.getImage(), object.getPosition())

        pygame.display.update()

    def __startUp(self):
        self.sifter = Sifter.Sifter()
        self.__clickables.append(self.sifter)

        self.gemGrid = GemGrid.GemGrid()
        self.__renderables.append(self.gemGrid)
        self.__clickables.append(self.gemGrid)

        self.rawDirt = Objects.Renderable()
        self.rawDirt.loadImage("../imgs/Art imgs/Dirt_pile.png", (400, 400))
        self.rawDirt.setPosition(850, 400)
        self.rawDirt.rect = pygame.Rect(self.rawDirt.rect.left+150, self.rawDirt.rect.top+125, 175, 100)
        self.__digging = False
        self.__renderables.append(self.rawDirt)
        self.__clickables.append(self.rawDirt)

        self.shovel = Objects.Renderable()
        self.shovel.loadImage("../imgs/Art imgs/shovel.png")
        self.shovel.image = pygame.transform.scale(self.shovel.image, (180, 241))
        self.shovel.setPosition(1040, 80)
        self.__renderables.append(self.shovel)
        self.__clickables.append(self.shovel)

        self.trash = None
        self.gem = None