import pygame
from sys import exit
from boards.tetris_game import Board
from values.colors import BLACK, COLORS
from boards.next_shape import NextShapeBoard, draw_text
from values.config import CELLS, SIZE_CELL
import random
from values.shape import SHAPES


class Game:
    def __init__(self):
        pygame.init()
        size = 500, 520
        self.screen = pygame.display.set_mode(size)
        self.screen2 = pygame.Surface((140, 180))
        self.screen3 = pygame.Surface((140, 260))
        self.screen.fill(BLACK)
        self.screen2.fill(BLACK)
        self.screen3.fill(BLACK)
        self.direction = 0
        self.step_x = 0
        self.step_y = 0
        self.running = True
        self.board = Board(CELLS, SIZE_CELL)
        self.shape = random.choice(SHAPES)
        self.new_shape = True

    def run(self):
        """
        Основной цикл игры
        """
        while self.running:
            self.board_next_shape()
            self.handle_event(pygame.event.get())
            self.update()
            self.render()
            self.check_game_over()
            pygame.display.flip()
            pygame.time.Clock().tick(10)

    def get_next_shape(self):
        """
        Проверка надобности отображения следующей фигуры
        """
        if self.new_shape:
            self.random_shape()

    def handle_event(self, events):
        """
        Обработка событий
        :param events: События
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                self.handle_event_keydown(event)

    def update(self):
        """
        Обработка дальнейших дейстий для падающей фигуры
        """
        if self.board.check_down(self.shape[0][self.direction], self.step_y, self.step_x):
            self.falling_shape()
        else:
            self.save_shape()

    def render(self):
        """"""
        self.board.refresh()
        self.board.delete_line()
        self.screen.blit(self.screen2, (260, 55))

    def quit(self):
        """
        Выход
        """
        self.running = False

    def handle_event_keydown(self, event):
        """
        Обработка нажатия кнопки
        :param event: Событие
        """
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.move_right()
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.move_left()
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.reverse()

    def move_right(self):
        """
        Движение направо
        """
        if self.board.check_left_right(self.shape[0][self.direction], self.step_y, self.step_x, 1):
            self.step_x += 1

    def move_left(self):
        """
        Движение налево
        """
        if self.board.check_left_right(self.shape[0][self.direction], self.step_y, self.step_x, -1):
            self.step_x -= 1

    def reverse(self):
        """
        Поворот фигуры
        """
        if self.board.check_reverse(self.shape[0][(self.direction + 1) % 4], self.step_y, self.step_x):
            self.direction += 1
            self.direction %= 4

    def falling_shape(self):
        """
        Падение фигуры
        """
        for i in range(4):
            figure = self.shape[0][self.direction][i].copy()
            figure[1] += self.step_y
            figure[0] += self.step_x
            self.board.start(figure)
        self.board.render(self.screen, self.shape[1])
        self.step_y += 1

    def save_shape(self):
        """
        Сохранение фигуры
        """
        for i in range(4):
            self.board.save([self.shape[0][self.direction][i][0] + self.step_x, self.shape[0][self.direction][i][1] + self.step_y - 1], self.shape[1])
        self.refresh_values()

    def refresh_values(self):
        """
        Возвращение переменных в старое положение
        :return:
        """
        self.shape = self.next_shape
        self.new_shape = True
        self.step_y = 0
        self.step_x = 0
        self.direction = 0

    def random_shape(self):
        """
        Выбор следующей фигуры.
        Передача в класс для дальнейшего отображения.
        """
        self.next_shape = random.choice(SHAPES)
        self.new_shape = False
        NextShapeBoard(self.next_shape[0][self.direction], self.next_shape[1], self.screen2)

    def check_game_over(self):
        """
        Обработка проигрыша
        """
        if self.board.check_game_over():
            exit()

    def board_next_shape(self):
        """
        Отображение текста "Next".
        Проверка следующей фигуры.
        """
        draw_text(self.screen2, random.choice(COLORS))
        self.get_next_shape()

