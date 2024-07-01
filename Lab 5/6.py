import re
txt = 'dinero dinero,dinero.yeye'
x = re.sub('[ .,]', ';', txt, 4)
print(x)