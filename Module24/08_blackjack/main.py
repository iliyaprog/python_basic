import random

class Players:
    points = 0
    player_cards = []

    def __init__(self, name):
        self.name = name

    def number(self, number_card):
        self.points += number_card

    def picture(self):
        self.points += 10

    def ace(self):
        if self.points > 10:
            self.points += 1
        else:
            self.points += 11

pack = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз'] * 4

player1 = Players('игрок1')
croupier = Players('крупье')
player2 = Players('игрок2')
player3 = Players('игрок3')
player_list = [player1, player2, player3, croupier]

for i_player in player_list:
    print('Играет {}: '.format(i_player.name))
    while len(i_player.player_cards) != 2:
        index_card = random.randint(0, len(pack) - 1)
        card = pack[index_card]
        del pack[index_card]
        i_player.player_cards.append(card)

    if i_player.player_cards == ['туз', 'туз']:
        user_points = 21
    else:
        for i_card in i_player.player_cards:
            if str(i_card).isdigit():
                i_player.number(i_card)
            elif i_card == 'туз':
                i_player.ace()
            else:
                i_player.picture()

    print('Карты: {}, {}'.format(i_player.player_cards[0], i_player.player_cards[1]))
    print('Количество очков', i_player.points)

    choice = ''
    while i_player.points < 21:
        choice = input('хватит или еще?\n')
        if choice == 'еще':
            index_card = random.randint(0, len(pack) - 1)
            card = pack[index_card]
            del pack[index_card]
            print(card)

            if str(card).isdigit():
                i_player.number(card)
            elif card == 'туз':
                i_player.ace()
            else:
                i_player.picture()

            print('Количество очков', i_player.points)

        elif choice == 'хватит':
            break

    if i_player.points > 21:
        print('Перебор\n')
    elif i_player.points == 21:
        print('Очко\n')
    else:
        print('Количество очков {}\n'.format(i_player.points))

max_point = 0
for j_player in player_list:
    if j_player.points > max_point and j_player.points <= 21:
        max_point = j_player.points
        winners = [j_player]
    elif j_player.points == max_point:
        winners.append(j_player)

for i in winners:
    print('Победитель {}'.format(i.name))


