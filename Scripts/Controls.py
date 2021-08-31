import pygame


class Controls:
    def __init__(self):
        self.leftKeyPressed = False
        self.leftKeyHeld = False

        self.rightKeyPressed = False
        self.rightKeyHeld = False

        self.spaceKeyPressed = False
        self.spaceKeyHeld = False

        self.quitPressed = False
        self.quitHeld = False

        self.leftClickPressed = False
        self.leftClickHeld = False

        self.rightClickPressed = False
        self.rightClickHeld = False

    def update(self):
        self.reset()

        # Get the current events, set attributes. If they are already set, then do not set them to false.
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.leftKeyPressed = event.key == pygame.K_LEFT or self.leftKeyPressed
                self.leftKeyHeld = event.key == pygame.K_LEFT or self.leftKeyHeld

                self.rightKeyPressed = event.key == pygame.K_RIGHT or self.rightKeyPressed
                self.rightKeyHeld = event.key == pygame.K_RIGHT or self.rightKeyHeld

                self.spaceKeyPressed = event.key == pygame.K_SPACE or self.spaceKeyPressed
                self.spaceKeyHeld = event.key == pygame.K_SPACE or self.spaceKeyHeld

                self.quitPressed = event.key == pygame.K_ESCAPE or self.quitPressed
                self.quitHeld = event.key == pygame.K_ESCAPE or self.quitHeld

            if event.type == pygame.KEYUP:
                self.leftKeyHeld = False
                self.rightKeyHeld = False
                self.spaceKeyHeld = False
                self.quitHeld = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.leftClickHeld = True
                    self.leftClickPressed = True
                if event.button == 3:
                    self.rightClickHeld = True
                    self.rightClickPressed = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.leftClickHeld = False
                if event.button == 3:
                    self.rightClickHeld = False

    def reset(self):
        self.leftClickPressed = False
        self.rightClickPressed = False

        self.leftKeyPressed = False
        self.rightKeyPressed = False
        self.spaceKeyPressed = False

        self.quitPressed = False
