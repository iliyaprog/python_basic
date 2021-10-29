import random

class Parents:
    def __init__(self, name, age, list_children):
        self.name = name
        self.age = age
        self.list_children = list_children

    def my_name(self):
        print('Меня зовут {}\n'
              'Мне {} лет\n'
              'У меня {} детей\n'.format(self.name, self.age, len(self.list_children)))

    def calm(self, child):
        child.state = 'Спокойствие'

    def food_intake(self, child):
        child.satiety = 'Сыт'

    def calm_child(self, child):
        child.state = 'Спокойствие'

class Children:
    def __init__(self, name, age, state, satiety):
        self.name = name
        self.age = age
        self.state = state
        self.satiety = satiety

    def print_child(self, child):
        print('{} {} и {}\n'.format(child.name, child.satiety, child.state))

children_state = ('Злится', 'Спокоен')
children_satiety = ('Сыт', 'Голоден')

children1 = Children('Роман', 7, random.choice(children_state), random.choice(children_satiety))
children2 = Children('Алекс', 6, random.choice(children_state), random.choice(children_satiety))
children3 = Children('Иван', 4, random.choice(children_state), random.choice(children_satiety))

childrens = [children1, children2, children3]
parent1 = Parents('Альберт Эйнштейн', 40, childrens)

parent1.my_name()
for j_child in childrens:
    j_child.print_child(j_child)
print()


for i_child in childrens:
    if i_child.satiety == 'Голоден':
        print('{} идет кормить {}'.format(parent1.name, i_child.name))
        parent1.food_intake(i_child)
        i_child.print_child(i_child)

    if i_child.state == 'Злится':
        print('{} идет успокаивать {}'.format(parent1.name, i_child.name))
        parent1.calm_child(i_child)
        i_child.print_child(i_child)

for children in childrens:
    children.print_child(children)