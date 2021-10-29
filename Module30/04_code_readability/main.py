from math import sqrt

first_and_second_numbers = [0, 1]

first_list = []
first_list += (first_and_second_numbers)

for x in range(2, 1001):
    if all(x % i != 0 for i in range(2, int(sqrt(x)) + 1)):
        first_list.append(x)
print(first_list)


print(first_and_second_numbers +
      (list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(sqrt(x)) + 1))), range(2, 1001)))))


