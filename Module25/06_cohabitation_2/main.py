import random

class House():

    def __init__(self, money, food, food_for_cat, dirt, coat):
        self.__money = money
        self.__food = food
        self.__food_for_cat = food_for_cat
        self.__dirt = dirt
        self.__coat = coat

    def get_money(self):
        return self.__money

    def get_food(self):
        return self.__food

    def get_food_for_cat(self):
        return self.__food_for_cat

    def get_dirt(self):
        return self.__dirt

    def get_coat(self):
        return self.__coat

    def append_food(self, i_food):
        self.__food += i_food
        self.__money -= i_food

    def append_food_for_cat(self):
        self.__food_for_cat += 20
        self.__money -= 20

    def append_money(self):
        self.__money += 150

    def append_coat(self):
        self.__coat += 1
        self.__money -= 350

    def append_dirt(self):
        self.__dirt += 5

    def wastle_dirt(self, i_dirt):
        self.__dirt -= i_dirt

    def wastle_food_for_cat(self, i_food):
        self.__food_for_cat -= i_food

    def wastle_food(self, i_food):
        self.__food -= i_food

class Husband():

    def __init__(self, name, satiety, happy):
        self.__name = name
        self.__satiety = satiety
        self.__happy = happy

    def get_name(self):
        return self.__name

    def get_satiety(self):
        return self.__satiety

    def get_happy(self):
        return self.__happy

    def food_intake(self):
        if my_house.get_food() >= 30:
            my_house.wastle_food(i_food=30)
            self.__satiety += 30
        elif 0 < my_house.get_food() < 30:
            self.__satiety += my_house.get_food()
            my_house.wastle_food(i_food=my_house.get_food())

    def waste_satiety(self):
        self.__satiety -= 10

    def play(self):
        self.__happy += 20
        husband.waste_satiety()

    def wastle_happy(self):
        self.__happy -= 10

    def work(self):
        my_house.append_money()
        husband.waste_satiety()

    def petting_cat(self):
        husband.waste_satiety()
        self.__happy += 5


class Wife():

    def __init__(self, name, satiety, happy):
        self.__name = name
        self.__satiety = satiety
        self.__happy = happy


    def get_name(self):
        return self.__name

    def get_satiety(self):
        return self.__satiety

    def get_happy(self):
        return self.__happy

    def food_intake(self):
        if my_house.get_food() >= 30:
            my_house.wastle_food(i_food=30)
            self.__satiety += 30
        elif 0 < my_house.get_food() < 30:
            self.__satiety += my_house.get_food()
            my_house.wastle_food(i_food=my_house.get_food())

    def waste_satiety(self):
        self.__satiety -= 10

    def petting_cat(self):
        wife.waste_satiety()
        self.__happy += 5

    def wastle_happy(self):
        self.__happy -= 10

    def cleaning(self):
        if my_house.get_dirt() > 100:
            my_house.wastle_dirt(i_dirt=100)
        else:
            my_house.wastle_dirt(i_dirt=my_house.get_dirt())
        wife.waste_satiety()

    def shop(self):
        if my_house.get_money() >= 120:
            i_food = 100
            my_house.append_food(i_food)
            if my_house.get_food_for_cat() < 50:
                my_house.append_food_for_cat()
        elif 0 < my_house.get_money() < 120:
            i_food = my_house.get_money() - 20
            my_house.append_food(i_food)
            if my_house.get_food_for_cat() < 20:
                my_house.append_food_for_cat()
        wife.waste_satiety()

    def buy_coat(self):
        my_house.append_coat()
        wife.waste_satiety()


class Cat():

    def __init__(self, name, satiety):
        self.__name = name
        self.__satiety = satiety

    def get_name(self):
        return self.__name

    def get_satiety(self):
        return self.__satiety

    def cat_sleep(self):
        self.__satiety -= 10

    def food_intake_cat(self):
        if my_house.get_food_for_cat() >= 10:
            my_house.wastle_food_for_cat(i_food=10)
            self.__satiety += 20
        elif 0 < my_house.get_food_for_cat() < 10:
            self.__satiety += my_house.get_food_for_cat() * 2
            my_house.wastle_food_for_cat(i_food=my_house.get_food_for_cat())

    def break_wallpaper(self):
        self.__satiety -= 10
        my_house.append_dirt()


my_house = House(money=100, food=50, food_for_cat=30, coat=0, dirt=0)
husband = Husband(name='Артем', satiety=50, happy=100)
wife = Wife(name='Анна', satiety=50, happy=100)
cat = Cat(name='Бегемот', satiety=50)

count_day = 0
while count_day < 365:
    count_day += 1
    print('Начался {} день'.format(count_day))
    my_house.append_dirt()

    if my_house.get_dirt() > 90:
        husband.wastle_happy()
        wife.wastle_happy()

    if husband.get_satiety() < 30 and my_house.get_food() > 0:
        print('{} ест'.format(husband.get_name()))
        husband.food_intake()
    elif husband.get_happy() < 30:
        husband_choice = random.randint(1, 2)
        if husband_choice == 1:
            print('{} играет'.format(husband.get_name()))
            husband.play()
        elif husband_choice == 2:
            print('{} гладит кота'.format(husband.get_name()))
            husband.petting_cat()
    elif my_house.get_money() < 200:
        print('{} работает'.format(husband.get_name()))
        husband.work()
    else:
        if my_house.get_food() > 10:
            husband_choice = random.randint(1, 4)
        else:
            husband_choice = random.randint(1, 3)

        if husband_choice == 1:
            print('{} работает'.format(husband.get_name()))
            husband.work()
        elif husband_choice == 2:
            print('{} играет'.format(husband.get_name()))
            husband.play()
        elif husband_choice == 3:
            print('{} гладит кота'.format(husband.get_name()))
            husband.petting_cat()
        elif husband_choice == 4:
            print('{} ест'.format(husband.get_name()))
            husband.food_intake()
    print('{}, сытость:{}, счастье:{}\n'.format(husband.get_name(), husband.get_satiety(), husband.get_happy()))


    if wife.get_satiety() < 30 and my_house.get_food() > 0:
        print('{} ест'.format(wife.get_name()))
        wife.food_intake()
    elif my_house.get_food() < 90:
        print('{} идет за покупками'.format(wife.get_name()))
        wife.shop()
    elif my_house.get_dirt() >= 100:
        print('{} убирается'.format(wife.get_name()))
        wife.cleaning()
    elif wife.get_happy() < 50:
        wife_choice = random.randint(1, 2)
        if wife_choice == 1 and my_house.get_money() > 350:
            print('{} покупает шубу'.format(wife.get_name()))
            wife.buy_coat()
        else:
            print('{} гладит кота'.format(wife.get_name()))
            wife.petting_cat()
    else:
        if my_house.get_money() > 350:
            wife_choice = random.randint(1, 5)
        else:
            wife_choice = random.randint(1, 4)

        if wife_choice == 1:
            print('{} ест'.format(wife.get_name()))
            wife.food_intake()
        elif wife_choice == 2:
            print('{} идет за покупками'.format(wife.get_name()))
            wife.shop()
        elif wife_choice == 3:
            print('{} убирается'.format(wife.get_name()))
            wife.cleaning()
        elif wife_choice == 4:
            print('{} гладит кота'.format(wife.get_name()))
            wife.petting_cat()
        elif wife_choice == 5:
            print('{} покупает шубу'.format(wife.get_name()))
            wife.buy_coat()
    print('{}, сытость:{}, счастье:{}\n'.format(wife.get_name(), wife.get_satiety(), wife.get_happy()))


    if cat.get_satiety() < 30 and my_house.get_food_for_cat() > 0:
        print('{} ест'.format(cat.get_name()))
        cat.food_intake_cat()
    else:
        if my_house.get_food_for_cat() > 0:
            cat_choice = random.randint(1, 3)
        else:
            cat_choice = random.randint(1, 2)

        if cat_choice == 1:
            print('{} спит'.format(cat.get_name()))
            cat.cat_sleep()
        elif cat_choice == 2:
            print('{} дерет обои'.format(cat.get_name()))
            cat.break_wallpaper()
        elif cat_choice == 3:
            print('{} ест'.format(cat.get_name()))
            cat.food_intake_cat()
    print('{}, сытость:{}\n'.format(cat.get_name(), cat.get_satiety()))

    print('В доме {} еды, {} еды для кота, {} денег {} грязи\n'.format(
        my_house.get_food(),
        my_house.get_food_for_cat(),
        my_house.get_money(),
        my_house.get_dirt()
    ))

print('За год куплено {} шуб'.format(my_house.get_coat()))
