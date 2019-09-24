# exercise36.py
# Function is a datatype

def getRank(element):
    return element[1]

fruits = [
    ('apple', 1), 
    ('Banana',3),
    ('rambutan',2),
    ('GUAVA',4),
]
# Sorted case sensitive
# Pass the function as a variable
# fruits.sort(key=getRank)
fruits.sort(key=lambda element: element[1])
print(fruits)