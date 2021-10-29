alphabet = 'abcdefghijklmnopqrstuvwxyz'
count_eng = 0
source_file = open('text.txt', 'r', encoding='utf-8')
data = source_file.read()

dict_sym = {}
for i_data in data:
    if i_data.lower() in alphabet:
        count_eng += 1
        if i_data.lower() not in dict_sym:
            dict_sym[i_data.lower()] = 1
        else:
            dict_sym[i_data.lower()] += 1

privat_dict = {}
for i_key in dict_sym:
    privat_dict[i_key] = round(dict_sym[i_key] / count_eng, 3)

ban_list = []
sorted_dict = {}

for privat_i_key in sorted(privat_dict.keys()):
    sorted_dict[privat_i_key] = privat_dict[privat_i_key]

end_file = open('analysis.txt', 'w')

for i_sym in sorted(sorted_dict.values(), reverse=True):
    for sorted_i_key in sorted_dict.keys():
        if sorted_dict[sorted_i_key] == i_sym:
            if sorted_i_key not in ban_list:
                end_file.write(sorted_i_key + ' ' + str(sorted_dict[sorted_i_key]) + '\n')
                ban_list.append(sorted_i_key)

source_file.close()
end_file.close()