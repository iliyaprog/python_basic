import os

def all_file(file):
    if os.path.isdir(file):
        count_subdirectory.append(file)
        for i_elem in os.listdir(file):
            all_file(file + os.path.join('\\', i_elem))
    else:
        all_file_way.append(file)

way_folder = str(input(
    f'Введите путь до каталога (через пробел): \n'))
testpath = way_folder.replace(' ', '/')

abs_path = os.path.abspath('/' + testpath)
print(abs_path)
check_file = os.path.exists(abs_path)

all_file_way = []
count_subdirectory = []

if check_file:
    if os.path.isdir(abs_path):
        file_size = 0
        all_file(abs_path)
        for i_file in all_file_way:
            file_size += (os.path.getsize(i_file) / 1024)
        print('Размер этого каталога (в кБ):', file_size)
        print('Количество файлов:', len(all_file_way))
        print('Количество подкаталогов:', (len(count_subdirectory) - 1))

    else:
        file_size = (os.path.getsize(abs_path) / 1024)
        print('Размер этого файла(в кБ):', file_size)
        print('Количество файлов: 1')


