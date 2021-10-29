import random
import logging

formatter = logging.basicConfig(filename='karma.log', filemode='w')

def setup_logger(name, level=logging.ERROR):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

class Person:
    __karma = 0
    __end_karma = 500

    def get_karma(self):
        return self.__karma

    def get_end_karma(self):
        return self.__end_karma

    def wastle_karma(self, i_karma):
        self.__karma -= i_karma

    def one_day(self):
        try:
            chance_of_error = random.randint(1, 10)
            if chance_of_error == 6:
                raise random.choice(list_error)

            else:
                a = random.randint(1, 7)
                self.__karma += a
                if self.__karma >= self.__end_karma:
                    return True
                else:
                    print('На {} день ты получил {} кармы. До просветления осталось {}'
                        .format(count_day, a, (self.__end_karma - self.__karma)))
                    return False

        except KillError:
            me.wastle_karma(10)
            errors_logger = setup_logger('karma',)
            errors_logger.error('На {} день ты кого то убил. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))
            print('На {} день ты кого то убил. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))



        except DrunkError:
            me.wastle_karma(6)
            errors_logger = setup_logger('karma')
            errors_logger.error('На {} день ты напился. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))
            print('На {} день ты напился. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))


        except CarCrashError:
            me.wastle_karma(7)
            errors_logger = setup_logger('karma')
            errors_logger.error('На {} день ты разбил машину. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))
            print('На {} день ты разбил машину. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))


        except GluttonyError:
            me.wastle_karma(4)
            errors_logger = setup_logger('karma')
            errors_logger.error('На {} день ты объелся. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))
            print('На {} день ты объелся. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))


        except DepressionError:
            me.wastle_karma(5)
            errors_logger = setup_logger('karma')
            errors_logger.error('На {} день у тебя была депрессия. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))
            print('На {} день у тебя была депрессия. До просвещения осталось {} кармы'.format(count_day,
                me.get_end_karma() - me.get_karma()))

class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass


me = Person()
list_error = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]

count_day = 0
education = False

while education != True:
    count_day += 1
    education = me.one_day()

print('Ты достиг просвещения за {} дней'. format(count_day))


