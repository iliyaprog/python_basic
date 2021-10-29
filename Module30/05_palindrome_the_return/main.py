from collections import Counter

def can_be_poly(string):

    return len(list(filter(lambda x: x % 2, Counter(string).values()))) <= 2


print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))