import os
import pygame
from src.values.config import SIZE_CELL


class Image:
    def load_image_block(self, name):
        fullname = os.path.join('src/data/blocks', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, (SIZE_CELL, SIZE_CELL))
        return image

    def load_image_boards(self, name, size):
        fullname = os.path.join('src/data/boards', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, size)
        return image

    def load_image_numbers(self, name):
        fullname = os.path.join('src/data/numbers', name)
        image = pygame.image.load(fullname).convert_alpha()
        image = pygame.transform.scale(image, (30, 23))
        return image

    def load_music(self, name):
        pygame.mixer.init()
        fullname = os.path.join('src/music', name)
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.play(-1, 0.0)