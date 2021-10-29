import requests
import json
from typing import Dict

"""Функция которая создает новый словарь. Записываются сезон, эпизод и запускается счетчик"""
def func_new_dict(old_dict: Dict) -> Dict:
    new_dict = dict()
    new_dict['season'] = old_dict['season']
    new_dict['episode'] = old_dict['episode']
    new_dict['counter_death'] = 1

    return new_dict


first_reg = requests.get('https://www.breakingbadapi.com/api/')
data = json.loads(first_reg.text)

for i_key in data:
    second_reg = requests.get(data[i_key])

data_death = json.loads(second_reg.text)

all_list = []

"""Здесь создается список словарей для каждого эпизода"""
for i in data_death:

    if all_list == []:
        new_death_episode = func_new_dict(i)
        all_list.append(new_death_episode)
    else:
        check = False
        for i_dict in all_list:

            if int(i_dict['season']) == int(i['season']) and int(i_dict['episode']) == int(i['episode']):
                i_dict['counter_death'] += 1
                check = True
                break

        if check == False:
            new_death_episode = func_new_dict(i)
            all_list.append(new_death_episode)

"""Здесь определяется в каком эпизоде было наибольшее количество смертей"""
max_episode = {'season': 0, 'episode': 0, 'counter_death': 0}
for i_episode in all_list:
    if i_episode['counter_death'] > max_episode['counter_death']:
        max_episode = i_episode

"""Тут добавляется id серии"""
episode_reg = requests.get(data['episodes'])
data_episodes = json.loads(episode_reg.text)
for i_elem in data_episodes:
    if int(i_elem['season']) == int(max_episode['season'])\
            and int(i_elem['episode']) == int(max_episode['episode']):
        max_episode['episode_id'] = i_elem['episode_id']
        break

"""Тут добавляется список погибших"""
max_episode['death'] = []
for i_death in data_death:
    if int(i_death['season']) == int(max_episode['season']) \
            and int(i_death['episode']) == int(max_episode['episode']):
        max_episode['death'].append(i_death['death'])


print(max_episode)

with open('new_file.txt', 'w+') as file:
    json.dump(max_episode, file, indent=4)

