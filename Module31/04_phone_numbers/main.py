import re
from typing import List


list_number: List = ['9999999999', '999999-999', '99999x9999', '8999979999', '79999x9999', '99999x99998']

for i_number in list_number:
    pattern = re.findall(r'\b[str(8), str(9)]\d{9}\b', i_number)
    if pattern:
        print('Номер {} соответствует\n'.format(i_number))
    else:
        print('Номер {} не соответствует\n'.format(i_number))