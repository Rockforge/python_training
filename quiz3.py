# quiz3.py
# Make a program that checks all odd numbers in numbers and 
# And append it to odd numbers

numbers = [1,2,3,4,5,6,7,8,9,10]

# List comprehensions
odds = [i for i in numbers if (i % 2 != 0)]

print(odds)