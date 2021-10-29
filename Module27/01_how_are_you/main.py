from typing import Any
from collections.abc import Callable

def how_are_you(func:Callable) -> Callable:
    """Декоратор, который мешает работе функции"""

    def wrapper(*args, **kwargs) -> Any:
        answer = input('Как дела?\n')
        print('А у меня не очень\n'
              'Вот твоя функция:')
        result = func(*args, **kwargs)
        return result
    return wrapper

@how_are_you
def test(i_list) -> int:
    summ = 0
    for i in i_list:
        summ += i
    return summ


list_list = [1, 2, 3, 4, 5]
result = test(list_list)
print(result)