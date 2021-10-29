class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Vapor()
        if isinstance(other, Earth):
            return Dirt()
        else:
            None

class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        else:
            None

class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Vapor()
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Earth):
            return Lava()
        else:
            None

class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        else:
            None

class Storm():
    def __str__(self):
        return 'Шторм'

class Vapor():
    def __str__(self):
        return 'Пар'

class Dirt():
    def __str__(self):
        return 'Грязь'

class Lightning():
    def __str__(self):
        return 'Молния'

class Dust():
    def __str__(self):
        return 'Пыль'

class Lava():
    def __str__(self):
        return 'Лава'


water = Water()
fire = Fire()
air = Air()
earth = Earth()

list_element1 = [water, fire, air, earth]
list_element2 = [water, fire, air, earth]

for i_elem in list_element1:
    for j_elem in list_element2:
        print(i_elem + j_elem)

