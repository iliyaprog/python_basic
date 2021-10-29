import logging
formatter = logging.Formatter('%(message)s')

def setup_logger(name, level=logging.ERROR):
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

count_line = 0
with open('registrations.txt', 'r', encoding='utf-8') as file:
        for i_line in file.readlines():
            try:
                count_line += 1
                reserve_line = i_line
                i_line = list(i_line.split())
                if len(i_line) < 3:
                    raise IndexError
                if not i_line[0].isalpha():
                    raise NameError
                if ('@' or '.') not in i_line[1]:
                    raise SyntaxError
                if int(i_line[2]) < 10 or int(i_line[2]) > 99:
                    raise ValueError

            except IndexError:
                errors_logger = setup_logger('errors')
                errors_logger.error('В строке {} не хватает данных'.format(count_line)
                                    + ': ' + reserve_line)

            except NameError:
                errors_logger = setup_logger('errors')
                errors_logger.error('В строке {} неправильно введено имя'.format(count_line)
                                    + ': ' + reserve_line)

            except SyntaxError:
                errors_logger = setup_logger('errors')
                errors_logger.error('В строке {} неправильно введен mail'.format(count_line)
                                    + ': ' + reserve_line)

            except ValueError:
                errors_logger = setup_logger('errors')
                errors_logger.error('В строке {} ошибка возраста'.format(count_line)
                                    + ': ' + reserve_line)

            else:
                with open('registrations_good.log', 'a') as good_file:
                    good_file.write(reserve_line)

