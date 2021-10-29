import collections
import zipfile

def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()

def collection_stats(file_name):
    result = {}
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    return result


def sort_stats(stats_dict):
    sorted_values = sorted(stats_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    print(stats_dict)
    print(sorted_dict)
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]

    return sorted_dict

def print_stats(stats):
    for char, count in stats.items():
        print(char, ':', count)

file_name = 'voyna-i-mir.zip'
stats = collection_stats(file_name)
stats = sort_stats(stats)
print_stats(stats)