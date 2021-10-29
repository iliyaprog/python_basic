import functools
from typing import Callable


def decorator_for_any_decorator(decorator_enhance: Callable) -> Callable:
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker

@decorator_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор', dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)
decorated_function("Юзер", 101)
