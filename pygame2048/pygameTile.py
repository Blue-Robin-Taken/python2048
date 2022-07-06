import os.path
import pathlib

import pygame
import random

pygame.init()


class TwentyFortyEightTile(pygame.sprite.Sprite):
    def __init__(self, number, position):
        super().__init__()
        self.image = pygame.surface.Surface((100, 100))
        self.rect = self.image.get_rect()
        self.number = number
        self.x = position[0]
        self.y = position[1]
        random.seed(number)
        if number == "⬜":
            color = (0, 0, 0)
        else:
            colorList = [(128, 0, 0), (139, 0, 0), (165, 42, 42), (178, 34, 34), (220, 20, 60), (255, 0, 0), (255, 99, 71),
                         (255, 127, 80), (205, 92, 92), (240, 128, 128), (233, 150, 122), (250, 128, 114), (255, 160, 122),
                         (255, 69, 0), (255, 140, 0), (255, 165, 0), (255, 215, 0), ]
            color = colorList[random.randrange(0, len(colorList))]
            self.image.fill(color)
        self.rect.x = self.x * self.image.get_width()
        self.rect.y = self.y * self.image.get_height()

        font = pygame.font.Font(
            os.path.relpath("Fonts/Dosis,VT323/Dosis/static/Dosis-Bold.ttf"),
            30)
        text = font.render(str(self.number), True, (0, 0, 0))
        self.image.blit(text, (
            self.image.get_width() / 2 - text.get_width() / 2, self.image.get_height() / 2 - text.get_height() / 2))

    def kill(self):
        self.kill()


class pygameText(pygame.font.Font):
    def __init__(self, number, position):
        super().__init__()
        self.render(str(self.number), True, (0, 0, 0))
