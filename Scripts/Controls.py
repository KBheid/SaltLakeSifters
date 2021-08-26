import pygame

class Controls:
    def __init__(self):
        self.leftKeyPressed = False
        self.rightKeyPressed = False
        self.spaceKeyPressed = False
        self.quitPressed = False

    def update(self):
        # Reset from last update
        self._reset()

        # Get the current events, set attributes. If they are already set, then do not set them to false.
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.leftKeyPressed = event.key == pygame.K_LEFT or self.leftKeyPressed
                self.rightKeyPressed = event.key == pygame.K_RIGHT or self.rightKeyPressed
                self.spaceKeyPressed = event.key == pygame.K_SPACE or self.spaceKeyPressed
                self.quitPressed = event.key == pygame.K_ESCAPE or self.quitPressed

    def _reset(self):
        self.leftKeyPressed = False
        self.rightKeyPressed = False
        self.spaceKeyPressed = False
        self.quitPressed = False