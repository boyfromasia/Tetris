import pygame
from values.colors import BLACK
from values.config import FILE_NAME_RECORD

class Score():
    def __init__(self, score, screen, color):
        self.render(score, screen, color)
        self.record = 0
        self.score = 0

    def render(self, score, screen, color):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        screen.fill(BLACK)
        self.draw_record_score(screen, color)
        self.draw_now_score(screen, color, score)
        self.update_record()
        self.time_in_game()

    def draw_record_score(self, screen, color):
        with open(FILE_NAME_RECORD, "rt", encoding="utf-8") as f:
            self.record = f.read()
        text = pygame.font.Font(None, 50).render(self.record, 0, color)
        screen.blit(text, (30, 0))

    def draw_now_score(self, screen, color, score):
        self.score = score * 50
        text = pygame.font.Font(None, 50).render(str(self.score), 0, color)
        screen.blit(text, (30, 50))

    def time_in_game(self):
        pass

    def update_record(self):
        if int(self.record) <= self.score:
            self.delete_old_record()
            self.refractor_record()

    def refractor_record(self):
        with open(FILE_NAME_RECORD, "wt", encoding="utf-8") as f:
            f.write(str(self.score))

    def delete_old_record(self):
        with open(FILE_NAME_RECORD, "w", encoding="utf-8") as f:
            f.close()

