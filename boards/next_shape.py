import pygame
from values.config import NEXT, BORDER_NEW_SHAPE, GREEN, PURPLE, RED, DARK_BLUE
from values.fonts import CALIBRI
from values.config import WHITE
import os


class NextShapeBoard():
    def __init__(self, shape, color, screen, screen4):
        """
        :param shape: Фигура
        :param color: Цвет
        :param screen: Экран
        """
        self.shape = shape
        self.color = color
        self.screen = screen
        self.size_cell = 20
        self.board_for_new_shape(screen4, BORDER_NEW_SHAPE)
        self.render(screen4, color, shape)

    def render(self, screen, color, shape):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        if color == GREEN:
            self.draw(screen, color, 5, 2, 20, 50, shape[1])
        elif color == PURPLE:
            self.draw(screen, color, 6, 2, 40, 40, shape[0])
        elif color == RED or color == DARK_BLUE:
            self.draw(screen, color, 5, 1, 30, 40, shape[0])
        else:
            self.draw(screen, color, 5, 2, 30, 40, shape[0])

    def draw(self, screen, color, x, y, x_plus, y_plus, shape):
        """
        Отрисовка каждой клетки
        :param color: Цвет клетки
        :param pos: позиция клетки
        """
        for i in range(4):
            self.cubes_for_new_shapes(screen, color, x, y, x_plus, y_plus, shape[i])

    def get_coord(self, x, y, x_plus, y_plus, pos):
        """
        Получение координат в пикселях
        :param pos: Координаты в клетках
        """
        x = (pos[0] - x) * 20 + x_plus
        y = (pos[1] - y) * 20 + y_plus
        return (x, y)

    def cubes_for_new_shapes(self, screen, name, x, y, x_plus, y_plus, pos):
        image = self.load_image_block(name)
        screen.blit(image, self.get_coord(x, y, x_plus, y_plus, pos))

    def board_for_new_shape(self, screen, name):
        image = self.load_image_border(name)
        screen.blit(image, (0, 0))

    def load_image_block(self, name):
        fullname = os.path.join('data/blocks', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, (20, 20))
        return image

    def load_image_border(self, name):
        fullname = os.path.join('data/boards', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, (120, 120))
        return image


def draw_text(screen, color):
    """
    Отрисовка текста следующей фигуры
    :param screen: Экран
    :param color: Цвет
    """
    # try:
    #     text = pygame.font.SysFont(CALIBRI, 40, True).render(NEXT, 0, color)
    # except Exception:
    text = pygame.font.Font(None, 50).render(NEXT, 0, color)
    screen.blit(text, (65, 10))