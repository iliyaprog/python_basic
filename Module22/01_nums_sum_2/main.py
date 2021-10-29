summ = 0
with open('number.txt', 'r') as f:
    for i_line in f.readlines():
        for i_elem in i_line:
            if i_elem != ' ' and i_elem != '\n':
                summ += int(i_elem)

end_file = open('answer.txt', 'w+')
end_file.write(str(summ))

