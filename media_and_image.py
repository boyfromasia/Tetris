import os
import pygame
from values.config import SIZE_CELL


class Image:
    def load_image_block(self, name):
        fullname = os.path.join('data/blocks', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, (SIZE_CELL, SIZE_CELL))
        return image

    def load_image_boards(self, name, size):
        fullname = os.path.join('data/boards', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, size)
        return image

    def load_image_numbers(self, name):
        fullname = os.path.join('data/numbers', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, (30, 23))
        return image

    def load_music(self, name):
        pygame.mixer.init()
        fullname = os.path.join('music', name)
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.play(-1, 0.0)