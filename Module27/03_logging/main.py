import math
import logging
from typing import Any
from collections.abc import Callable

formatter = logging.basicConfig(filename='result.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def setup_logger(name, log_file, level=logging.INFO) -> logging:

    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

def my_logging(func:Callable) -> Callable:
    """Декоратор, вызывающий логгер"""
    def wrapper(*args, **kwargs):
        end_result = func(*args, **kwargs)

        if end_result.__class__ == type:
            logger = setup_logger(name='error_log', log_file='result.log', level=logging.ERROR)
            logger.error('Error')

        else:
            logger = setup_logger(name='info_log', log_file='result.log')
            logger.info(end_result)

        return logger
    return wrapper


@my_logging
def sqrt(elem) ->Any:
    try:
        result = math.sqrt(elem)
    except: result = ValueError
    return result

list_number = [4, 9, 16, -2, 64, 81, -11, 121]
for i_elem in list_number:
    sqrt(i_elem)



