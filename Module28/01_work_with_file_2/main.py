import os

class File:

    """Контекст менеджер, создающий и читающий файлы"""

    def __init__(self, file: os.path) -> None:
        print('Начинаем работу:')
        self.__file = file

    def __enter__(self) -> 'File':
        check_file = os.path.exists(self.__file)
        if check_file is False:
            print('Такого файла не существует')
            self.work_file = open(self.__file, 'w+')
            new_str = input('Введите сообщение для нового файла: ')
            self.work_file.write(new_str)
            self.work_file.close()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return True

    def readlines(self):
        my_file = open(self.__file, 'r')
        for i_line in my_file.readlines():
            print(i_line)




way_folder = str(input(
    f'Введите путь до каталога (через пробел): \n'))
testpath = way_folder.replace(' ', '/')

abs_path = os.path.abspath('/' + testpath)
print(abs_path)

with File(abs_path) as new_file:
    new_file.readlines()
    print('Работа программы завершена')