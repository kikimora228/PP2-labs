import re
txt = 'FJEWNINMaiki'
x = re.findall('[A-Z]{1}[a-z]+', txt)
print(x)