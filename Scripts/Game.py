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
        self.__picked = False
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

        # Handle clicks
        if self.__controls.leftClickPressed:
            pos = pygame.mouse.get_pos()

            # Get all sprites whose rect intersects with the mouse position
            clicked_sprites = [s for s in self.__clickables if s.rect.collidepoint(pos)]

            for sp in clicked_sprites:
                if sp is self.shovel and not self.__digging:
                    self.__digging = True

                if sp is self.rawDirt and self.__digging:
                    self.__dirtOnShovel = True

                if sp is self.sifter and not self.__picking:
                    # If we do not have the shovel and there is dirt, shake the sifter
                    if not self.__digging and self.sifter.hasDirt():
                        self.sifter.sift(1)

                        # Create gems or trash
                        rand = random.randint(0, 9)
                        if rand == 0:
                            pass
                        elif rand < 6:
                            self.trash = Trash.Trash()
                            self.__renderables.append(self.trash)

                            sievePos = self.sifter.getPosition()
                            self.trash.setPosition(sievePos[0] + 10, sievePos[1] + 10)

                            self.gem = None
                            self.__picking = True
                        else:
                            # Create new gem
                            self.gem = Gem.Gem()
                            self.__renderables.append(self.gem)

                            sievePos = self.sifter.getPosition()
                            self.gem.setPosition(sievePos[0] + 10, sievePos[1] + 10)

                            self.trash = None
                            self.__picking = True

                    # If we do have the shovel and it has dirt in it, place dirt in sifter
                    if self.__digging and self.__dirtOnShovel:
                        self.sifter.addDirt(1)
                        self.__dirtOnShovel = False

                    # If we don't have the shovel, shake the sifter
                    else:
                        self.__shakeSieveCount = min(self.__shakeSieveCount + 8, 24)

        if self.__digging:
            pos = pygame.mouse.get_pos()
            self.shovel.setPosition(pos[0] - 67, pos[1] - 112)

    # Game loop
    def __gameLoop(self):
        if self.__controls.rightClickPressed:
            if self.__digging:
                self.__digging = False
                self.__dirtOnShovel = False
                self.shovel.setPosition(1040, 80)

        if self.__controls.spaceKeyPressed:
            if self.trash is not None and self.__picking:
                self.__picking = False
                self.__renderables.remove(self.trash)
                self.trash = None

            if self.gem is not None and self.__picking:
                self.__picking = False
                gem = self.gem
                self.gem = None

                self.gemGrid.addGem(gem)

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
        self.rawDirt.loadImage("../imgs/rawDirt.png")
        self.rawDirt.setPosition(940, 504)
        self.__digging = False
        self.__renderables.append(self.rawDirt)
        self.__clickables.append(self.rawDirt)

        self.shovel = Objects.Renderable()
        self.shovel.loadImage("../imgs/tmp/shovel.png")
        self.shovel.setPosition(1040, 80)
        self.__renderables.append(self.shovel)
        self.__clickables.append(self.shovel)

        self.trash = None
        self.gem = None
