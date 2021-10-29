import random

import logging
formatter = logging.Formatter('%(message)s')

summ_number = 0
count_operation = 0

try:
    while summ_number < 777:
        count_operation += 1
        user_number = int(input('Введите число: '))
        summ_number += user_number
        a = random.randint(0, 13)
        if a == 13:
            raise BaseException
        with open('result.txt', 'a', encoding='utf-8') as file:
            file.write(str(user_number) + ' сумма равна ' + str(summ_number))
            file.write('\n')

except BaseException:
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    logger.error('Не повезло в {} строке'.format(count_operation))