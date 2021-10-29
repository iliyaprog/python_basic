def arithmetic(line):
    try:
        reserve_line = line
        line = list(line.split())
        if line[1] == '+':
            a = int(line[0]) + int(line[2])
        elif line[1] == '-':
            a = int(line[0]) - int(line[2])
        elif line[1] == '/':
            a = int(line[0]) / int(line[2])
        elif line[1] == '//':
            a = int(line[0]) // int(line[2])
        elif line[1] == '%':
            a = int(line[0]) % int(line[2])
        elif line[1] == '*':
            a = int(line[0]) * int(line[2])
        elif line[1] == '**':
            a = int(line[0]) ** int(line[2])
        else:
            raise SyntaxError
    except SyntaxError:
        print('Ошибка в {} строке:'.format(count_line), reserve_line)
        a = error_func()
    finally: return a

def error_func():
    choice = input('Хотите исправить ошибку? да/нет: ')
    while choice not in ['да', 'нет']:
        choice = input('Ответ должен быть "да" или "нет": ')
    if choice == 'да':
        corrected_line = input('Введите исправленную строку: ')
        result_func = arithmetic(corrected_line)
        return result_func
    elif choice == 'нет':
        return 0

result = 0
count_line = 0

try:
    with open('calc.txt', 'r') as file:

        for i_line in file.readlines():
            count_line += 1
            result += arithmetic(i_line)

    print('Сумма результатов', result)

except FileNotFoundError:
    print('Исходного файла не существует')
