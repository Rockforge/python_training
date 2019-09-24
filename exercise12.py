# exercise12.py
# List slicing

fruits = [
    'Coconut',
    'Avocado',
    'Apple',
    'Melon',
    'Papaya',
    'Banana',
]



print(fruits[0:4]) # Exclusive
print(fruits[3:len(fruits)])

print(fruits[0:6:2]) # The third value is the step in slicing
print(fruits[3:])
print(fruits[:4])
print(fruits[::2])
print(fruits[::-1])
print(fruits[-3:])
print(fruits[:-4])
