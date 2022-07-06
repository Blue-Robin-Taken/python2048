import main  # main folder
from main import main as mainGame  # main.py
import sys
import pygame
import pygameTile

pygame.init()
pygame.display.set_caption("Pygame 2048")
# --- Variables ---
twentyfortyeight = mainGame.TwentyFortyEight(False)
screen = pygame.display.set_mode((640, 480))


# --- Functions ---
def getBoard():
    tileGroup = pygame.sprite.Group()
    for y in range(4):
        for x in range(4):
            numberTile = pygameTile.TwentyFortyEightTile(twentyfortyeight.boardList[y][x], (x, y))
            tileGroup.add(numberTile)

    return tileGroup


def refreshBoard(prevBoard):
    prevBoard.empty()
    board = getBoard()

    return board


# --- Main game loop ---
def loop():
    group = getBoard()
    alive = True
    while alive:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('Key Left')
                    twentyfortyeight.Left()
                if event.key == pygame.K_RIGHT:
                    print("Key Right")
                    twentyfortyeight.Right()
                if event.key == pygame.K_DOWN:
                    print("Key Down")
                    twentyfortyeight.Down()
                if event.key == pygame.K_UP:
                    print("Key Up")
                    twentyfortyeight.Up()
                group = refreshBoard(group)

        alive = not twentyfortyeight.dead
        screen.fill((255, 255, 255))  # fill background color
        group.update()
        group.draw(screen)

        pygame.display.flip()


loop()
