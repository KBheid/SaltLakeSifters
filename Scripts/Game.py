import pygame
import Controls

# TODO: This should be a singleton class
class Game:
    # Constructor
    def __init__(self):
        # Initialize the pygame
        pygame.init()

        # Create window and set window properties
        self.size = 800, 600
        self.title = "Salt Lake Sifters"
        # TODO: Load the window icon
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        # TODO: Set the window icon

        # Initialize the control system
        self.__controls = Controls.Controls()

        # Initialize the game state
        self.__running = True

    # Main loop
    def mainLoop(self):
        while self.__running:
            self.__eventLoop()
            self.__gameLoop()
            self.__renderLoop()

    # Event loop
    def __eventLoop(self):
        self.__controls.update()
        if self.__controls.quitPressed:
            self.__running = False

    # Game loop
    def __gameLoop(self):
        pass

    # Render loop
    def __renderLoop(self):
        pass