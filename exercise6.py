# exercise6.py
# Data type: Multi-line string, r-prefix


name = 'Christian Jurilla'
age = 20

template = '''Name: {}
Age: {}
Motto: World Peace'''
print(template.format(name, age))

file = r'c:\windows\temp\secrets.txt'
print(file)