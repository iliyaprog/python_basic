import os
from collections.abc import Iterable

import logging
formatter = logging.basicConfig(filename='result.log', filemode='w')
def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

def get_files_pass(path) -> None:
    for i_elem in os.listdir(path):
        way = os.path.abspath(path + os.path.join('\\', i_elem))
        list_file.append(way)

def my_generator(i_list) -> Iterable:
    count_line = 0
    for i_path in i_list:
        if i_path.endswith('.py'):
            with open(i_path, 'r', encoding='utf-8') as file:
                for i_line in file.readlines():
                    space_flag = True
                    for i_symbol in i_line[:-2]:
                        if i_symbol != ' ':
                            space_flag = False
                            break
                    if i_line.startswith('#') or space_flag == True:
                        pass
                    else:
                        count_line += 1
                        yield i_line

    end_log = setup_logger('end_log')
    end_log.info(f'Всего строк {count_line}'.format(count_line))


way_folder = str(input(
    f'Введите путь до каталога (через пробел): \n'))
testpath = way_folder.replace(' ', '/')

abs_path = os.path.abspath('/' + testpath)
print(abs_path)
check_file = os.path.exists(abs_path)

list_file = []
if check_file:
    list_file.append(abs_path)
    flag = False
    while flag == False:
        count_file = 0
        for i_elem in list_file:
            if os.path.isdir(i_elem):
                count_file += 1
                get_files_pass(i_elem)
                list_file.remove(i_elem)

        if count_file == 0:
            flag = True

    end_list = my_generator(list_file)

    for i in end_list:
        info_log = setup_logger('line')
        info_log.info(i)




