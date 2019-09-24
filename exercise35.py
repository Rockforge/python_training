# exercise35.py
# Function is a datatype
# anonymous function / lambda

def changeCase(element):
    return element.lower()

fruits = ['apple', 'Banana', 'rambutan', 'GUAVA']
# Sorted case sensitive
# Pass the function as a variable
# fruits.sort(key=changeCase)
fruits.sort(key=lambda x: x.lower())
print(fruits)