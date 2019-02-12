import pygame
from values.config import WHITE, GREEN, LIGHT_BLUE, DARK_BLUE, RED, YELLOW, PURPLE, ORANGE, ONE_LINE_SCORE
from values.colors import GREY
from work_with_image import Image
from values.config import BOARD


class Board:
    def __init__(self, cells, size_cell):
        """
        Инициализация матрицы игры
        """
        self.score = 0
        self.cells = cells
        self.size_cell = size_cell
        self.line = 0

    def render(self, screen, color):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        self.draw_border(screen)
        self.draw_board(screen, color)

    def draw_full_cell(self, pos, screen, color):
        """
        Отрисовка полной клетки
        :param color: Цвет клетки
        :param pos: позиция клетки
        :param screen: слой
        """
        self.draw_color_for_cell(screen, color, pos)
        self.draw_border_for_cells(screen, pos)

    def get_coord(self, cell):
        """
        Получение координат в пикселях
        :param cell: Координаты
        """
        x = cell[0] * self.size_cell
        y = cell[1] * self.size_cell
        return (x, y)

    def start(self, coord):
        """
        Изменение значения в матрице. Начало Игры.
        :param coord: координаты
        """
        self.cells[coord[1]][coord[0]] *= -1

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
        elif color == DARK_BLUE:
            self.cells[coord[1]][coord[0]] = 4
        elif color == YELLOW:
            self.cells[coord[1]][coord[0]] = 5
        elif color == PURPLE:
            self.cells[coord[1]][coord[0]] = 6
        elif color == ORANGE:
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
        """
        Удаление поля при заполнении
        """
        for cell in self.cells[3:-1]:
            flag = False
            for dot in cell[2:12]:
                if dot != -1:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                self.score += (self.cells.index(cell) - 2) * ONE_LINE_SCORE
                self.line += 1
                del self.cells[self.cells.index(cell)]
                self.cells.insert(3, [0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0])

    def draw_border(self, screen):
        """
        Отрисока рамки для поля
        :param screen: Экран
        """
        image = Image().load_image_boards(BOARD, (216, 416))
        screen.blit(image, (32, 52))

    def draw_board(self, screen, color):
        """
        Отрисовка поля
        :param screen: Экран
        :param color: Цвет
        """
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j] == -1:
                    self.draw_border_for_cells(screen, self.get_coord((j, i)))
                else:
                    if self.cells[i][j] == 1:
                        self.draw_full_cell(self.get_coord((j, i)), screen, color)
                    elif self.cells[i][j] == 2:
                        self.draw_full_cell(self.get_coord((j, i)), screen, GREEN)
                    elif self.cells[i][j] == 3:
                        self.draw_full_cell(self.get_coord((j, i)), screen, RED)
                    elif self.cells[i][j] == 4:
                        self.draw_full_cell(self.get_coord((j, i)), screen, DARK_BLUE)
                    elif self.cells[i][j] == 5:
                        self.draw_full_cell(self.get_coord((j, i)), screen, YELLOW)
                    elif self.cells[i][j] == 6:
                        self.draw_full_cell(self.get_coord((j, i)), screen, PURPLE)
                    elif self.cells[i][j] == 7:
                        self.draw_full_cell(self.get_coord((j, i)), screen, ORANGE)
                    elif self.cells[i][j] == 8:
                        self.draw_full_cell(self.get_coord((j, i)), screen, LIGHT_BLUE)

    def draw_border_for_cells(self, screen, pos):
        """
        Отрисовка рамки для одного квадрата
        :param screen: Экран
        :param pos: Координата
        """
        pygame.draw.polygon(screen, GREY, ((pos[0], pos[1]),
                                               (pos[0] + self.size_cell, pos[1]),
                                               (pos[0] + self.size_cell, pos[1] + self.size_cell),
                                               (pos[0], pos[1] + self.size_cell)), 1)

    def draw_color_for_cell(self, screen, color, pos):
        """
        Отрисовка одной клетки
        :param screen: Экран
        :param color: Цвет
        :param pos: Координата
        """
        image = Image().load_image_block(color)
        screen.blit(image, pos)
