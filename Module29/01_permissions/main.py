import functools
from typing import Callable
import logging


formatter = logging.basicConfig(filename='result.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def setup_logger(name: str, level) -> logging:

    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger


user_permissions = ['admin']

def check_permission(person) -> Callable:

    def check(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if person in user_permissions:
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError
            except PermissionError:
                logger = setup_logger(name='PermissionError', level=logging.ERROR)
                logger.error('У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(func.__name__))

        return wrapper
    return check

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
