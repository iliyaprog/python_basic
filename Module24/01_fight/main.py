import random
class Unit:
    health = 100

    def __init__(self, name):
        self.name = name

def fight(health_warrior):
    new_health = health_warrior - 20
    return new_health


unit_1 = Unit('Воин Света')
unit_2 = Unit('Воин Тьмы')

while (unit_1.health > 0) and (unit_2.health > 0):
    variable = random.randint(1, 2)
    if variable == 1:
        print('Силы Света атакуют')
        unit_2.health = fight(unit_2.health)
    else:
        print('Силы Тьмы атакуют')
        unit_1.health = fight(unit_1.health)
    print('Здоровье воина света', unit_1.health)
    print('Здоровье война тьмы', unit_2.health, '\n')

if unit_1.health > 0:
    print('Победа Сил Света')
else:
    print('Победа Сил Тьмы')


