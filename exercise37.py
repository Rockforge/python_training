# exercise37.py
# Function is a datatype

def getRank(element):
    # Use the zero index if tie with the first index
    return (element[1], element[0].lower())

fruits = [
    ('banana', 1), 
    ('rambutan',4),
    ('APPLE',4),
    ('GUAVA',3),
]
# Sorted case sensitive
# Pass the function as a variable
# fruits.sort(key=getRank)
fruits.sort(key=lambda x: (x[1], x[0].lower()))
print(fruits)