import logging
formatter = logging.basicConfig(filename='result.log', filemode='w')

from collections.abc import Iterable

def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

"""Тут старый код"""

# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break

"""Тут новый код код"""

def generator(x_list: list, y_list: list) -> Iterable[int]:
    for x in x_list:
        for y in y_list:
            result = x * y
            info_logger = setup_logger('num_result')
            info_logger.info('{x_log} * {y_log} = {result_log}'.format(
                x_log=x,
                y_log=y,
                result_log=result))
            yield result

list_generator = generator(list_1, list_2)
for i_value in list_generator:
    if i_value == to_find:
        break


