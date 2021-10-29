import itertools
from typing import List


list_number: List[int] = [i for i in range(10)]

first_comb: List = list(itertools.combinations_with_replacement(list_number, 2))

second_comb: List = list(itertools.permutations(list_number, 2))

end_list_one = set(first_comb + second_comb)
end_list_two = set(first_comb + second_comb)
end_list: List = list(itertools.product(end_list_one, end_list_two))

all_pin_code = []
for i_pin_code in end_list:
    pin_code = i_pin_code[0] + i_pin_code[1]
    all_pin_code.append(pin_code)

print(len(all_pin_code))
print(all_pin_code)



