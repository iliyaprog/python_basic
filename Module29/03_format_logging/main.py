import logging
import functools
from typing import Callable

formatter = logging.basicConfig(filename='result.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(name='result')
logger.setLevel(level=logging.INFO)

def log_methods(func: Callable) -> logging:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info('Результат функции {function}: {answer}'.format(function=func.__name__, answer=result))
    return wrapper


def decorate(cls):
    for i_method in dir(cls):
        if i_method.startswith('__') is False:
            cur_method = getattr(cls, i_method)
            decorated_method = log_methods(cur_method)
            setattr(cls, i_method, decorated_method)
    return cls


@decorate
class First_class:

    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@decorate
class Second_class(First_class):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = Second_class()
my_obj.test_sum_1()
my_obj.test_sum_2()
