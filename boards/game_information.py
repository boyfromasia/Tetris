from boards.next_shape import NextShapeBoard
from boards.score import Score
from values.config import NEW_SHAPE_BOARD
from media_and_image import Image


class GameInformation:
    def __init__(self,line, score, screen2, screen_record, screen_next_shape, screen_line, screen_score):
        self.screen2 = screen2
        self.screen_record = screen_record
        self.screen_next_shape = screen_next_shape
        self.draw_border_next_shape(screen2, NEW_SHAPE_BOARD)
        Score(line, score, screen_record, screen_score, screen_line)

    def next_shape_board(self, figure, block, screen):
        """
        Подключение доски со следующей фигурой
        :param figure: фигура
        :param block: нахвание спрайта
        :param screen: слой
        """
        NextShapeBoard(figure, block, self.screen_next_shape)

    def draw_border_next_shape(self, screen, name):
        """
        Отрисовка доски с информацией о игре
        :param screen: слой
        :param name: название спрайта
        """
        image = Image().load_image_boards(name, (216, 416))
        screen.blit(image, (0, 0))


