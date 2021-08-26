# import the pygame module, so you can use it
import Game


game = None

def main():
    global game

    game = Game.Game()
    game.mainLoop()


if __name__ == "__main__":
    main()
