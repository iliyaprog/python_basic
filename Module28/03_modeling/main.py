import logging
import itertools
import math

formatter = logging.basicConfig(filename='result.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def setup_logger(name, log_file, level=logging.INFO) -> logging:

    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

class Square:

    """Класс квадрат"""
    def __init__(self, length:(int, float)) -> None:
        self.__length = length

    def square(self) -> (int, float):
        result = self.__length ** 2
        return result

    def perimeter(self) ->(int, float):
        result = self.__length * 4
        return result

    @property
    def length(self) -> (int, float):
        return self.__length

    @length.setter
    def length(self, change) -> None:
        self.__length = change

class Triangle:

    """Класс треугольник"""
    def __init__(self, length: (int, float), height: (int, float)) -> None:
        self.__length = length
        self.__height = height

    def square(self) -> (int, float):
        result = (self.__height * self.__length) / 2
        return result

    def perimeter(self) -> (int, float):
        result = math.sqrt(((self.__length / 2) ** 2) + (self.__height ** 2)) * 2 + self.__length
        return result

    @property
    def length_and_height(self) -> (int, float):
        return self.__length, self.__height

    @length_and_height.setter
    def length_and_height(self, change_length: (int, float), change_height: (int, float)) -> None:
        self.__length = change_length
        self.__height = change_height

class Mixin_sq:

    """Класс примесь в котором считаются площади объемных фигур"""
    def figure_sq(self, list_figure: list) -> (int, float):
        summ = 0
        for i_elem in list_figure:
            s = i_elem.square()
            summ += s
        return summ

class Cube(Mixin_sq):

    """Дочерний класс Куб"""
    def __init__(self, list_sq: list) -> None:
        self.list = list_sq


class Pyramid(Mixin_sq):

    """Дочерний класс Пирамида"""
    def __init__(self, list_sq) -> None:
        self.list = list_sq


figure_1 = [Triangle(6, 4), Triangle(6, 4), Triangle(6, 4), Triangle(6, 4), Square(6)]
figure_2 = [Square(2), Square(2), Square(2), Square(2), Square(2), Square(2)]

my_pyramid = Pyramid(figure_1)
my_cube = Cube(figure_2)

for i_elem in figure_2:
    i_elem.length = 3


for i_elem in (figure_1 + figure_2):
    logger = setup_logger(name='sq_{}'.format(type(i_elem).__name__), log_file='result_log')
    logger.info('Площадь фигуры {}'.format(i_elem.square()))

    logger = setup_logger(name='sq_{}'.format(type(i_elem).__name__), log_file='result_log')
    logger.info('Периметр фигуры {}'.format(i_elem.perimeter()))


logger = setup_logger(name='sq_{}'.format(type(my_cube).__name__), log_file='result_log')
logger.info('Площадь куба {}'.format(my_cube.figure_sq(figure_1)))

logger = setup_logger(name='sq_{}'.format(type(my_pyramid).__name__), log_file='result_log')
logger.info('Площадь пирамиды {}'.format(my_pyramid.figure_sq(figure_2)))





