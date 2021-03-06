import pygame
from src.boards.board import Board
from src.values.colors import BLACK, RED
from src.values.config import CELLS, SIZE_CELL, GAME_OVER, INSTRUCTION
import random
from src.boards.media_and_image import Image
from src.values.shape import SHAPES
from src.boards.game_information import GameInformation
import time
from src.values.music import SOUNDTRACK

class Game:
    def __init__(self):
        pygame.init()
        Image().load_music(random.choice(SOUNDTRACK))
        pygame.display.set_caption("TETRIS")
        size = 500, 520
        self.screen = pygame.display.set_mode(size)
        self.screen2 = pygame.Surface((216, 416))
        self.screen_record = pygame.Surface((180, 50))
        self.screen_next_shape = pygame.Surface((120, 120))
        self.screen_score = pygame.Surface((180, 50))
        self.screen_line = pygame.Surface((180, 50))
        self.screen.fill(BLACK)
        self.screen2.fill(BLACK)
        self.screen_record.fill(BLACK)
        self.screen_next_shape.fill(RED)
        self.direction = 0
        self.step_x = 0
        self.step_y = 0
        self.time_start = 0
        self.game_over_flag = False
        self.running = True
        self.board = Board(CELLS, SIZE_CELL)
        self.shape = random.choice(SHAPES)
        self.position = self.shape[0]
        self.color = self.shape[1]
        self.new_shape = True
        self.start_game_flag = False

    def run(self):
        """
        Основной цикл игры
        """
        while self.running:
            if self.start_game_flag:
                if self.game_over_flag is False:
                    self.start()
                else:
                    self.game_over()
            else:
                self.instruction()

    def game_over(self):
        """
        При проигрыше выполняется выход
        """
        image = Image().load_image_boards(GAME_OVER, (500, 520))
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
        if time.time() - self.time_start >= 5:
            self.running = False
            pygame.quit()

    def start(self):
        """
        Запуск игры
        """
        self.game_information = GameInformation(self.board.line, self.board.score, self.screen2,
                                                self.screen_record, self.screen_next_shape, self.screen_line,
                                                self.screen_score)
        self.get_next_shape()
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
        if self.board.check_down(self.position[self.direction], self.step_y, self.step_x):
            self.falling_shape()
        else:
            self.save_shape()

    def render(self):
        """
        Рендер экрана
        """
        self.board.refresh()
        self.board.delete_line()
        self.screen.blit(self.screen2, (260, 53))
        self.screen.blit(self.screen_record, (278, 237))
        self.screen.blit(self.screen_next_shape, (308, 100))
        self.screen.blit(self.screen_score, (278, 303))
        self.screen.blit(self.screen_line, (278, 371))

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
        if self.board.check_left_right(self.position[self.direction], self.step_y, self.step_x, 1):
            self.step_x += 1

    def move_left(self):
        """
        Движение налево
        """
        if self.board.check_left_right(self.position[self.direction], self.step_y, self.step_x, -1):
            self.step_x -= 1

    def reverse(self):
        """
        Поворот фигуры
        """
        if self.board.check_reverse(self.position[(self.direction + 1) % 4], self.step_y, self.step_x):
            self.direction += 1
            self.direction %= 4

    def falling_shape(self):
        """
        Падение фигуры
        """
        for i in range(4):
            figure = self.position[self.direction][i].copy()
            figure[1] += self.step_y
            figure[0] += self.step_x
            self.board.start(figure)
        self.board.render(self.screen, self.color)
        self.step_y += 1

    def save_shape(self):
        """
        Сохранение фигуры
        """
        for i in range(4):
            self.board.save([self.position[self.direction][i][0] + self.step_x,
                             self.position[self.direction][i][1] + self.step_y - 1], self.color)
        self.refresh_values()

    def refresh_values(self):
        """
        Возвращение переменных в старое положение
        """
        self.position = self.next_shape[0]
        self.color = self.next_shape[1]
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
        self.game_information.next_shape_board(self.next_shape[0], self.next_shape[1], self.screen2)

    def check_game_over(self):
        """
        Обработка проигрыша
        """
        if self.board.check_game_over():
            self.game_over_flag = True
            self.time_start = time.time()

    def instruction(self):
        """
        Экран инструкции
        """
        image = Image().load_image_boards(INSTRUCTION, (500, 520))
        self.screen.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                self.screen.fill(BLACK)
                self.start_game_flag = True
        pygame.display.flip()


