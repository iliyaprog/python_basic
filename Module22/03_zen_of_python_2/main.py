def minimum(dictionary):
    new_minimum = {}
    for i_key in dictionary:
        if new_minimum == {}:
            new_minimum = {i_key: dictionary[i_key]}
            min_value = dictionary[i_key]
        elif dictionary[i_key] < min_value:
            new_minimum = {i_key: dictionary[i_key]}
            min_value = dictionary[i_key]

    return new_minimum

zen_file = open('zen.txt', 'r')

count_dict = {}
count_line = 0
count_word = 0
count_alphabet = 0

for i_line in zen_file:
    count_line += 1
    words = i_line.split()
    for i_word in words:
        count_word += 1
    for i_elem in i_line:
        if i_elem.isalpha():
            count_alphabet += 1
            if i_elem in count_dict:
                count_dict[i_elem] += 1
            else:
                count_dict[i_elem.lower()] = 1

print('Количество строк', count_line)
print('Количество букв', count_word)
print('Количество букв:', count_alphabet)
rarest = minimum(count_dict)
for i in rarest:
    print('Самая редкая буква', i, ': встречается', rarest[i], 'раз')

zen_file.close()