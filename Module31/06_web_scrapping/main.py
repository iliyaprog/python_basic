import re
import requests


my_reg = requests.get('http://www.columbia.edu/~fdc/sample.html')
work_object = my_reg.text


print(re.findall(r'<h3.*?>(.*?)</h3>', work_object))

