# import the pygame module, so you can use it
import Game
import pygame.sprite


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
    game = Game.Game()
    game.mainLoop()


if __name__ == "__main__":
    main()
