import logging
import random

formatter = logging.Formatter('%(message)s')

def setup_logger(name, level=logging.ERROR):
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def increase_randomly(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def decrease_randomly(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


count_line = 0

try:
    with open('coordinates.txt', 'r') as file:
        for line in file.readlines():
            my_list = []
            count_line += 1
            nums_list = list(line.split())

            try:
                res1 = increase_randomly(int(nums_list[0]), int(nums_list[1]))
                my_list.append(res1)
            except ZeroDivisionError:
                errors_logger = setup_logger('errors')
                errors_logger.error('Ошибка в {} строке, в первой функции. Деление на ноль'.format(count_line))

            try:
                res2 = decrease_randomly(int(nums_list[0]), int(nums_list[1]))
                my_list.append(res2)
            except ZeroDivisionError:
                errors_logger = setup_logger('errors')
                errors_logger.error('Ошибка в {} строке, во второй функции. Деление на ноль'.format(count_line))

            number = random.randint(0, 100)
            my_list.append(number)

            my_list = str(sorted(my_list))

            with open('result.txt', 'a') as file_2:
                file_2.write(my_list + '\n')

except FileNotFoundError:
    errors_logger = setup_logger('errors')
    errors_logger.error('Ошибка. Файла с координатами не существует')





