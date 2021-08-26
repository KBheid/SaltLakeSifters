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
        object = Objects.Renderable()
        object.loadImage("../imgs/circle.png")
        object.setPosition(0, 0)
        self.__renderables.append(object)

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

    # Game loop
    def __gameLoop(self):
        if self.__controls.spaceKeyPressed:
            print("test")

    # Render loop
    def __renderLoop(self):
        self.__window.fill((255, 255, 0))

        for object in self.__renderables:
            self.__window.blit(object.image(), object.getPosition())

        pygame.display.update()