from typing import Any
from collections.abc import Callable

def debug(func:Callable) -> Callable:
    """Декоратор, который раскладывает все по полочкам"""
    def wrapper(*args, **kwargs) ->Callable:
        print('Вызывается функция {}'.format(func.__name__))
        result = func(*args, **kwargs)
        print('{func} вернула значение {res}'.format(func=func.__name__, res=result))
        print(result, '\n')
        return result
    return wrapper

@debug
def greeting(name:str, age=None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
