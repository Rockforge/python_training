# exercise13.py

fruits = [
    'Coconut',
    'avocado',
    'apple',
    'Melon',
    'Papaya',
    'Banana',
]

# sorted_fruits = fruits # By reference

# Create a new copy of the list
sorted_fruits = list(fruits)
sorted_fruits = fruits[:]

sorted_fruits.sort()
sorted_fruits.reverse()

print(fruits)