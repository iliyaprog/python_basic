import os
from collections.abc import Iterable

def get_files_pass(path) -> None:
    for i_elem in os.listdir(path):
        way = os.path.abspath(path + os.path.join('\\', i_elem))
        list_file.append(way)

def my_generator() -> Iterable:
    for i in list_file:
        yield i

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


    all_path = my_generator()

    for i in all_path:
        print(i)


