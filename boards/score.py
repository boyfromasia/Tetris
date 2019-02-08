import pygame


class Score():
    def __init__(self, score, screen):
        self.score = score
        self.screen = screen
        self.render(screen, color)

    def render(self, screen, color):
        """
        Рендер поля
        :param color: Цвет клетки
        """


    def draw_record_score(self, pos, screen, color):
        with open("record.txt", "rt", encoding="utf-8") as f:
            record = f.read()


    def draw_now_score(self):
        pass

    def time_in_game(self):
        pass