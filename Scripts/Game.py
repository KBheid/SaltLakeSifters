import pygame
import sys
import Controls
import Objects


# TODO: This should be a singleton class
class Game:

    # Constructor
    def __init__(self):
        # Initialize the pygame
        pygame.init()

        # Create window and set window properties
        self.__size = 800, 600
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

        self.__startUp()

        self.__digging = False
        self.__sieving = False

    # Add a sprite to be rendered
    def addSprite(self, sprite):
        if sprite not in self.__renderables:
            self.__renderables.append(sprite)

    # Add a sprite to be clickable
    def addClickableSprite(self, sprite):
        if sprite not in self.__clickables:
            self.__clickables.append(sprite)

    # Main loop
    def mainLoop(self):
        while self.__running:
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


        # Handle clicks, set renderables to clicked
        # is the clickables cleared every frame?
        if self.__controls.leftClickPressed:
            pos = pygame.mouse.get_pos()

            # Get all sprites that rects intersect with the mouse position
            clicked_sprites = [s for s in self.__clickables if s.rect.collidepoint(pos)]

            for sp in clicked_sprites:
                print("The following sprite was clicked: %s" % sp)

            if self.rawDirt.rect.collidepoint(pos) and not self.__sieving:
                self.rawDirt.loadImage("../imgs/rawDirt.png")
                self.__digging = True

            if self.sieve.rect.collidepoint(pos):

                # dirt placed on sieve
                if self.__sieving:
                    self.__renderables.remove(self.dirt)
                    self.__sieving = False

                # rawDirt clicked
                if self.__digging:
                    self.dirt = Objects.Renderable()
                    self.dirt.loadImage("../imgs/dirt.png")
                    sievePos = self.sieve.getPosition()
                    self.dirt.setPosition(sievePos[0], sievePos[1])
                    self.__renderables.append(self.dirt)
                    self.__digging = False
                    self.__sieving = True

        if self.__digging:
            self.shovel = Objects.Renderable()
            self.shovel.loadImage("../imgs/shovel.png")
            pos = pygame.mouse.get_pos()
            self.shovel.setPosition(pos[0], pos[1])
        else:
            self.rawDirt.loadImage("../imgs/dirtWithShovel.png")


    # Game loop
    def __gameLoop(self):
        if self.__controls.spaceKeyPressed:
            print("test")

    # Render loop
    def __renderLoop(self):
        self.__window.fill((255, 255, 0))

        for object in self.__renderables:
            self.__window.blit(object.getImage(), object.getPosition())

        if self.__digging:
            self.__window.blit(self.shovel.getImage(), self.shovel.getPosition())

        pygame.display.update()

    def __startUp(self):
        self.sieve = Objects.Renderable()
        self.sieve.loadImage("../imgs/circle.png")
        self.sieve.setPosition(0, 0)
        self.__renderables.append(self.sieve)
        self.__clickables.append(self.sieve)

        self.rawDirt = Objects.Renderable()
        self.rawDirt.loadImage("../imgs/dirtWithShovel.png")
        self.rawDirt.setPosition(500, 0)
        self.__digging = False
        self.__renderables.append(self.rawDirt)
