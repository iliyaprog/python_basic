import random

class Human():

    def __init__(self, name,  satiety):
        self.satiety = satiety
        self.name = name

    def food_intake(self):
            print('{}, надо поесть'.format(self.name))
            if my_house.food < 10:
                i_human.shop()
            else:
                self.satiety += 10
                my_house.food -= 10

    def work(self):
        print('{}, нужно поработать'.format(self.name))
        self.satiety -= 10
        my_house.money += 10

    def play(self):
        print('{}, можно и поиграть'.format(self.name))
        self.satiety -= 10

    def shop(self):
        print('{}, нужно сходить в магазин'.format(self.name))
        if my_house.money < 10:
            i_human.work()
        else:
            my_house.money -= 10
            my_house.food += 10

class House():
    food = 50
    money = 0

def print_data():
    print('Сытость {} {}'.format(human1.name, human1.satiety))
    print('Сытость {} {}'.format(human2.name, human2.satiety))
    print('Деньги {}'.format(my_house.money))
    print('Еда {}\n'.format(my_house.food))

human1 = Human('Артем', 50)
human2 = Human('Битлджус', 50)
my_house = House

residents = [human1, human2]

count_day = 0
while count_day < 365:
    count_day += 1
    print('День {}:'.format(count_day))
    for i_human in residents:
        number_cube = random.randint(1, 6)
        if i_human.satiety < 20:
            i_human.food_intake()
        elif my_house.food < 10:
            i_human.shop()
        elif my_house.money < 50:
            i_human.work()
        elif number_cube == 1:
            i_human.work()
        elif number_cube == 2:
            i_human.food_intake()
        else:
            i_human.play()

        if i_human.satiety <= 0:
            print('{} умер от голода'.format(i_human.name))
            break
    print_data()