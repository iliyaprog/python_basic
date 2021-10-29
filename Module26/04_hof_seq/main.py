# Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))

from collections.abc import Iterable
import logging
formatter = logging.basicConfig(filename='result.log', filemode='w')

def setup_logger(name, level=logging.INFO) -> logging:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

class Iterator:
    def __init__(self, index: int) -> None:
        self.index = index
        self.counter = 0
        self.first_number = 1
        self.second_number = 1

    def __iter__(self) -> Iterable[int]:
        self.counter = 0
        return self

    def __next__(self) -> int:
        self.counter += 1
        if self.counter > self.index:
            raise StopIteration
        if self.counter == 1 or self.counter == 2:
            result = 1
        else:
            first_variable = Iterator(self.counter - 1)
            for i in first_variable:
                i_number = i
            first_iterator = Iterator(self.counter - i)
            for i in first_iterator:
                first_num = i


            second_variable = Iterator(self.counter - 2)
            for i in second_variable:
                i_number = i
            second_iterator = Iterator(self.counter - i)
            for i in second_iterator:
                second_num = i

            result = first_num + second_num
        return result

numbers = [1, 1]
my_iterator = Iterator(21)
for i in my_iterator:
    info_logger = setup_logger('result')
    info_logger.info(i)
