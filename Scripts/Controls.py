import pygame


class Controls:
    def __init__(self):
        self.leftKeyPressed = False
        self.rightKeyPressed = False
        self.spaceKeyPressed = False
        self.quitPressed = False

        self.leftClickPressed = False
        self.rightClickPressed = False

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.leftClickPressed = True
                if event.button == 3:
                    self.rightClickPressed = True


    def _reset(self):
        self.leftKeyPressed = False
        self.rightKeyPressed = False
        self.spaceKeyPressed = False
        self.quitPressed = False

        self.leftClickPressed = False
        self.rightClickPressed = False
