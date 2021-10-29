from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


new_floats: List[float] = list(map(lambda x: round(x ** 3, 3), floats))
print(new_floats)
new_names: List[str] = list(filter(lambda i_name: (len(i_name) >= 5), names))
print(new_names)
new_numbers: int = reduce(lambda x, y: x * y, numbers)
print(new_numbers)

