class Property:
    def __init__(self, worth):
        self.worth = worth

class Appartment(Property):
    def taxes_appartament(self):
        taxes = self.worth / 1000
        return taxes


class Car(Property):
    def taxes_car(self):
        taxes = self.worth / 200
        return taxes

class CountryHouse(Property):
    def taxes_countryhouse(self):
        taxes = self.worth / 500
        return taxes

worth_appartment = int(input('Стоимость квартиры: '))
worth_car = int(input('Стоимость машины: '))
worth_house = int(input('Стоимость загородного дома: '))
money = int(input('Сколько у вас денег: '))


appartment = Appartment(worth_appartment)
car = Car(worth_car)
country_house = CountryHouse(worth_house)


taxes = []
print('Налог на квартиру =', appartment.taxes_appartament())
taxes.append(appartment.taxes_appartament())
print('Налог на машину =', car.taxes_car())
taxes.append(car.taxes_car())
print('Налог на загородный дом =', country_house.taxes_countryhouse())
taxes.append(country_house.taxes_countryhouse())
print('Общая сумма налога =', sum(taxes))


if money >= sum(taxes):
    print('Денег на уплату налогов достаточно')
else:
    print('У тебя не хватает {} денег. Придется еще поработать'.format(sum(taxes) - money))