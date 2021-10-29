from typing import Any
from collections.abc import Callable
import functools

def counter(func:Callable) -> Callable:
    """Декоратор счётчика"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        wrapper.count += 1
        res = func(*args, **kwargs)
        print('Функция {func} была вызвана {count} раз'.format
              (func=func.__name__, count=wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

@counter
def test() -> Any:
    print('test')

for _ in range(5):
    test()