import logging
formatter = logging.Formatter('%(message)s')

def setup_logger(name, file_log, level=logging.INFO):
    handler = logging.FileHandler(file_log)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

count_line = 0
sym_sum = 0

with open('people.txt', 'r') as start_file:
    for i_line in start_file:
        try:
            length = len(i_line)
            count_line += 1
            if i_line.endswith('\n'):
                length -= 1
            if length < 3:
                raise BaseException
            sym_sum += length
        except BaseException:
            errors_logger = setup_logger('errors', 'errors.log', logging.ERROR)
            errors_logger.error('В ' + str(count_line) + ' строке меньше 2-х символов')

info_logger = setup_logger('info', 'info.log')
info_logger.info('Всего символов ' + str(sym_sum))
