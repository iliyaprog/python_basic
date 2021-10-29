first_file = open('first_tour.txt', 'r')
line_list = []

for i_line in first_file:
    line_list.append(i_line)

second_file = open('second_tour.txt', 'w')
second_file.write('Second tour\n')

new_dict = {}

for i_elem in line_list:
    if i_elem != line_list[0]:
        i = list((i_elem).split())
        if int(i[2]) >= int(line_list[0]):
            new_dict[i[2]] = i[0:2]

for i_players in (sorted((new_dict), reverse=True)):
    line = new_dict[i_players][0] + ' ' + new_dict[i_players][1] + ' ' + i_players
    second_file.write(line + '\n')






