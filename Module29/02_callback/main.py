import os
import functools
from typing import Callable


def check_file(path: os) -> bool:
    if os.path.exists(path):
        return True
    else:
        return False

def callback(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@callback
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


way_folder = str(input(
    f'Введите путь до каталога (через пробел): \n'))
testpath = way_folder.replace(' ', '/')

abs_path = os.path.abspath('/' + testpath)

route = check_file(abs_path)

if route:
    response = example()
    print('Ответ:', response)
else:
    print('Такого пути нет')

