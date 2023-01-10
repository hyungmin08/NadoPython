import re

p = re.compile('[+-]?\d+([\.?])+\d*')

text = '[ -20.0 |'
value= p.search(text)[0]
print(value)