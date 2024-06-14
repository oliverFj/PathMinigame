import pygame
import sys
from game import Game

def main():
    print("Programmet starter")
    pygame.init()
    game = Game()
    print("Spil instans oprettet")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Spillet starter")
                    game.start()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        game.update()
        game.draw()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
