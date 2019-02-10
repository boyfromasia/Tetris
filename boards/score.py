import pygame
from values.colors import BLACK
from values.config import FILE_NAME_RECORD, RECORD, SCORE
from values.numbers import ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, ZERO
import os


class Score():
    def __init__(self, score, screen_record, screen_score, color):
        self.record = 0
        self.score = 0
        self.screen_score = screen_score
        self.screen_record = screen_record
        self.render(score, screen_record, screen_score, color)

    def render(self, score, screen_record, screen_score, color):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        screen_record.fill(BLACK)
        self.draw_record(screen_record, color)
        self.draw_score(screen_score, color, score)
        self.update_record()
        self.time_in_game()

    def draw_record(self, screen, color):
        with open(FILE_NAME_RECORD, "rt", encoding="utf-8") as f:
            self.record = f.read()
        image = self.load_image_border(RECORD)
        screen.blit(image, (0, 0))

    def draw_score(self, screen, color, score):
        self.score = str(score * 50)
        image = self.load_image_border(SCORE)
        screen.blit(image, (0, 0))
        self.draw_numbers(screen, self.score)



    def time_in_game(self):
        pass

    def update_record(self):
        if int(self.record) <= int(self.score):
            self.delete_old_record()
            self.refractor_record()

    def refractor_record(self):
        with open(FILE_NAME_RECORD, "wt", encoding="utf-8") as f:
            f.write(str(self.score))

    def load_image_border(self, name):
        fullname = os.path.join('data/boards', name)
        image = pygame.image.load(fullname)
        image = pygame.transform.scale(image, (180, 50))
        return image

    def load_image_number(self, name):
        fullname = os.path.join('data/numbers', name)
        image = pygame.image.load(fullname)
        image = pygame.transform.scale(image, (30, 23))
        return image

    def delete_old_record(self):
        with open(FILE_NAME_RECORD, "w", encoding="utf-8") as f:
            f.close()

    def draw_numbers(self, screen, score):
        cnt = 1
        for number in score[::-1]:
            if number == "1":
                image = self.load_image_number(ONE)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "2":
                self.load_image_number(TWO)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "3":
                image = self.load_image_number(THREE)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "4":
                image = self.load_image_number(FOUR)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "5":
                image = self.load_image_number(FIVE)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "6":
                image = self.load_image_number(SIX)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "7":
                image = self.load_image_number(SEVEN)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "8":
                image = self.load_image_number(EIGHT)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "9":
                image = self.load_image_number(NINE)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "0":
                image = self.load_image_number(ZERO)
                screen.blit(image, (180 - cnt * 30, 25))
            cnt += 1
