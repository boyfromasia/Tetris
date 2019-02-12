import pygame
from values.colors import BLACK
from values.config import FILE_NAME_RECORD, RECORD, SCORE, LINE
from values.numbers import ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, ZERO
import os
from work_with_image import Image


class Score:
    def __init__(self, line, score, screen_record, screen_score, screen_line):
        self.screen_score = screen_score
        self.screen_record = screen_record
        self.render(line, score, screen_record, screen_score, screen_line)

    def render(self, line, score, screen_record, screen_score, screen_line):
        """
        Рендер поля
        :param color: Цвет клетки
        """
        screen_record.fill(BLACK)
        self.draw_record(screen_record)
        self.draw_score(screen_score, score)
        self.update_record()
        self.draw_line(screen_line, line)

    def draw_record(self, screen):
        """
        Отрисовка рекорда
        :param screen: слой
       """
        with open(FILE_NAME_RECORD, "rt", encoding="utf-8") as f:
            self.record = f.read()
        image = Image().load_image_boards(RECORD, (180, 60))
        screen.blit(image, (0, 0))
        self.draw_numbers(screen, self.record)

    def draw_score(self, screen, score):
        """
        Отрисовка баллов наи данный момент
        :param screen: слой
        :param score: баллы
        :return:
        """
        self.score = str(score)
        image = Image().load_image_boards(SCORE, (180, 50))
        screen.blit(image, (0, 0))
        self.draw_numbers(screen, self.score)

    def draw_line(self, screen, line):
        """
        Отрисовка количество линий было убрано
        :param screen: слой
        :param line: количество линий
        """
        self.line = str(line)
        image = Image().load_image_boards(LINE, (180, 50))
        screen.blit(image, (0, 0))
        self.draw_numbers(screen, self.line)

    def update_record(self):
        """
        обновление рекорда
        """
        if int(self.record) <= int(self.score):
            self.delete_old_record()
            self.refractor_record()

    def refractor_record(self):
        """
        перезапись рекорда
        """
        with open(FILE_NAME_RECORD, "wt", encoding="utf-8") as f:
            f.write(str(self.score))

    def delete_old_record(self):
        """
        удаление старого рекорда
        """
        with open(FILE_NAME_RECORD, "w", encoding="utf-8") as f:
            f.close()

    def draw_numbers(self, screen, score):
        """
        отрисовка цифр
        :param screen: слой
        :param score: то, что нужно нужно отрисовать
        :return:
        """
        cnt = 1
        for number in score[::-1]:
            if number == "1":
                image = Image().load_image_numbers(ONE)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "2":
                image = Image().load_image_numbers(TWO)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "3":
                image = Image().load_image_numbers(THREE)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "4":
                image = Image().load_image_numbers(FOUR)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "5":
                image = Image().load_image_numbers(FIVE)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "6":
                image = Image().load_image_numbers(SIX)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "7":
                image = Image().load_image_numbers(SEVEN)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "8":
                image = Image().load_image_numbers(EIGHT)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "9":
                image = Image().load_image_numbers(NINE)
                screen.blit(image, (180 - cnt * 30, 25))
            elif number == "0":
                image = Image().load_image_numbers(ZERO)
                screen.blit(image, (180 - cnt * 30, 25))
            cnt += 1
