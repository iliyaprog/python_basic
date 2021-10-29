zen_dict = {}
i = 0

with open('zen.txt', 'r') as f:
    for i_line in f.readlines():
        zen_dict[i] = i_line
        i += 1

revese_text = sorted(zen_dict.keys(), reverse=True)
for i_key in revese_text:
    print(zen_dict[i_key], end='')


