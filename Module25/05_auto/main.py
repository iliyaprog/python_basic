import math

class Auto:
    all_distance = 0

    def __init__(self, x, y, angle):
        self.__x = x
        self.__y = y
        self.__angle = angle

    def move(self, distance):
        self.__x += distance * math.cos(self.__angle)
        self.__y += distance * math.sin(self.__angle)
        print('Поехали')
        self.all_distance += distance

    def change_angle(self, new_angle):
        self.__angle = math.radians(new_angle)

    def getAuto_x(self):
        return self.__x

    def getAuto_y(self):
        return self.__x


class Bus(Auto):
    count_passenger = 0
    money = 0
    list_passenger = []
    dict_distance = {}

    def enter(self, number_passenger):
        for i in range(self.count_passenger + 1, self.count_passenger + number_passenger + 1):
            self.list_passenger.append(i)
        self.count_passenger += number_passenger
        self.money += number_passenger * 10

    def out(self, number_passenger):
        print('В автобусе сейчас пассажиры под номером', end=' ')
        print(self.list_passenger)
        print('Какие пассажиры выходят?')

        for _ in range(number_passenger):
            i_passenger = int(input())
            self.list_passenger.remove(i_passenger)
            if self.dict_distance[i_passenger] > 10:
                ratio = self.dict_distance[i_passenger] // 10
                self.money += ratio * 10


    def count_distance(self, distance):
        for i_people in self.list_passenger:
            if i_people not in self.dict_distance.keys():
                self.dict_distance[i_people] = distance
            else:
                self.dict_distance[i_people] += distance

super_bus = Bus(0, 0, 0)

choice = 'work'
while choice != 'end':
    passengers = int(input('Сколько человек зашло в автобус?: '))
    super_bus.enter(number_passenger=passengers)

    angly_bus = int(input('Введите направление в градусах: '))
    super_bus.change_angle(new_angle=angly_bus)

    distance_bus = int(input('Введите расстояние: '))
    super_bus.move(distance=distance_bus)
    super_bus.count_distance(distance=distance_bus)

    print('Доехали до места. Мы находимся по координатам {} {}'.format(super_bus.getAuto_x(), super_bus.getAuto_y()))
    out_passenger = int(input('Сколько человек выходит?:'))
    if out_passenger > 0:
        super_bus.out(number_passenger=out_passenger)

    choice = input('Продолжаем? (work/end: )')
    if choice == 'end':
         while len(super_bus.list_passenger) > 0:
            print('Ты не выгрузил всех пассажиров')
            super_bus.out(len(super_bus.list_passenger))

print('Заработано {}. Всего было пассажиров {}. Проехал {}'.format(
    super_bus.money, len(super_bus.dict_distance), super_bus.all_distance)
)



