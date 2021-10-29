import logging
formatter = logging.Formatter('%(message)s')

def setup_logger(name, level=logging.INFO):
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

result = 0
count_line = 0

try:
    with open('calc.txt', 'r') as file:

        for i_line in file.readlines():
            count_line += 1
            try:
                i_line = list(i_line.split())
                if i_line[1] == '+':
                    a = int(i_line[0]) + int(i_line[2])
                elif i_line[1] == '-':
                    a = int(i_line[0]) - int(i_line[2])
                elif i_line[1] == '/':
                    a = int(i_line[0]) / int(i_line[2])
                elif i_line[1] == '//':
                    a = int(i_line[0]) // int(i_line[2])
                elif i_line[1] == '%':
                    a = int(i_line[0]) % int(i_line[2])
                elif i_line[1] == '*':
                    a = int(i_line[0]) * int(i_line[2])
                elif i_line[1] == '**':
                    a = int(i_line[0]) ** int(i_line[2])
                else:
                    raise SyntaxError
                result += a
            except SyntaxError:
                errors_logger = setup_logger('errors', logging.ERROR)
                errors_logger.error('Ошибка в {} строке'.format(count_line))

    info_logger = setup_logger('info')
    info_logger.info('Сумма результатов ' + str(result))

except FileNotFoundError:
    errors_logger = setup_logger('errors', logging.ERROR)
    errors_logger.error('Исходного файла не существует')
