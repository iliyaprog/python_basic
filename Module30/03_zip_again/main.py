from typing import List, Any

strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result: List[Any] = list(map(lambda x, y: (x, y), strings, numbers))
print(result)
