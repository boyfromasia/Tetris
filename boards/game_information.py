import pygame
import os
import random
from boards.next_shape import draw_text
from values.colors import COLORS
from boards.next_shape import NextShapeBoard
from boards.score import Score


class GameInformation():
    def __init__(self, score, screen2, screen3):
        self.screen2 = screen2
        self.screen3 = screen3
        draw_text(screen2, random.choice(COLORS))
        Score(score, screen3, random.choice(COLORS))

    def next_shape_board(self, figure, block, screen):
        NextShapeBoard(figure, block, screen)

    def draw_border_next_shape(self, screen, name):
        image = self.load_image_border(name)
        screen.blit(image, (0, 0))

    def load_image_border(self, name):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        image = pygame.transform.scale(image, (216, 416))
        return image

    def board_next_shape(self):
        """
        Отображение текста "Next".
        Проверка следующей фигуры.
        """
        self.get_next_shape()