import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def print_coordinartes(self):
        print('x = ', self.x)
        print('y = ', self.y)
        print('R = ', self.radius)

    def square(self):
        s = (math.pi *self.radius) ** 2
        print(s)

    def circumference(self):
        l = math.pi * self.radius * 2
        print(l)

    def increase(self):
        k = int(input('Во сколько раз увеличить?: '))
        self.radius = k * self.radius

    def do_intersect(self, other):
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return abs(self.radius - other.radius) <= dist <= self.radius + other.radius

count_circle = int(input('Сколько будет окружностей?: '))
list_circle = []
count = 0

while count != count_circle:
    count += 1
    x = int(input('Введите координаты центра окружности {}: \nx = '.format(count)))
    y = int(input('y = '))
    radius = int(input('Радиус окружности: '))
    circle = Circle(x, y, radius)
    list_circle.append(circle)


while True:
    number_circle = int(input('Выберете нужную окружность: '))
    choice = int(input('Выберете действие\n'
                       '1 - показать координаты и радиус окружности\n'
                       '2 - показать площадь окружности\n'
                       '3 - показать длину окружности\n'
                       '4 - увеличить радиус окружности\n'
                       '5 - пересекается ли окружность с другой окружностью\n'
                       '6 - завершить программу программу\n'))
    if choice == 1:
        list_circle[number_circle - 1].print_coordinartes()
    elif choice == 2:
        list_circle[number_circle - 1].square()
    elif choice == 3:
        list_circle[number_circle - 1].circumference()
    elif choice == 4:
        list_circle[number_circle - 1].increase()
    elif choice == 5:
        second_circle = int(input('Выберете еще одну окружность: '))

        while second_circle == number_circle or second_circle > len(list_circle):
            if second_circle == number_circle:
                print('2 раза выбрана одна окружность')
            elif second_circle > len(list_circle):
                print('Такой окружности не существует')
            second_circle = int(input('Выберете еще одну окружность: '))

        if (list_circle[number_circle - 1].do_intersect(list_circle[second_circle - 1])):
            print('Окружности пересекаются')
        else:
            print('Окружности не пересекаются')
    elif choice == 6:
        print('Программа завершена')
        break



