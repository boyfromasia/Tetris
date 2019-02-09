import pygame
from values.config import NEXT, NEW_SHAPE_BOARD
from values.fonts import CALIBRI
from values.config import WHITE
import os


class NextShapeBoard():
    def __init__(self, shape, color, screen):
        """
        :param shape: Фигура
        :param color: Цвет
        :param screen: Экран
        """
        self.shape = shape
        self.color = color
        self.screen = screen
        self.size_cell = 20
        self.cells = [[-1] * 7 for _ in range(7)]
        for i in range(4):
            self.cells[shape[i][1] + 1][shape[i][0] - 3] *= -1
        self.draw_border_next_shape(screen, NEW_SHAPE_BOARD)
        self.render(screen, color)

    def render(self, screen, color):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j] == -1:
                    self.draw(self.get_coord((j, i)), screen, WHITE)
                else:
                    if self.cells[i][j] == 1:
                        self.draw(self.get_coord((j, i)), screen, color)

    def draw(self, pos, screen, color):
        """
        Отрисовка каждой клетки
        :param color: Цвет клетки
        :param pos: позиция клетки
        """
        image = self.load_image_block(color)
        screen.blit(image, pos)

    def get_coord(self, pos):
        """
        Получение координат в пикселях
        :param pos: Координаты в клетках
        """
        x = pos[0] * 20 + 40
        y = pos[1] * 20 + 40
        return (x, y)

    def load_image_block(self, name):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        image = pygame.transform.scale(image, (20, 20))
        return image

    def draw_border_next_shape(self, screen, name):
        image = self.load_image_border(name)
        screen.blit(image, (0, 0))

    def load_image_border(self, name):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        image = pygame.transform.scale(image, (216, 416))
        return image


def draw_text(screen, color):
    """
    Отрисовка текста следующей фигуры
    :param screen: Экран
    :param color: Цвет
    """
    try:
        text = pygame.font.SysFont(CALIBRI, 40, True).render(NEXT, 0, color)
    except Exception:
        text = pygame.font.Font(None, 50).render(NEXT, 0, color)
    screen.blit(text, (27, 0))