import pygame
import random

direction = 0
step_x = 0
step_y = 0
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
I = ([[6, 0], [6, 1], [6, 2], [6, 3]], [[5, 2], [6, 2], [7, 2], [8, 2]], [[6, 2], [6, 1], [6, 3], [6, 4]], [[6, 2], [5, 2], [4, 2], [7, 2]])
L_L = ([[6, 3], [6, 1], [6, 2], [7, 3]], [[5, 3], [6, 3], [7, 3], [7, 2]], [[5, 1], [6, 1], [6, 2], [6, 3]], [[5, 3], [5, 2], [6, 2], [7, 2]])
L_R = ([[6, 3], [6, 2], [6, 1], [5, 3]], [[5, 3], [6, 3], [7, 3], [7, 2]], [[5, 1], [6, 1], [6, 2], [6, 3]], [[5, 3], [5, 2], [6, 2], [7, 2]])
W = ([[6, 2], [6, 3], [7, 3], [5, 3]], [[6, 3], [6, 2], [6, 1], [7, 2]], [])
Q = [[6, 3], [7, 3], [6, 2], [7, 2]]
Z_R = [[6, 3], [7, 3], [5, 2], [6, 2]]
Z_L = [[6, 3], [5, 3], [6, 2], [7, 2]]


shapes = [I]
new_shape = True
save_coord = []


class Board:
    def __init__(self):
        """
        Инициализация матрицы игры
        """
        self.cells = [[0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0] if x != 0 and x != 1 and x != 2 and x != 23 else
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(24)]
        self.size_cell = 20

    def render(self, screen):
        """
        Рендер поля
        """
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                self.draw(self.cells[i][j], self.get_coord((j, i)), screen)

    def draw(self, cell, pos, screen):
        """
        Отрисовка каждой клетки
        :param cell: значение клетки
        :param pos: позиция клетки
        """
        if cell == -1:
            pygame.draw.polygon(screen, white, ((pos[0], pos[1]),
                                                  (pos[0] + self.size_cell, pos[1]),
                                                  (pos[0] + self.size_cell, pos[1] + self.size_cell),
                                                  (pos[0], pos[1] + self.size_cell)))
        elif cell == 1:
            pygame.draw.polygon(screen, red, ((pos[0], pos[1]),
                                                     (pos[0] + self.size_cell, pos[1]),
                                                     (pos[0] + self.size_cell, pos[1] + self.size_cell),
                                                     (pos[0], pos[1] + self.size_cell)))
        elif cell == 2:
            pygame.draw.polygon(screen, green, ((pos[0], pos[1]),
                                                     (pos[0] + self.size_cell, pos[1]),
                                                     (pos[0] + self.size_cell, pos[1] + self.size_cell),
                                                     (pos[0], pos[1] + self.size_cell)))

    def get_coord(self, cell):
        """
        Получение координат в пикселях
        :param cell: Координаты
        """
        x = cell[0] * self.size_cell
        y = cell[1] * self.size_cell
        return (x, y)

    def start(self, coords, screen):
        """
        Изменение значения в матрице. Начало Игры.
        :param coords: координаты
        """
        self.cells[coords[1]][coords[0]] *= -1
        self.render(screen)

    def refresh(self):
        """
        Возвращение измененных клеток в исходное положение.
        """
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j] == 0:
                    self.cells[i][j] = 0
                elif self.cells[i][j] == 1:
                    self.cells[i][j] = -1

    def check_down(self, coords, step_y, step_x):
        """
        Проверка дна
        :param coords: Координаты фигуры в исходном положении
        :param step_y: Сколько шагов должен пройти по OY
        :param step_x: Сколько шагов должен пройти по OХ
        """
        for coord in coords:
            if self.cells[coord[1] + step_y][coord[0] + step_x] * -1 != 1 and coord[1] + step_y > 2:
                return False
        return True

    def check_left_right(self, coords, step_y, step_x, dir):
        """
        Проверка правой стенки и левой стенки
        :param coords: Координаты фигуры в исходном положении
        :param step_y: Сколько шагов должен пройти по OY
        :param step_x: Сколько шагов должен пройти по OХ
        :param dir: Если клетка передвинется направо(при dir = 1) или налево (при dir = -1)
        """
        for coord in coords:
            if self.cells[coord[1] + step_y][coord[0] + step_x + dir] * -1 != 1:
                return False
        return True

    def check_reverse(self, coords, step_y, step_x):
        """
        Проверка поворота фигуры
        :param coords: Координаты фигуры в исходном положении
        :param step_y: Сколько шагов должен пройти по OY
        :param step_x: Сколько шагов должен пройти по OХ
        """
        for coord in coords:
            if self.cells[coord[1] + step_y][coord[0] + step_x] * -1 != 1:
                return False
        return True

    def save(self, coord):
        """
        Сохранение клетки, которая упала до конца
        :param coord: Координаты клетки
        :return:
        """
        self.cells[coord[1]][coord[0]] = 2


pygame.init()
size = width, height = 700, 650
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
running = True
board = Board()
while running:
    if new_shape:
        shape = random.choice(shapes)
        new_shape = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if board.check_left_right(shape[direction], step_y, step_x, 1):
                    step_x += 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if board.check_left_right(shape[direction], step_y, step_x, -1):
                    step_x -= 1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if board.check_reverse(shape[(direction + 1) % 4], step_y, step_x):
                    direction += 1
                    direction %= 4
    if board.check_down(shape[direction], step_y, step_x):
        for i in range(4):
            l = shape[direction][i].copy()
            l[1] += step_y
            l[0] += step_x
            board.start(l, screen)
        step_y += 1
    else:
        for i in range(4):
            board.save([shape[direction][i][0] + step_x, shape[direction][i][1] + step_y - 1])
        new_shape = True
        step_y = 0
        step_x = 0
    board.refresh()
    pygame.time.delay(100)
    pygame.display.flip()