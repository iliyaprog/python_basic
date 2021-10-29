import logging
formatter = logging.basicConfig(filename='result.log', filemode='w')

from collections.abc import Iterable

def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

class Iterator:
    def __init__(self, number: int) -> None:
        self.number = number
        self.counter = 0

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> int:
        self.counter += 1
        if self.counter > self.number:
            raise StopIteration
        result = self.counter ** 2
        return result

def sequence_square(number: int) -> Iterable[int]:
    for i in range(1, number + 1):
        yield (i ** 2)


n = int(input('Введите число: '))

sequence_1 = (num ** 2 for num in range(1, n + 1))
for i_value in sequence_1:
    info_log = setup_logger('cycle')
    info_log.info(i_value)


sequence_2 = Iterator(n)
for i_value in sequence_2:
    info_log = setup_logger('iter')
    info_log.info(i_value)

sequence_3 = sequence_square(n)
for i_value in sequence_3:
    info_log = setup_logger('generator')
    info_log.info(i_value)








