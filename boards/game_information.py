import pygame
import os
import random
from boards.next_shape import draw_text
from values.colors import COLORS
from boards.next_shape import NextShapeBoard
from boards.score import Score
from values.config import NEW_SHAPE_BOARD


class GameInformation():
    def __init__(self, score, screen2, screen_record, screen_next_shape, screen_score):
        self.screen2 = screen2
        self.screen_record = screen_record
        self.screen_next_shape = screen_next_shape
        self.draw_border_next_shape(screen2, NEW_SHAPE_BOARD)
        draw_text(screen2, random.choice(COLORS))
        Score(score, screen_record, screen_score, random.choice(COLORS))

    def next_shape_board(self, figure, block, screen):
        NextShapeBoard(figure, block, screen, self.screen_next_shape)

    def draw_border_next_shape(self, screen, name):
        image = self.load_image_border(name)
        screen.blit(image, (0, 0))

    def load_image_border(self, name):
        fullname = os.path.join('data/boards', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, (216, 416))
        return image


    def board_next_shape(self):
        """
        Отображение текста "Next".
        Проверка следующей фигуры.
        """
