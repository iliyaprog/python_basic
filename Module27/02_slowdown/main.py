from typing import Any
from collections.abc import Callable
from typing import List

import time

"""Декоратор, который включает таймер и задерживает выполнение функции"""

def decorator_factory(argument):
    def breakes(func:Callable) ->Callable:
        def wrapper(*args, **kwargs) -> Any:
            time.sleep(argument)
            end_move = func(*args, **kwargs)
            return end_move
        return wrapper
    return breakes

@decorator_factory(argument=3)
def this_function(number) -> List:
    i_list = [(i ** 2) for i in range(number + 1)]
    return i_list

limit_number = int(input('До квадрата какого числа будем считать?: '))
for _ in range(3):
    result = this_function(limit_number)
    print(result)


