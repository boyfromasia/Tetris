import pygame


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
        self.render(screen, color)

    def render(self, screen, color):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j] == -1:
                    self.draw(self.get_coord((j, i)), screen, (255, 255, 255))
                else:
                    if self.cells[i][j] == 1:
                        self.draw(self.get_coord((j, i)), screen, color)
        pygame.draw.polygon(screen, (255, 0, 0), ((0, 40), (138, 40), (138, 178), (0, 178)), 5)

    def draw(self, pos, screen, color):
        """
        Отрисовка каждой клетки
        :param color: Цвет клетки
        :param pos: позиция клетки
        """
        pygame.draw.polygon(screen, color, ((pos[0], pos[1]),
                                            (pos[0] + self.size_cell, pos[1]),
                                            (pos[0] + self.size_cell, pos[1] + self.size_cell),
                                            (pos[0], pos[1] + self.size_cell)))
        pygame.draw.polygon(screen, (255, 245, 238), ((pos[0], pos[1]),
                                            (pos[0] + self.size_cell, pos[1]),
                                            (pos[0] + self.size_cell, pos[1] + self.size_cell),
                                            (pos[0], pos[1] + self.size_cell)), 1)

    def get_coord(self, pos):
        """
        Получение координат в пикселях
        :param pos: Координаты в клетках
        """
        x = pos[0] * 20
        y = pos[1] * 20 + 40
        return (x, y)


def draw_text(screen, color):
    """
    Отрисовка текста следующей фигуры
    :param screen: Экран
    :param color: Цвет
    """
    text = pygame.font.Font(None, 50).render("Next", 0, color)
    screen.blit(text, (30, 0))