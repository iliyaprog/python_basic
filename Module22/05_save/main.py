import os

text = str(input(f'Введите строку: \n'))
way = str(input(
    f'Куда хотите сохранить документ? Введите последовательность папок (через пробел): \n'))
filename = str(input(f'Введите имя файла: \n'))

testpath = way.replace(' ', '/')
newpath = str(testpath + '/' + filename)
print(newpath)
abs_path = os.path.abspath('/' + newpath)
print(abs_path)
check_file = os.path.exists(abs_path)
print(check_file)
if check_file:
    choice = input(f'Вы действительно хотите перезаписать файл? (да/нет) \n')
    if choice == 'да':
        end_file = open(abs_path, 'w')
        end_file.write(text)
        print(f'Файл успешно перезаписан!')
        end_file.close()
    else:
        print(f'Файл не сохранен')

else:
    end_file = open(abs_path, 'w+')
    end_file.write(text)
    print(f'Файл успешно сохранён!')
    end_file.close()

