from sys import exit
from boards.next_shape import next_shape_board
from boards.next_shape import draw_text
import pygame
import random
import pprint

direction = 0
step_x = 0
step_y = 0

seashell = (255, 245, 238)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
pink = (255, 165, 0)
light_blue = (64, 224, 208)
colors = [seashell, white, red, green, blue, yellow, purple, pink, light_blue]

I = (([[6, 0], [6, 1], [6, 2], [6, 3]], [[5, 2], [6, 2], [7, 2], [8, 2]], [[6, 0], [6, 1], [6, 2], [6, 3]], [[5, 2], [6, 2], [7, 2], [8, 2]]), green)
L = (([[6, 2], [7, 2], [7, 1], [5, 2]], [[6, 2], [6, 1], [6, 3], [5, 1]], [[6, 2], [7, 2], [5, 2], [5, 3]], [[6, 3], [6, 1], [6, 2], [7, 3]]), red)
J = (([[6, 2], [7, 2], [7, 3], [5, 2]], [[6, 2], [6, 1], [6, 3], [7, 1]], [[6, 2], [7, 2], [5, 2], [5, 1]], [[6, 3], [6, 2], [6, 1], [5, 3]]), blue)
W = (([[6, 2], [6, 3], [7, 3], [5, 3]], [[6, 3], [6, 2], [6, 1], [7, 2]], [[6, 4], [6, 3], [7, 3], [5, 3]], [[6, 3], [6, 2], [6, 1], [5, 2]]), light_blue)
Q = (([[6, 3], [7, 3], [6, 2], [7, 2]], [[6, 3], [7, 3], [6, 2], [7, 2]], [[6, 3], [7, 3], [6, 2], [7, 2]], [[6, 3], [7, 3], [6, 2], [7, 2]]), purple)
Z = (([[6, 3], [7, 3], [5, 2], [6, 2]], [[6, 3], [6, 2], [7, 2], [7, 1]], [[6, 3], [7, 3], [5, 2], [6, 2]], [[6, 3], [6, 2], [7, 2], [7, 1]]), pink)
S = (([[6, 3], [5, 3], [6, 2], [7, 2]], [[5, 1], [5, 2], [6, 2], [6, 3]], [[6, 3], [5, 3], [6, 2], [7, 2]], [[5, 1], [5, 2], [6, 2], [6, 3]]), yellow)
shapes = [I, L, J, W, Q, Z, S]

new_shape = True


class Board:
    def __init__(self):
        """
        Инициализация матрицы игры
        """
        self.cells = [[0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0] if x != 0 and x != 1 and x != 2 and x != 23 else
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(24)]
        self.size_cell = 20

    def render(self, screen, color):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        pygame.draw.polygon(screen, blue, (self.get_coord((2, 3)),
                                               self.get_coord((12, 3)) ,self.get_coord((12, 23)), self.get_coord((2, 23))), 10)
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j] == -1:
                    self.draw(self.get_coord((j, i)), screen, white)
                else:
                    if self.cells[i][j] == 1:
                        self.draw(self.get_coord((j, i)), screen, color)
                    elif self.cells[i][j] == 2:
                        self.draw(self.get_coord((j, i)), screen, green)
                    elif self.cells[i][j] == 3:
                        self.draw(self.get_coord((j, i)), screen, red)
                    elif self.cells[i][j] == 4:
                        self.draw(self.get_coord((j, i)), screen, blue)
                    elif self.cells[i][j] == 5:
                        self.draw(self.get_coord((j, i)), screen, yellow)
                    elif self.cells[i][j] == 6:
                        self.draw(self.get_coord((j, i)), screen, purple)
                    elif self.cells[i][j] == 7:
                        self.draw(self.get_coord((j, i)), screen, pink)
                    elif self.cells[i][j] == 8:
                        self.draw(self.get_coord((j, i)), screen, light_blue)

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
        pygame.draw.polygon(screen, seashell, ((pos[0], pos[1]),
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

    def start(self, coords, screen, color):
        """
        Изменение значения в матрице. Начало Игры.
        :param coords: координаты
        :param color: Цвет клетки
        """
        self.cells[coords[1]][coords[0]] *= -1
        #self.render(screen, color)

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

    def save(self, coord, color):
        """
        Сохранение клетки, которая упала до конца
        :param color: Цвет клетки
        :param coord: Координаты клетки
        """
        if color == green:
            self.cells[coord[1]][coord[0]] = 2
        elif color == red:
            self.cells[coord[1]][coord[0]] = 3
        elif color == blue:
            self.cells[coord[1]][coord[0]] = 4
        elif color == yellow:
            self.cells[coord[1]][coord[0]] = 5
        elif color == purple:
            self.cells[coord[1]][coord[0]] = 6
        elif color == pink:
            self.cells[coord[1]][coord[0]] = 7
        elif color == light_blue:
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
                del self.cells[self.cells.index(cell)]
                self.cells.insert(3, [0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0])


pygame.init()
size = width, height = 500, 520
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface((140, 180))
screen.fill((0, 0, 0))
screen2.fill((0, 0, 0))
running = True
board = Board()
shape = random.choice(shapes)

while running:
    draw_text(screen2, random.choice(colors))
    if new_shape:
        "Выбор новой фигуры"
        next_shape = random.choice(shapes)
        new_shape = False
        next_shape_board(next_shape[0][direction], next_shape[1], screen2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                "Направо"
                if board.check_left_right(shape[0][direction], step_y, step_x, 1):
                    step_x += 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                "Налево"
                if board.check_left_right(shape[0][direction], step_y, step_x, -1):
                    step_x -= 1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                "Повернуть"
                if board.check_reverse(shape[0][(direction + 1) % 4], step_y, step_x):
                    direction += 1
                    direction %= 4
    if board.check_down(shape[0][direction], step_y, step_x):
        "Движение фигуры"
        for i in range(4):
            l = shape[0][direction][i].copy()
            l[1] += step_y
            l[0] += step_x
            board.start(l, screen, shape[1])
        board.render(screen, shape[1])
        step_y += 1
    else:
        for i in range(4):
            "Сохранение фигуры"
            board.save([shape[0][direction][i][0] + step_x, shape[0][direction][i][1] + step_y - 1], shape[1])
        shape = next_shape
        new_shape = True
        step_y = 0
        step_x = 0
        direction = 0
    board.refresh()
    board.delete_line()
    screen.blit(screen2, (260, 55))
    if board.check_game_over():
        exit()
    pygame.display.flip()
    pygame.time.Clock().tick(10)