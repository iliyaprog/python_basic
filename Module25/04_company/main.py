import logging

formatter = logging.basicConfig(filename='salary.log')


def setup_logger(name, level=logging.ERROR):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return str(self.__name)

    def get_surname(self):
        return str(self.__surname)

class Employee(Person):

    def salary_people(self):
        salary = i_people.salary()
        return salary


class Manager(Employee):

    def salary(self):
        manager_salary = 13000
        return manager_salary

class Agent(Employee):

    def i_sales(self):
        sales = {'Mihail': 100000, 'Kolya': 120000, 'Oksana': 92000}
        sale = sales[i_people.get_name()]
        return sale

    def salary(self):
        agent_salary = 5000 + i_people.i_sales() * 0.05
        return agent_salary


class Worker(Employee):
    def i_work(self):
        hours = {'Oleg': 160, 'Alex': 172, 'Kirill': 170}
        work = hours[i_people.get_name()]
        return work

    def salary(self):
        worker_salary = 100 * i_people.i_work()
        return worker_salary


people1 = Manager('Ivan', 'Ivanov', 28)
people2 = Manager('Elena', 'Agafonova', 30)
people3 = Manager('Oleg', 'Boyarov', 24)
people4 = Agent('Mihail', 'Petrov', 32)
people5 = Agent('Kolya', 'Nikolaev', 35)
people6 = Agent('Oksana', 'Fedorova', 21)
people7 = Worker('Oleg', 'Petrov', 28)
people8 = Worker('Alex', 'Kotov', 31)
people9 = Worker('Kirill', 'Kirillov', 25)

list_people = [people1, people2, people3, people4, people5, people6, people7, people8, people9]
for i_people in list_people:
    i_salary = i_people.salary_people()
    info_log = setup_logger('person', level=logging.INFO)
    info_log.info('{i_name} {i_surname} заработал: {summ}'.format(
        i_name=i_people.get_name(),
        i_surname=i_people.get_surname(),
        summ=i_salary
    ))




