import pygame
from values.colors import RED, GREEN, BLUE, YELLOW, PURPLE, PINK, LIGHT_BLUE, WHITE, SEASHELL

score = 0


class Board:
    def __init__(self, cells, size_cell):
        """
        Инициализация матрицы игры
        """
        self.cells = cells
        self.size_cell = size_cell

    def render(self, screen, color):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        pygame.draw.polygon(screen, BLUE, (self.get_coord((2, 3)),
                                               self.get_coord((12, 3)) ,self.get_coord((12, 23)), self.get_coord((2, 23))), 10)
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j] == -1:
                    self.draw(self.get_coord((j, i)), screen, WHITE)
                else:
                    if self.cells[i][j] == 1:
                        self.draw(self.get_coord((j, i)), screen, color)
                    elif self.cells[i][j] == 2:
                        self.draw(self.get_coord((j, i)), screen, GREEN)
                    elif self.cells[i][j] == 3:
                        self.draw(self.get_coord((j, i)), screen, RED)
                    elif self.cells[i][j] == 4:
                        self.draw(self.get_coord((j, i)), screen, BLUE)
                    elif self.cells[i][j] == 5:
                        self.draw(self.get_coord((j, i)), screen, YELLOW)
                    elif self.cells[i][j] == 6:
                        self.draw(self.get_coord((j, i)), screen, PURPLE)
                    elif self.cells[i][j] == 7:
                        self.draw(self.get_coord((j, i)), screen, PINK)
                    elif self.cells[i][j] == 8:
                        self.draw(self.get_coord((j, i)), screen, LIGHT_BLUE)

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
        pygame.draw.polygon(screen, SEASHELL, ((pos[0], pos[1]),
                                            (pos[0] + self.size_cell, pos[1]),
                                            (pos[0] + self.size_cell, pos[1] + self.size_cell),
                                            (pos[0], pos[1] + self.size_cell)), 1)

    def get_coord(self, cell):
        """
        Получение координат в пикселях
        :param cell: Координаты
        """
        x = cell[0] * self.size_cell
        y = cell[1] * self.size_cell
        return (x, y)

    def start(self, coords):
        """
        Изменение значения в матрице. Начало Игры.
        :param coords: координаты
        """
        self.cells[coords[1]][coords[0]] *= -1

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
        try:
            for coord in coords:
                if self.cells[coord[1] + step_y][coord[0] + step_x] * -1 != 1:
                    return False
            return True
        except IndexError:
            return False

    def save(self, coord, color):
        """
        Сохранение клетки, которая упала до конца
        :param color: Цвет клетки
        :param coord: Координаты клетки
        """
        if color == GREEN:
            self.cells[coord[1]][coord[0]] = 2
        elif color == RED:
            self.cells[coord[1]][coord[0]] = 3
        elif color == BLUE:
            self.cells[coord[1]][coord[0]] = 4
        elif color == YELLOW:
            self.cells[coord[1]][coord[0]] = 5
        elif color == PURPLE:
            self.cells[coord[1]][coord[0]] = 6
        elif color == PINK:
            self.cells[coord[1]][coord[0]] = 7
        elif color == LIGHT_BLUE:
            self.cells[coord[1]][coord[0]] = 8

    def check_game_over(self):
        """
        Проверка проигрыша.
        """
        for cell in self.cells[:3]:
            for dot in cell:
                if dot != 0:
                    return True
        return False

    def delete_line(self):
        for cell in self.cells[3:-1]:
            flag = False
            for dot in cell[2:12]:
                if dot != -1:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                global score
                score += 1
                del self.cells[self.cells.index(cell)]
                self.cells.insert(3, [0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0])
