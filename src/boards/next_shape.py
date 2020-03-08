from src.values.config import BORDER_NEW_SHAPE, GREEN, PURPLE, RED, DARK_BLUE
from src.boards.media_and_image import Image


class NextShapeBoard:
    def __init__(self, shape, color, screen_for_new_shape):
        """
        :param shape: Фигура
        :param color: Цвет
        :param screen: Экран
        """
        self.shape = shape
        self.color = color
        self.size_cell = 20
        self.board_for_new_shape(screen_for_new_shape, BORDER_NEW_SHAPE)
        self.render(screen_for_new_shape, color, shape)

    def render(self, screen, color, shape):
        """
        Рендер поля
        :param screen: слой
        :param color: название спрайта
        :param shape: фигура
        :return:
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
        Отрисовка фигуры
        :param screen: слой
        :param color: название спрайта
        :param x: нахождение блока по Х
        :param y: нахождение блока по Y
        :param x_plus: отступ по X
        :param y_plus: отступ по Y
        :param shape: фигура
        """
        for i in range(4):
            self.cubes_for_new_shapes(screen, color, x, y, x_plus, y_plus, shape[i])

    def get_coord(self, x, y, x_plus, y_plus, pos):
        """
        Получение координат по пикселям
        :param x: нахождение блока по Х
        :param y: нахождение блока по Y
        :param x_plus: отступ по X
        :param y_plus: отступ по Y
        :param pos: положение фигуры
        """
        x = (pos[0] - x) * 20 + x_plus
        y = (pos[1] - y) * 20 + y_plus
        return (x, y)

    def cubes_for_new_shapes(self, screen, name, x, y, x_plus, y_plus, pos):
        """
        Отрисовка блока
        :param screen: слой
        :param name: название спрайта
        :param x: нахождение блока по Х
        :param y: нахождение блока по Y
        :param x_plus: отступ по X
        :param y_plus: отступ по Y
        :param pos: положение фигуры
        """
        image = Image().load_image_block(name)
        screen.blit(image, self.get_coord(x, y, x_plus, y_plus, pos))

    def board_for_new_shape(self, screen, name):
        """
        Рамка для фигуры
        :param screen: слой
        :param name: название спрайта
        """
        image = Image().load_image_boards(name, (120, 120))
        screen.blit(image, (0, 0))

