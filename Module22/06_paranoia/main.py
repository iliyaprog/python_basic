def cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 52] if sym != ' ' else ' ') for sym in string
                 if sym != '\n']
    new_list = ''
    for i_char in char_list:
        new_list += i_char
    new_list += '\n'
    return new_list

file_name = open('text.txt', 'r')
end_file = open('cipher_text.txt', 'w')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
line_number = 1

for i in file_name:
    new_str = cipher(i, line_number)
    end_file.write(new_str)
    line_number += 1

file_name.close()
end_file.close()
