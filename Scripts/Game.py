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

        shovel = Objects.Renderable()
        shovel.loadImage("../imgs/shovel.png")

        dirtWithShovel = Objects.Renderable()
        dirtWithShovel.loadImage("../imgs/dirtWithShovel.png")
        dirtWithShovel.setPosition(500, 0)
        self.__renderables.append(dirtWithShovel)
        self.__clickables.append(dirtWithShovel)

        dirt = Objects.Renderable()
        dirt.loadImage("../imgs/dirt.png")
        dirt.setPosition(500, 0)

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
        if self.__controls.leftClickPressed:
            pos = pygame.mouse.get_pos()

            # Get all sprites that rects intersect with the mouse position
            clicked_sprites = [s for s in self.__clickables if s.rect.collidepoint(pos)]

            for sp in clicked_sprites:
                print("The following sprite was clicked: %s"%sp)

            # if dirtAndShovel is clicked:
            #     self.__renderables.remove(dirtWithShovel)


    # Game loop
    def __gameLoop(self):
        if self.__controls.spaceKeyPressed:
            print("test")

    # Render loop
    def __renderLoop(self):
        self.__window.fill((255, 255, 0))

        for object in self.__renderables:
            self.__window.blit(object.getImage(), object.getPosition())

        pygame.display.update()

    def __startUp(self):
        object = Objects.Renderable()
        object.loadImage("../imgs/circle.png")
        object.setPosition(0, 0)
        self.__renderables.append(object)
        self.__clickables.append(object)
