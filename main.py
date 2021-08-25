# import the pygame module, so you can use it
import pygame
import pygame.sprite


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
                self.quitPressed = event.key == pygame.QUIT or self.quitPressed

    def _reset(self):
        self.leftKeyPressed = False
        self.rightKeyPressed = False
        self.spaceKeyPressed = False
        self.quitPressed = False


class GameState:
    def __init__(self):
        self.renderables = []
        self.controls = Controls()


def eventLoop(gameState):
    gameState.controls.update()


def gameLoop(gameState):
    if gameState.controls.spaceKeyPressed:
        s = pygame.sprite.Sprite()
        s.image = pygame.image.load("./imgs/jump.png").convert()
        s.rect = s.image.get_rect()
        gameState.renderables.append(s)


def renderLoop(gameState, screen):
    # TODO: For some reason, they are not rendered. Probably because I haven't looked into how sprites work at all...
    for renderable in gameState.renderables:
        screen.blit(renderable.image, renderable.rect)


def main():
    gameState = GameState()

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("./imgs/jump.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # The screen is where all rendering takes place
    screen = pygame.display.set_mode((1000, 300))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # Event loop, where events like key presses or collisions get set
        eventLoop(gameState)
        if gameState.controls.quitPressed:
            running = False

        # Game loop, where all game logic happens
        gameLoop(gameState)

        # Render loop, where all rendering takes place
        renderLoop(gameState, screen)


if __name__ == "__main__":
    main()
